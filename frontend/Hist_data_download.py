# from pya3 import *
# import datetime
# import pandas as pd

# # AliceBlue credentials
# username1 = '1243841'
# api_key1 = 'BfCY1jP6p2HvW0t1FaOM3dbMpEk8gyWuVEJxgyVTNcXXokxAbARTEW2Hh8NF8QqzQEIyfxBMAA5E6WteQXBt31c2NpoPm19STQnvqVvTCOTUStOHBeAoFsncDyvn3cSs'
# alice = Aliceblue(user_id=username1, api_key=api_key1)
# alice.get_session_id()

# # Function to download stock data
# def download_stock_data(symbol, exchange, from_date, to_date):
#     try:
#         # Get instrument details for the symbol
#         instrument = alice.get_instrument_by_symbol(exchange, symbol)
		
#         # Fetch historical data
#         stock_data = alice.get_historical(instrument, from_date, to_date, "1", False)
		
#         # Set index as datetime
#         stock_data.set_index(pd.DatetimeIndex(stock_data['datetime']), inplace=True)
		
#         # Resample the data (1-minute frequency)
#         stock_data_resampled = stock_data.groupby(pd.Grouper(freq='1min')).agg({
#             "open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"
#         })

#         # Avoid weekends (Saturday and Sunday)
#         stock_data_resampled = stock_data_resampled[stock_data_resampled.index.dayofweek < 5]

#         # Filter data between trading hours (09:15 to 15:30)
#         start_time = pd.Timestamp("09:15:00")
#         end_time = pd.Timestamp("15:30:00")
#         mask = (stock_data_resampled.index.time >= start_time.time()) & (stock_data_resampled.index.time <= end_time.time())
#         stock_data_filtered = stock_data_resampled[mask]

#         # for Eod Data
#         stock_data_filtered = stock_data_resampled

#         # Add 'Name' column with the stock symbol
#         stock_data_filtered['Name'] = symbol

#         # Split datetime into 'Date' and 'Time' columns
#         stock_data_filtered['Date'] = stock_data_filtered.index.date
#         stock_data_filtered['Time'] = stock_data_filtered.index.time

#         # Define a filename for the CSV file
#         filename = f"D:/Kaustubh/Python/PrateekSingh/stockdata/{symbol}.csv"

#         # Save the processed data to CSV
#         stock_data_filtered.to_csv(filename, index=False)  # index=False removes the datetime index from the CSV
#         print(f"Data for {symbol} saved to {filename}")

#     except Exception as e:
#         print(f"Error downloading data for {symbol}: {e}")

# # Load the CSV file containing the symbols
# symbol_file = 'D:/Kaustubh/Python/PrateekSingh/NSE_sym_list.csv'  # Replace with the actual path to your file
# symbols_df = pd.read_csv(symbol_file)

# # Define the date range
# from_datetime = datetime.datetime.now() - datetime.timedelta(days=60)
# to_datetime = datetime.datetime.now()

# # Loop through each symbol and download data
# for index, row in symbols_df.iterrows():
#     sym = row['Symbol']  # Assuming the column name is 'Symbol'
#     exch = "NSE"  # Change the exchange if needed
#     download_stock_data(sym, exch, from_datetime, to_datetime)







# from pya3 import *
# import datetime
# import pandas as pd

# # AliceBlue credentials
# username1 = '1243841'
# api_key1 = 'BfCY1jP6p2HvW0t1FaOM3dbMpEk8gyWuVEJxgyVTNcXXokxAbARTEW2Hh8NF8QqzQEIyfxBMAA5E6WteQXBt31c2NpoPm19STQnvqVvTCOTUStOHBeAoFsncDyvn3cSs'
# alice = Aliceblue(user_id=username1, api_key=api_key1)
# alice.get_session_id()

# # Function to download stock data
# def download_stock_data(symbol, exchange, from_date, to_date):
#     try:
#         # Get instrument details for the symbol
#         instrument = alice.get_instrument_by_symbol(exchange, symbol)
		
