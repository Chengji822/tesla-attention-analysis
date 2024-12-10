
'''
the file is to get weekly attention data of tesla from Google
'''

from pytrends.request import TrendReq
import pandas as pd
import yfinance as yf
import time


def getTeslaAttentionData():
# Initialize pytrends
    pytrends = TrendReq(hl='en-US', tz=360)

    # Define the search term and time chunks
    search_term = 'Tesla'

    timeframes = [
        '2014-01-01 2015-12-31',
        '2016-01-01 2017-12-31',
        '2018-01-01 2019-12-31',
        '2020-01-01 2021-12-31',
        '2022-01-01 2024-12-10'
    ]

    # Initialize an empty DataFrame
    all_data = pd.DataFrame()

    # Loop through each timeframe and fetch data
    for timeframe in timeframes:
        print(f"working on {timeframe}")
        pytrends.build_payload([search_term], cat=0, timeframe=timeframe, geo='', gprop='')
        data = pytrends.interest_over_time()
        if not data.empty:
            data = data.drop(columns=['isPartial'])
            all_data = pd.concat([all_data, data], axis=0)  # Append the data
        time.sleep(20)  # Respect rate limits


    # Fill or interpolate missing values as appropriate:
    all_data = all_data.fillna(method='ffill').fillna(method='bfill')

    # Reset the index to ensure proper alignment
    all_data.reset_index(inplace=True)

    return all_data


def getTeslaStockPriceInfo():
    # Fetch Tesla stock data from Yahoo Finance
    ticker = "TSLA"
    start_date = "2013-12-30"
    end_date = "2024-12-10"

    # Download the weekly stock data
    tesla_stock = yf.download(ticker, start=start_date, end=end_date, interval="1wk")

    # Reset index to make the data easier to merge
    tesla_stock.reset_index(inplace=True)

    # Select only relevant columns
    tesla_stock = tesla_stock[['Date', 'Close']]

    # Rename columns for clarity
    tesla_stock.rename(columns={"Date": "Week", "Close": "Stock Price"}, inplace=True)

    return tesla_stock


def combine_data(google_trends, tesla_stock):
    # Load the weekly Google Trends data for Tesla (assuming the file exists from earlier steps)
    google_trends = pd.read_csv('Final_tesla_attention_weekly.csv')
    tesla_stock = pd.read_csv('Final_tesla_weekly_stockPrice.csv')

    # Ensure that both datasets have their date columns in the same format and frequency.
    google_trends['date'] = pd.to_datetime(google_trends['date'])
    tesla_stock['Week'] = pd.to_datetime(tesla_stock['Week'])

    google_trends['date'] = google_trends['date'] - pd.Timedelta(days=6)  # Adjust to match week start

    # Merge the datasets on the 'Week' column
    combined_data = pd.merge(google_trends, tesla_stock, left_on='date', right_on='Week', how='inner')

    # Drop redundant columns
    combined_data.drop(columns=['Week'], inplace=True)

    combined_data.dropna()
    combined_data.rename(columns={
        'date': 'Week',  # Rename 'date' to 'Week'
        'Tesla': 'Google Trends Attention',  # Rename 'Tesla' to indicate attention data
        'Stock Price': 'Weekly Stock Price'  # Rename 'Stock Price' for clarity
    }, inplace=True)

    # Save the combined dataset
    return combined_data

