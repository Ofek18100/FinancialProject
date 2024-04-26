import yfinance as yf
import pandas as pd


SAVE_PATH = "./"

def download_stock_data(ticker_symbol, save_path=SAVE_PATH):
    """
    Download historical stock data from Yahoo Finance.

    Args:
    - ticker_symbol (str): Ticker symbol of the stock (e.g., 'AAPL' for Apple Inc.).
    - save_path (str): Path where the downloaded data will be saved.

    Returns:
    - df (DataFrame): Pandas DataFrame containing the historical stock data.
    """
    try:
        # Download historical data from Yahoo Finance
        df = yf.download(ticker_symbol, period="1y")
        
        # Save data to file
        df.to_csv(save_path + "/" + ticker_symbol + ".csv")
        return True
    except Exception as e:
        print("Error occurred:", e)
        return False
    
def get_snp_list():
    sp500_tickers = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]
    sp500_tickers = sp500_tickers.Symbol.tolist()
    return sp500_tickers 

def download_all_stocks_snp(save_path=SAVE_PATH):
    sp500_tickers = get_snp_list()
    for stock in sp500_tickers:
         download_stock_data(stock)
if __name__ == "__main__":
    download_all_stocks_snp()