#         # Fetch historical data
#         stock_data = alice.get_historical(instrument, from_date, to_date, "1", False)
		
#         # Set index as datetime
#         stock_data.set_index(pd.DatetimeIndex(stock_data['datetime']), inplace=True)
		
#         # Resample the data (1-minute frequency)
#         stock_data_resampled = stock_data.groupby(pd.Grouper(freq='1min')).agg({
#             "open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"
#         })

#         # Avoid weekends (Saturday and Sunday)
#         stock_data_resampled = stock_data_resampled[stock_data_resampled.index.dayofweek < 5]

#         # Filter data between trading hours (09:15 to 15:30)
#         start_time = pd.Timestamp("09:15:00")
#         end_time = pd.Timestamp("15:29:00")
#         mask = (stock_data_resampled.index.time >= start_time.time()) & (stock_data_resampled.index.time <= end_time.time())
#         stock_data_filtered = stock_data_resampled[mask]  # Ensure filtering before final assignment

#         # Add 'Name' column with the stock symbol
#         stock_data_filtered['Ticker'] = symbol

#         # Split datetime into 'Date' and 'Time' columns
#         stock_data_filtered['Date'] = stock_data_filtered.index.date
#         stock_data_filtered['Time'] = stock_data_filtered.index.time

#         # Define a filename for the CSV file
#         filename = f"D:/Kaustubh/Python/PrateekSingh/stockdata/{symbol}.csv"

#         # Save the processed data to CSV
#         stock_data_filtered.to_csv(filename, index=False)  # index=False removes the datetime index from the CSV
#         print(f"Data for {symbol} saved to {filename}")

#     except Exception as e:
#         print(f"Error downloading data for {symbol}: {e}")

# # Load the CSV file containing the symbols
# symbol_file = 'D:/Kaustubh/Python/PrateekSingh/NSE_sym_list.csv'  # Replace with the actual path to your file
# symbols_df = pd.read_csv(symbol_file)

# # Define the date range
# from_datetime = datetime.datetime.now() - datetime.timedelta(days=60)
# to_datetime = datetime.datetime.now()

# # Loop through each symbol and download data
# for index, row in symbols_df.iterrows():
#     sym = row['Symbol']  # Assuming the column name is 'Symbol'
#     exch = "NSE"  # Change the exchange if needed
#     download_stock_data(sym, exch, from_datetime, to_datetime)





# 













# from pya3 import *
# import datetime
# import pandas as pd

# # AliceBlue credentials
# username1 = '1243841'
# api_key1 = 'BfCY1jP6p2HvW0t1FaOM3dbMpEk8gyWuVEJxgyVTNcXXokxAbARTEW2Hh8NF8QqzQEIyfxBMAA5E6WteQXBt31c2NpoPm19STQnvqVvTCOTUStOHBeAoFsncDyvn3cSs'
# alice = Aliceblue(user_id=username1, api_key=api_key1)
# alice.get_session_id()

# # Function to download stock data
# def download_stock_data(symbol, exchange, from_date, to_date):
#     try:
#         # Get instrument details for the symbol
#         instrument = alice.get_instrument_by_symbol(exchange, symbol)
		
#         # Fetch historical data
#         stock_data = alice.get_historical(instrument, from_date, to_date, "1", False)
		
#         # Set index as datetime
#         stock_data.set_index(pd.DatetimeIndex(stock_data['datetime']), inplace=True)
		
#         # Resample the data (1-minute frequency)
#         stock_data_resampled = stock_data.groupby(pd.Grouper(freq='1min')).agg({
#             "open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"
#         })

#         # Avoid weekends (Saturday and Sunday)
#         stock_data_resampled = stock_data_resampled[stock_data_resampled.index.dayofweek < 5]

