import os
import pandas as pd

import os
import pandas as pd

DATA_BASE_PATH="/home/guysh/InvestingProject/DataBase"

def read_stock_data(directory):
    """
    Read historical stock data from CSV files in the specified directory.

    Args:
    - directory (str): Directory path containing the CSV files.

    Returns:
    - data (dict): Dictionary containing DataFrame objects for each stock.
    """
    data = {}
    for file_name in os.listdir(directory):
        if file_name.endswith('.csv'):
            file_path = os.path.join(directory, file_name)
            ticker_symbol = os.path.splitext(file_name)[0]
            data[ticker_symbol] = pd.read_csv(file_path)
    return data

def calculate_sma(df, window):
    """
    Calculate the simple moving average (SMA) of a DataFrame.

    Args:
    - df (DataFrame): DataFrame containing stock data.
    - window (int): Window size for the SMA calculation.

    Returns:
    - sma (Series): Series containing the SMA values.
    """
    return df['Close'].rolling(window=window).mean()

def calculate_distance_from_sma(df, sma):
    """
    Calculate the distance from the simple moving average (SMA) of a DataFrame.

    Args:
    - df (DataFrame): DataFrame containing stock data.
    - sma (Series): Series containing the SMA values.

    Returns:
    - distance (float): Distance from the SMA in percentage terms.
    """
    distance = 100
    try:
        latest_close = df['Close'].iloc[-1]
        print(latest_close)
        latest_sma = sma.iloc[-1]
        print(latest_sma)
        distance = ((latest_close - latest_sma) / latest_close) * 100
    except:
        pass
    print(distance)
    return distance

def analyze_stock_data(data):
    """
    Analyze historical stock data and calculate distance from the simple moving average (SMA).

    Args:
    - data (dict): Dictionary containing DataFrame objects for each stock.

    Returns:
    - sorted_stocks (list): List of tuples containing ticker symbols and distances from SMAs.
    """
    sma_150 = {}
    sma_200 = {}
    for ticker_symbol, df in data.items():
        # Calculate SMA(150) and SMA(200)
        sma_150[ticker_symbol] = calculate_sma(df, window=150)
        sma_200[ticker_symbol] = calculate_sma(df, window=200)

    distances = {}
    for ticker_symbol, df in data.items():
        # Calculate distances from SMAs
        distance_150 = calculate_distance_from_sma(df, sma_150[ticker_symbol])
        distance_200 = calculate_distance_from_sma(df, sma_200[ticker_symbol])
        # Add maximum distance to distances dictionary
        distances[ticker_symbol] = round(min(distance_150, distance_200),2)
    # Sort stocks by distance from SMAs
    sorted_stocks = sorted(distances.items(), key=lambda x: abs(x[1]))

    return sorted_stocks

def analyze_all_stocks():
    # Directory containing CSV files of historical stock data
    data_directory = DATA_BASE_PATH

    # Step 1: Read data
    data = read_stock_data(data_directory)

    # Step 2: Analyze data and calculate distances from SMAs
    sorted_stocks = analyze_stock_data(data)

    # Display sorted stocks
    for ticker_symbol, distance in sorted_stocks:
        print(f"{ticker_symbol}: Distance from SMAs: {distance:.2f}%")
    return sorted_stocks

def calculate_distance_from_sma_for_stock(stock_symbol):
    """
    Calculate the distance from the SMA for a given stock symbol.

    Args:
    - stock_symbol (str): Ticker symbol of the stock.

    Returns:
    - distance (float): Distance from the SMA in percentage terms.
    """
    file_path = os.path.join(DATA_BASE_PATH, f"{stock_symbol}.csv")
    if not os.path.exists(file_path):
        print(file_path + "not exist")
        return None

    df = pd.read_csv(file_path)
    sma_150 = calculate_sma(df, window=150) 
    sma_200 = calculate_sma(df, window=200)
    distance_150 = calculate_distance_from_sma(df, sma_150)
    distance_200 = calculate_distance_from_sma(df, sma_200)
    #print(str(sma_150) + " " + str(distance_150))
    #print(str(sma_200) + " " + str(distance_200))
    if abs(distance_200) < abs(distance_150):
        return round(distance_200,2)
    return round(distance_150,2)

if __name__ == '__main__':
    # Directory containing CSV files of historical stock data
    data_directory = "../"
    o = calculate_distance_from_sma_for_stock("TSLA")
