API_KEY = 'YOUR_API_KEY'
API_SECRET = 'YOUR_API_SECRET'

from binance.client import Client
import pandas as pd
import numpy as np
import time
import sys

# Configure various settings
SYMBOL = 'BTCUSDT'
SIZE = 0.001
INTERVAL = Client.KLINE_INTERVAL_15MINUTE
LIMIT = 101

# Create a Client to connect to the Binance API
client = Client(api_key=API_KEY, api_secret=API_SECRET)

def calculate_ema(data, period):
    ema = pd.Series(data).ewm(span=period, adjust=False).mean()
    return ema.tolist()

def open_position(side):
    order_side = Client.SIDE_BUY if side == "long" else Client.SIDE_SELL
    order = client.futures_create_order(
        symbol=SYMBOL,
        side=order_side,
        type=Client.ORDER_TYPE_MARKET,
        quantity=SIZE,
    )
    print("Position opened:", order)
    return side

def close_position(current_side):
    order_side = Client.SIDE_SELL if current_side == "long" else Client.SIDE_BUY
    close_order = client.futures_create_order(
        symbol=SYMBOL,
        side=order_side,
        type=Client.ORDER_TYPE_MARKET,
        quantity=SIZE,
    )
    print("Position closed:", close_order)
    return None

position_side = None

while True:
    try:
        current_time = int(time.time())
        current_second = current_time % 60

        print(current_second)
        if current_second == 0:
            klines = client.futures_klines(
                symbol=SYMBOL, interval=INTERVAL, limit=LIMIT)

            close_prices = np.array([float(candle[4])
                                    for candle in klines[:-1]])
            timestamps = np.array([candle[0] for candle in klines[:-1]])

            ema_7 = calculate_ema(close_prices, 7)
            ema_25 = calculate_ema(close_prices, 25)

            print("Timestamp:", pd.to_datetime(timestamps[-1], unit='ms'))
            print("EMA 7:", ema_7[-1])
            print("EMA 25:", ema_25[-1])

            if ema_7[-1] > ema_25[-1] and position_side != "long":
                if position_side:
                    print("Close position")
                    close_position(position_side)
                    time.sleep(1)
                print("Open long position")
                position_side = open_position("long")

            elif ema_7[-1] < ema_25[-1] and position_side != "short":
                if position_side:
                    print("Close position")
                    close_position(position_side)
                    time.sleep(1)
                print("Open short position")
                position_side = open_position("short")

        time.sleep(1)
    except Exception as e:
        print("An error occurred:", str(e))
        if position_side:
            print("Closing position due to error")
            close_position(position_side)
        sys.exit()  # Exit the program
    except KeyboardInterrupt:
        print("KeyboardInterrupt: Closing position")
        if position_side:
            close_position(position_side)
        sys.exit()  # Exit the program