#         # Filter data between trading hours (09:15 to 15:30)
#         start_time = pd.Timestamp("09:15:00")
#         end_time = pd.Timestamp("15:29:00")
#         mask = (stock_data_resampled.index.time >= start_time.time()) & (stock_data_resampled.index.time <= end_time.time())
#         stock_data_filtered = stock_data_resampled.loc[mask]  # Use .loc[] to avoid warnings

#         # Add 'Ticker' column with the stock symbol
#         stock_data_filtered.loc[:, 'Ticker'] = symbol  # Use .loc[] to avoid warnings

#         # Split datetime into 'Date' and 'Time' columns
#         stock_data_filtered.loc[:, 'Date'] = stock_data_filtered.index.date
#         stock_data_filtered.loc[:, 'Time'] = stock_data_filtered.index.time

#         # Reorder columns to match the desired format
#         stock_data_filtered = stock_data_filtered[['Ticker', 'Date', 'Time', 'open', 'high', 'low', 'close', 'volume']]

#         # Define a filename for the CSV file
#         filename = f"D:/Kaustubh/Python/PrateekSingh/stockdata/{symbol}.csv"

#         # Save the processed data to CSV
#         stock_data_filtered.to_csv(filename, index=False)  # index=False removes the datetime index from the CSV
#         print(f"Data for {symbol} saved to {filename}")

#     except Exception as e:
#         print(f"Error downloading data for {symbol}: {e}")

# # Load the CSV file containing the symbols
# symbol_file = 'D:/Kaustubh/Python/PrateekSingh/NSE_sym_list.csv'  # Replace with the actual path to your file
# symbols_df = pd.read_csv(symbol_file)

# # Define the date range
# from_datetime = datetime.datetime.now() - datetime.timedelta(days=60)
# to_datetime = datetime.datetime.now()

# # Loop through each symbol and download data
# for index, row in symbols_df.iterrows():
#     sym = row['Symbol']  # Assuming the column name is 'Symbol'
#     exch = "NSE"  # Change the exchange if needed
#     download_stock_data(sym, exch, from_datetime, to_datetime)













####### WORKING CODE ==================


# from pya3 import *
# import datetime
# import pandas as pd

# # # AliceBlue credentials
# # username1 = '1243841'
# # api_key1 = 'BfCY1jP6p2HvW0t1FaOM3dbMpEk8gyWuVEJxgyVTNcXXokxAbARTEW2Hh8NF8QqzQEIyfxBMAA5E6WteQXBt31c2NpoPm19STQnvqVvTCOTUStOHBeAoFsncDyvn3cSs'

# username1 = '488059'
# api_key1 = 'FTlDyv5M6j931VGZ6elvlU7HgWYkWy5IWrFeyAAF15QULcYIgsPS8Cyli4lFW481DF6sfDy7zkfNXQ6XFclL0RkuTIJeFRK566xOZM3qcQRhvIyn3AFiTrhIhdy883by'


# alice = Aliceblue(user_id=username1, api_key=api_key1)
# alice.get_session_id()
# print(alice.get_session_id)

# # Function to download stock data
# def download_stock_data(symbol, exchange, from_date, to_date):
#     try:
#         # Get instrument details for the symbol
#         instrument = alice.get_instrument_by_symbol(exchange, symbol)
		
#         # Fetch historical data
#         stock_data = alice.get_historical(instrument, from_date, to_date, "1", False)
		
#         # Check if the returned data is a DataFrame
#         if isinstance(stock_data, pd.DataFrame):
#             # Set index as datetime
#             stock_data.set_index(pd.DatetimeIndex(stock_data['datetime']), inplace=True)

#             # Resample the data (1-minute frequency)
#             stock_data_resampled = stock_data.groupby(pd.Grouper(freq='1min')).agg({
#                 "open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"
#             })

#             # Avoid weekends (Saturday and Sunday)
#             stock_data_resampled = stock_data_resampled[stock_data_resampled.index.dayofweek < 5]

