# Cryptocurrency Dashboard

# Import Libraries
import os
import keys
import requests
import pandas as pd
import plotly.graph_objects as go
import matplotlib.colors as mcolors
from datetime import datetime, timedelta


# Binance API Constants
load_dotenv('keys.env')
BINANCE_API_KEY = os.getenv('BINANCE_API_KEY')
BINANCE_API_URL = 'https://api.binance.us/api/v3/klines'
BINANCE_API_URL_CURRENT_PRICE = 'https://api.binance.us/api/v3/ticker/price?symbol='

# File Path for the CSV
CSV_FILE_PATH = 'all_time_data.csv'

# Helper Functions

def fetch_historical_data(symbol='BTCUSDT', interval='1d', start_time=None, end_time=None, limit=1000):
    """Fetch historical data for a given symbol from Binance API."""
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': limit,
        'startTime': start_time,
        'endTime': end_time
    }
    response = requests.get(BINANCE_API_URL, headers={'X-MBX-APIKEY': BINANCE_API_KEY}, params=params)

    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return None

    data = response.json()
    df = pd.DataFrame(data, columns=[
        'Open Time', 'Open', 'High', 'Low', 'Close', 'Volume',
        'Close Time', 'Quote Asset Volume', 'Number of Trades',
        'Taker Buy Base Asset Volume', 'Taker Buy Quote Asset Volume', 'Ignore'
    ])
    df['Date'] = pd.to_datetime(df['Open Time'], unit='ms')
    df = df.drop(columns=['Open Time', 'Close Time', 'Quote Asset Volume',
                          'Taker Buy Base Asset Volume', 'Taker Buy Quote Asset Volume', 'Ignore'])
    df['Symbol'] = symbol[:-4]
    return df

def fetch_and_save_all_time_data(symbols):
    """Fetch and save all-time data for a list of symbols."""
    all_dataframes = []
    for symbol in symbols:
        df = fetch_historical_data(symbol=symbol)
        if df is not None:
            all_dataframes.append(df)

    if all_dataframes:
        combined_df = pd.concat(all_dataframes)
        combined_df.to_csv(CSV_FILE_PATH, index=False)
        print(f"Data saved to {CSV_FILE_PATH}")
    else:
        print("No data available to save.")

def load_all_time_data_from_csv():
    """Load all-time data from a CSV file."""
    if os.path.exists(CSV_FILE_PATH):
        df = pd.read_csv(CSV_FILE_PATH)
        df['Date'] = pd.to_datetime(df['Date'])
        return df
    else:
        print(f"{CSV_FILE_PATH} does not exist.")
        return None

def fetch_current_price(symbol):
    """Fetch the current price for a given symbol from Binance API."""
    url = BINANCE_API_URL_CURRENT_PRICE + symbol
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return float(data.get('price', 0))
    else:
        print(f"Error fetching current price for {symbol}: {response.status_code}")
        return None

def add_moving_averages(df):
    """Add Simple and Exponential Moving Averages to the DataFrame."""
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['SMA_200'] = df['Close'].rolling(window=200).mean()
    df['EMA_50'] = df['Close'].ewm(span=50, adjust=False).mean()
    df['EMA_200'] = df['Close'].ewm(span=200, adjust=False).mean()
    return df

def calculate_interval_data(df, interval):
    """Calculate high, low, close, and moving averages for a given interval."""
    start, end = intervals[interval]
    df_interval = df.copy()

    if start:
        df_interval = df_interval[df_interval['Date'] >= datetime.fromtimestamp(start / 1000)]
    if end:
        df_interval = df_interval[df_interval['Date'] <= datetime.fromtimestamp(end / 1000)]

    if df_interval.empty:
        return {}

    df_interval = add_moving_averages(df_interval)
    high = df_interval['High'].max()
    low = df_interval['Low'].min()
    close = df_interval['Close'].iloc[-1]

    return {
        'High': high,
        'Low': low,
        'Close': close,
        'SMA_50': df_interval['SMA_50'].iloc[-1],
        'SMA_200': df_interval['SMA_200'].iloc[-1],
        'EMA_50': df_interval['EMA_50'].iloc[-1],
        'EMA_200': df_interval['EMA_200'].iloc[-1]
    }

def convert_color(color_name, opacity=0.8):
    """Convert a color name to rgba format."""
    rgba = mcolors.to_rgba(color_name, opacity)
    return f'rgba({int(rgba[0]*255)}, {int(rgba[1]*255)}, {int(rgba[2]*255)}, {rgba[3]})'

# Colors
colors_a = {
    'BTC': 'orange',
    'ETH': 'mediumpurple',
    'BNB': 'indianred'
}

