# Binance Trading Bot with EMA Crossover Strategy

This is a Python trading bot that uses the Binance API to implement a simple EMA (Exponential Moving Average) crossover strategy for trading the BTCUSDT trading pair on the Binance exchange. The bot will automatically open and close positions based on EMA crossover signals.

## Prerequisites

Before using this trading bot, you need to have the following:

1. **Binance Account**: You should have an active Binance account to access the Binance API.

2. **API Key and Secret**: You need to create an API key and secret from your Binance account and replace `YOUR_API_KEY` and `YOUR_API_SECRET` with your actual API credentials in the code.

3. **Python and Libraries**: Make sure you have Python installed on your system. You'll also need to install the required libraries by running `pip install binance-client pandas numpy`.

## Configuration

You can configure the bot by modifying the following parameters in the code:

- `SYMBOL`: The trading pair you want to trade, e.g., 'BTCUSDT'.

- `SIZE`: The quantity of the asset you want to trade.

- `INTERVAL`: The Kline interval for fetching price data.

- `LIMIT`: The number of Klines to retrieve.

## How it Works

The bot follows this simple EMA crossover strategy:

- It calculates the EMA for a short period (7) and a long period (25) of historical price data.

- When the short EMA crosses above the long EMA, it opens a long position.

- When the short EMA crosses below the long EMA, it opens a short position.

- The bot closes any existing position before opening a new one based on the crossover signals.

## Usage

To run the bot:

1. Replace `YOUR_API_KEY` and `YOUR_API_SECRET` with your actual Binance API credentials.

2. Configure the `SYMBOL`, `SIZE`, `INTERVAL`, and `LIMIT` parameters as desired.

3. Execute the code in a Python environment.

The bot will continuously monitor price data and open/close positions based on the EMA crossover signals. It also handles errors and can be manually interrupted by pressing Ctrl+C.

## Disclaimer

- **Use at Your Own Risk**: Trading cryptocurrencies involves risks, and this bot is for educational purposes only. You should thoroughly understand the strategy and be aware of the risks before using it for real trading.

- **API Security**: Keep your API key and secret secure and do not share them with anyone. Be cautious when using API keys with trading bots.

- **Financial Responsibility**: You are solely responsible for any gains or losses incurred while using this bot. Always trade responsibly and consider your risk tolerance.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to modify and improve this README to better suit your project. Include any additional information, warnings, or usage instructions that are relevant to your specific use case.