#             # Filter data between trading hours (09:15 to 15:30)
#             start_time = pd.Timestamp("09:15:00")
#             end_time = pd.Timestamp("15:29:00")
#             mask = (stock_data_resampled.index.time >= start_time.time()) & (stock_data_resampled.index.time <= end_time.time())
#             stock_data_filtered = stock_data_resampled.loc[mask]

#             # Add 'Ticker' column with the stock symbol
#             stock_data_filtered.loc[:, 'Ticker'] = symbol

#             # Split datetime into 'Date' and 'Time' columns
#             stock_data_filtered.loc[:, 'Date'] = stock_data_filtered.index.date
#             stock_data_filtered.loc[:, 'Time'] = stock_data_filtered.index.time

#             # Reorder columns to match the desired format
#             stock_data_filtered = stock_data_filtered[['Ticker', 'Date', 'Time', 'open', 'high', 'low', 'close', 'volume']]

#             # Define a filename for the CSV file
#             filename = f"stockdata/{symbol}.csv"

#             # Save the processed data to CSV
#             stock_data_filtered.to_csv(filename, index=False)
#             print(f"Data for {symbol} saved to {filename}")
#         else:
#             print(f"Unexpected data format for {symbol}: {type(stock_data)}")

#     except Exception as e:
#         print(f"Error downloading data for {symbol}: {e}")

# # Load the CSV file containing the symbols
# # symbol_file = 'NSE_sym_list.csv'  # Replace with the actual path to your file
# symbol_file = 'selected_symbols.csv'  # Replace with the actual path to your file
# symbols_df = pd.read_csv(symbol_file)

# # Define the date range
# from_datetime = datetime.datetime.now() - datetime.timedelta(days=120)
# to_datetime = datetime.datetime.now()

# # # Loop through each symbol and download data
# # for index, row in symbols_df.iterrows():
# #     #sym = row['Symbol']  # Assuming the column name is 'Symbol'
# #     sym = row['Trading Symbol']  # Assuming the column name is 'Trading Symbol'
# #     exch = "NSE"  # Change the exchange if needed
# #     download_stock_data(sym, exch, from_datetime, to_datetime)

# # Loop through each symbol and download data
# for index, row in symbols_df.iterrows():
#     sym = row['Trading Symbol']  # Assuming the column name is 'Trading Symbol'
#     exch = row['EXCH'] if 'EXCH' in row and pd.notna(row['EXCH']) else 'NSE'  # Use 'EXCH' from the file or default to 'NSE' if missing
#     download_stock_data(sym, exch, from_datetime, to_datetime)





# from pya3 import *
# import datetime
# import pandas as pd
# from datetime import datetime, timedelta
# import time
# # # AliceBlue credentials
# # username1 = '1243841'
# # api_key1 = 'BfCY1jP6p2HvW0t1FaOM3dbMpEk8gyWuVEJxgyVTNcXXokxAbARTEW2Hh8NF8QqzQEIyfxBMAA5E6WteQXBt31c2NpoPm19STQnvqVvTCOTUStOHBeAoFsncDyvn3cSs'

# username1 = '488059'
# api_key1 = 'FTlDyv5M6j931VGZ6elvlU7HgWYkWy5IWrFeyAAF15QULcYIgsPS8Cyli4lFW481DF6sfDy7zkfNXQ6XFclL0RkuTIJeFRK566xOZM3qcQRhvIyn3AFiTrhIhdy883by'


# alice = Aliceblue(user_id=username1, api_key=api_key1)
# alice.get_session_id()
# print(alice.get_session_id)

# instrument = alice.get_instrument_by_symbol("MCX", "GOLD26NOV24C80000")
# from_datetime = datetime.now() - timedelta(days=30)     # From last & days
# to_datetime = datetime.now()                                    # To now
# interval = "1"       # ["1", "D"]
# indices = False      # For Getting index data
# print(alice.get_historical(instrument, from_datetime, to_datetime, interval, indices))




# from pya3 import Aliceblue
# import datetime
# import pandas as pd
# from datetime import timedelta