colors_b = {
    'BTC': 'gold',
    'ETH': 'plum',
    'BNB': 'lightsalmon'
}

# Intervals
intervals = {
    'All_Time': [None, None],
    '5Y': [int((datetime.now() - timedelta(days=5*365)).timestamp() * 1000), None],
    '1Y': [int((datetime.now() - timedelta(days=365)).timestamp() * 1000), None],
    '6M': [int((datetime.now() - timedelta(days=180)).timestamp() * 1000), None],
    '3M': [int((datetime.now() - timedelta(days=90)).timestamp() * 1000), None],
    '1M': [int((datetime.now() - timedelta(days=30)).timestamp() * 1000), None],
    '2W': [int((datetime.now() - timedelta(days=14)).timestamp() * 1000), None],
    '1W': [int((datetime.now() - timedelta(days=7)).timestamp() * 1000), None],
}

# Main Execution Flow

def main():
    symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT']
    fetch_and_save_all_time_data(symbols)

    combined_df = load_all_time_data_from_csv()

    if combined_df is not None:
        ath_dict = {}
        current_price_dict = {}
        percent_change_ath_dict = {}
        price_by_interval_dict = {symbol[:-4]: {} for symbol in symbols}

        for symbol in symbols:
            symbol_name = symbol[:-4]
            df_symbol = combined_df[combined_df['Symbol'] == symbol_name]

            ath = df_symbol['High'].max()
            ath_dict[symbol_name] = ath

            current_price = fetch_current_price(symbol)
            current_price_dict[symbol_name] = current_price

            if current_price is not None:
                percent_change_ath_dict[symbol_name] = round(((current_price - ath) / ath) * 100, 2)
            else:
                percent_change_ath_dict[symbol_name] = None

            for interval_name in intervals.keys():
                interval_data = calculate_interval_data(df_symbol, interval_name)
                price_by_interval_dict[symbol_name][interval_name] = interval_data

        # Visualizations
        plot_current_vs_ath(symbols, ath_dict, current_price_dict, colors_a, colors_b)
        plot_price_curves(symbols, combined_df, colors_a, colors_b)

# Current Price vs. All-Time-High for All Symbols

def plot_current_vs_ath(symbols, ath_dict, current_price_dict, colors_a, colors_b):
    """Plot the current price vs All-Time High."""
    fig = go.Figure()

    for symbol in symbols:
        symbol_name = symbol[:-4]

        fig.add_trace(go.Bar(
            name=f'{symbol_name} All-Time-High: $ {ath_dict[symbol_name]:.2f}', # show Price in Legend
            y=[symbol_name],
            x=[ath_dict[symbol_name]],
            marker_color=convert_color(colors_b[symbol_name], 0.6),
            orientation='h',
            hovertemplate=f'{symbol_name}<br>All-Time-High: $ %{{x:.2f}}<extra></extra>'
        ))

        fig.add_trace(go.Bar(
            name=f'{symbol_name} Current Price: $ {current_price_dict[symbol_name]:.2f}',
            y=[symbol_name],
            x=[current_price_dict[symbol_name]],
            marker_color=convert_color(colors_a[symbol_name], 0.8),
            orientation='h',
            hovertemplate=f'{symbol_name}<br>Latest Price: $ %{{x:.2f}}<extra></extra>'
        ))

    fig.update_layout(
        title_text="Cryptocurrency Market Overview: Current Price vs. All-Time High",
        xaxis_title="Price (USD)",
        barmode='overlay',
        xaxis_type='log',
        template='plotly_white'
    )

    fig.show()

def plot_price_curves(symbols, df, colors_a, colors_b):
    """Plot the price curves over time for the given symbols."""
    fig = go.Figure()

    for symbol in symbols:
        symbol_name = symbol[:-4]
        df_symbol = df[df['Symbol'] == symbol_name]

        fig.add_trace(go.Scatter(
            x=df_symbol['Date'],
            y=df_symbol['Close'],
            mode='lines',
            name=f'{symbol_name} Close',
            line=dict(color=convert_color(colors_a[symbol_name], 0.8)),
            fill='tozeroy',
            fillcolor=convert_color(colors_b[symbol_name], 0.6),
            hovertemplate=f'{symbol_name}<br>Date: %{{x}}<br>Close: $ %{{y:.2f}}<extra></extra>'
        ))

    fig.update_layout(
        title_text="Cryptocurrency Price Over Time",
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        yaxis_type="log",
        xaxis_rangeslider_visible=True,
        template='plotly_white'
    )

    fig.show()

if __name__ == "__main__":
    main()