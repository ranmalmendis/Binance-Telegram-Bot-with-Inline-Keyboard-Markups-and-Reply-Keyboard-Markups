import logging
import io
from binance import Client
import datetime
from matplotlib import pyplot as plt
import pandas as pd
import cred

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)


def get_historical_klines(coin):
    """Echo the user message."""

    # OUR KEYS
    api_key = cred.api_key
    api_secret = cred.api_secret
    client = Client(api_key, api_secret)
    res = []

    # TWO FUNCTIONS TO MANAGE THE DATE
    def unix_to_datetime(unix_time):
        return datetime.datetime.fromtimestamp(unix_time / 1000.0)

    def date_to_unix(date):
        date = datetime.datetime.now()
        date = date.replace(hour=0, minute=0, second=0, microsecond=0)
        date = date - datetime.timedelta(days=7)
        return int(date.timestamp() * 1000)

    # We'll be getting the data related to BTCUSDT here.
    crypto = coin

    # To get the historical data in 5 min intervals
    klines = client.get_historical_klines(crypto, Client.KLINE_INTERVAL_30MINUTE, date_to_unix(datetime.datetime.now()))

    values = [[unix_to_datetime(el[0]), float(el[1])] for el in klines]
    df = pd.DataFrame(values, columns=['ds', 'y'])
    # plot the data and sending as an image via telegram
    plt.plot(df['ds'], df['y'])
    plt.xticks(rotation=15)
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    res.append(img)

    df = pd.DataFrame(klines)
    df["Date"] = pd.to_datetime(df.iloc[:, 0], unit="ms")
    df.columns = ["Open Time", "Open", "High", "Low", "Close", "Volume",
                  "Clos Time", "Quote Asset Volume", "Number of Trades",
                  "Taker Buy Base Asset Volume", "Taker Buy Quote Asset Volume", "Ignore", "Date"]
    df = df[["Date", "Open", "High", "Low", "Close", "Volume"]].copy()
    df.set_index("Date", inplace=True)
    for column in df.columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # calculating the changed percentage of a given symbol
    change = ((df['Close'] - df['Open']) / df['Open'])
    change = round(change.sum() * 100, 2)
    res.append(change)
    return res