# # AliceBlue credentials
# username1 = '488059'
# api_key1 = 'FTlDyv5M6j931VGZ6elvlU7HgWYkWy5IWrFeyAAF15QULcYIgsPS8Cyli4lFW481DF6sfDy7zkfNXQ6XFclL0RkuTIJeFRK566xOZM3qcQRhvIyn3AFiTrhIhdy883by'

# # Initialize AliceBlue session
# alice = Aliceblue(user_id=username1, api_key=api_key1)
# alice.get_session_id()
# print("Session ID:", alice.get_session_id())

# # Function to download stock data
# def download_stock_data(symbol, exchange, from_date, to_date):
#     try:
#         # Get instrument details for the symbol
#         instrument = alice.get_instrument_by_symbol(exchange, symbol)
		
#         # Fetch historical data
#         stock_data = alice.get_historical(instrument, from_date, to_date, "1", False)
		
#         # Check if the returned data is a DataFrame
#         if isinstance(stock_data, pd.DataFrame):
#             # Set index as datetime
#             stock_data.set_index(pd.DatetimeIndex(stock_data['datetime']), inplace=True)

#             # Resample the data (1-minute frequency)
#             stock_data_resampled = stock_data.groupby(pd.Grouper(freq='1min')).agg({
#                 "open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"
#             })

#             # Avoid weekends (Saturday and Sunday)
#             stock_data_resampled = stock_data_resampled[stock_data_resampled.index.dayofweek < 5]

#             # Filter data between trading hours (09:15 to 15:30)
#             start_time = pd.Timestamp("09:15:00")
#             end_time = pd.Timestamp("15:29:00")
#             mask = (stock_data_resampled.index.time >= start_time.time()) & (stock_data_resampled.index.time <= end_time.time())
#             stock_data_filtered = stock_data_resampled.loc[mask]

#             # Add 'Ticker' column with the stock symbol
#             stock_data_filtered.loc[:, 'Ticker'] = symbol

#             # Split datetime into 'Date' and 'Time' columns
#             stock_data_filtered.loc[:, 'Date'] = stock_data_filtered.index.date
#             stock_data_filtered.loc[:, 'Time'] = stock_data_filtered.index.time

#             # Reorder columns to match the desired format
#             stock_data_filtered = stock_data_filtered[['Ticker', 'Date', 'Time', 'open', 'high', 'low', 'close', 'volume']]

#             # Define a filename for the CSV file
#             filename = f"stockdata/{symbol}.csv"

#             # Save the processed data to CSV
#             stock_data_filtered.to_csv(filename, index=False)
#             print(f"Data for {symbol} saved to {filename}")
#         else:
#             print(f"Unexpected data format for {symbol}: {type(stock_data)}")

#     except Exception as e:
#         print(f"Error downloading data for {symbol}: {e}")

# # Load the CSV file containing the symbols and exchange
# symbol_file = 'selected_symbols.csv'  # Replace with the actual path to your file
# symbols_df = pd.read_csv(symbol_file)

# # Define the date range for historical data
# from_datetime = datetime.datetime.now() - timedelta(days=40)
# to_datetime = datetime.datetime.now()

# # Loop through each symbol and download data
# for index, row in symbols_df.iterrows():
#     sym = row['Trading Symbol']  # Assuming the column name is 'Trading Symbol'
#     exch = row['EXCH'] if 'EXCH' in row and pd.notna(row['EXCH']) else 'NSE'  # Use 'EXCH' from the file or default to 'NSE' if missing
#     download_stock_data(sym, exch, from_datetime, to_datetime)


# from pya3 import Aliceblue
# import datetime
# import pandas as pd
# from datetime import timedelta

# # AliceBlue credentials
# username1 = '488059'
# api_key1 = 'FTlDyv5M6j931VGZ6elvlU7HgWYkWy5IWrFeyAAF15QULcYIgsPS8Cyli4lFW481DF6sfDy7zkfNXQ6XFclL0RkuTIJeFRK566xOZM3qcQRhvIyn3AFiTrhIhdy883by'

# # Initialize AliceBlue session
# alice = Aliceblue(user_id=username1, api_key=api_key1)
# alice.get_session_id()
# print("Session ID:", alice.get_session_id())

# # Function to download stock data
# def download_stock_data(symbol, exchange, from_date, to_date):
#     try:
#         # Get instrument details for the symbol
#         instrument = alice.get_instrument_by_symbol(exchange, symbol)
		
#         # Fetch historical data
#         stock_data = alice.get_historical(instrument, from_date, to_date, "1", False)
		
#         # Check if the returned data is a DataFrame
#         if isinstance(stock_data, pd.DataFrame):
#             # Set index as datetime
#             stock_data.set_index(pd.DatetimeIndex(stock_data['datetime']), inplace=True)

#             # Resample the data (1-minute frequency)
#             stock_data_resampled = stock_data.groupby(pd.Grouper(freq='1min')).agg({
#                 "open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"
#             })

#             # Avoid weekends (Saturday and Sunday)
#             stock_data_resampled = stock_data_resampled[stock_data_resampled.index.dayofweek < 5]

#             # Filter data between trading hours (09:15 to 15:30)
#             start_time = pd.Timestamp("09:15:00")
#             end_time = pd.Timestamp("15:29:00")
#             mask = (stock_data_resampled.index.time >= start_time.time()) & (stock_data_resampled.index.time <= end_time.time())
#             stock_data_filtered = stock_data_resampled.loc[mask]

#             # Add 'Ticker' column with the stock symbol (without -EQ)
#             stock_data_filtered.loc[:, 'Ticker'] = symbol

#             # Split datetime into 'Date' and 'Time' columns
#             stock_data_filtered.loc[:, 'Date'] = stock_data_filtered.index.date
#             stock_data_filtered.loc[:, 'Time'] = stock_data_filtered.index.time

#             # Reorder columns to match the desired format
#             stock_data_filtered = stock_data_filtered[['Ticker', 'Date', 'Time', 'open', 'high', 'low', 'close', 'volume']]

#             # Define a filename for the CSV file
#             filename = f"stockdata/{symbol}.csv"

#             # Save the processed data to CSV
#             stock_data_filtered.to_csv(filename, index=False)
#             print(f"Data for {symbol} saved to {filename}")
#         else:
#             print(f"Unexpected data format for {symbol}: {type(stock_data)}")

#     except Exception as e:
#         print(f"Error downloading data for {symbol}: {e}")

# # Load the CSV file containing the symbols and exchange
# symbol_file = 'selected_symbols.csv'  # Replace with the actual path to your file
# symbols_df = pd.read_csv(symbol_file)

# # Define the date range for historical data
# from_datetime = datetime.datetime.now() - timedelta(days=40)
# to_datetime = datetime.datetime.now()

# # Loop through each symbol and download data
# for index, row in symbols_df.iterrows():
#     sym = row['Trading Symbol'].replace("-EQ", "")  # Remove '-EQ' suffix if present
#     exch = row['EXCH'] if 'EXCH' in row and pd.notna(row['EXCH']) else 'NSE'  # Use 'EXCH' from the file or default to 'NSE' if missing
#     download_stock_data(sym, exch, from_datetime, to_datetime)













from pya3 import Aliceblue
import datetime
import pandas as pd
from datetime import timedelta

# AliceBlue credentials
username1 = '488059'
api_key1 = 'FTlDyv5M6j931VGZ6elvlU7HgWYkWy5IWrFeyAAF15QULcYIgsPS8Cyli4lFW481DF6sfDy7zkfNXQ6XFclL0RkuTIJeFRK566xOZM3qcQRhvIyn3AFiTrhIhdy883by'

# Initialize AliceBlue session
alice = Aliceblue(user_id=username1, api_key=api_key1)
alice.get_session_id()
print("Session ID:", alice.get_session_id())

# Function to download stock data
def download_stock_data(symbol, exchange, from_date, to_date):
	try:
		# Get instrument details for the symbol
		instrument = alice.get_instrument_by_symbol(exchange, symbol)
		
		# Fetch historical data
		stock_data = alice.get_historical(instrument, from_date, to_date, "1", False)
		
		# Check if the returned data is a DataFrame
		if isinstance(stock_data, pd.DataFrame):
			# Set index as datetime
			stock_data.set_index(pd.DatetimeIndex(stock_data['datetime']), inplace=True)

			# Resample the data (1-minute frequency)
			stock_data_resampled = stock_data.groupby(pd.Grouper(freq='1min')).agg({
				"open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"
			})

			# Avoid weekends (Saturday and Sunday)
			stock_data_resampled = stock_data_resampled[stock_data_resampled.index.dayofweek < 5]

			# Filter data between trading hours (09:15 to 15:30)
			start_time = pd.Timestamp("09:15:00")
			end_time = pd.Timestamp("15:29:00")
			mask = (stock_data_resampled.index.time >= start_time.time()) & (stock_data_resampled.index.time <= end_time.time())
			stock_data_filtered = stock_data_resampled.loc[mask]

			# Add 'Ticker' column with the stock symbol (without -EQ)
			stock_data_filtered.loc[:, 'Ticker'] = symbol

			# Split datetime into 'Date' and 'Time' columns
			stock_data_filtered.loc[:, 'Date'] = stock_data_filtered.index.date
			stock_data_filtered.loc[:, 'Time'] = stock_data_filtered.index.time

			# Reorder columns to match the desired format
			stock_data_filtered = stock_data_filtered[['Ticker', 'Date', 'Time', 'open', 'high', 'low', 'close', 'volume']]

			# Drop rows with any missing data
			stock_data_filtered.dropna(inplace=True)

			# Ensure numeric columns are in the correct format; drop rows with non-numeric values
			stock_data_filtered = stock_data_filtered[pd.to_numeric(stock_data_filtered['open'], errors='coerce').notna()]
			stock_data_filtered = stock_data_filtered[pd.to_numeric(stock_data_filtered['high'], errors='coerce').notna()]
			stock_data_filtered = stock_data_filtered[pd.to_numeric(stock_data_filtered['low'], errors='coerce').notna()]
			stock_data_filtered = stock_data_filtered[pd.to_numeric(stock_data_filtered['close'], errors='coerce').notna()]
			stock_data_filtered = stock_data_filtered[pd.to_numeric(stock_data_filtered['volume'], errors='coerce').notna()]

			# Define a filename for the CSV file
			# filename = f"stockdata/{symbol}.csv"
			filename = f"Selected/{symbol}.csv"

			# Save the cleaned data to CSV
			stock_data_filtered.to_csv(filename, index=False)
			print(f"Cleaned data for {symbol} saved to {filename}")
		else:
			print(f"Unexpected data format for {symbol}: {type(stock_data)}")

	except Exception as e:
		print(f"Error downloading data for {symbol}: {e}")

# Load the CSV file containing the symbols and exchange
# symbol_file = 'selected_symbols.csv'  # Replace with the actual path to your file
symbol_file = 'NSEtoken1.csv'  # Replace with the actual path to your file
symbols_df = pd.read_csv(symbol_file)

# Define the date range for historical data
from_datetime = datetime.datetime.now() - timedelta(days=1200)
to_datetime = datetime.datetime.now()

# Loop through each symbol and download data
for index, row in symbols_df.iterrows():
	#sym = row['Trading Symbol']  # Assuming the column name is 'Trading Symbol'
	sym = row['Trading Symbol'].replace("-EQ", "")  # Remove '-EQ' suffix if present
	exch = row['EXCH'] if 'EXCH' in row and pd.notna(row['EXCH']) else 'NSE'  # Use 'EXCH' from the file or default to 'NSE' if missing
	download_stock_data(sym, exch, from_datetime, to_datetime)
