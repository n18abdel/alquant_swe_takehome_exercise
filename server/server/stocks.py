import yfinance as yf


def performance(symbols=["AAPL", "MSFT", "TSLA"]):
    df = yf.download(symbols, start="2023-05-08").loc[:, "Close"]
    df.index = df.index.strftime("%Y-%m-%d")
    normalized_df = (df / df.iloc[0]) * 100
    return normalized_df.to_dict("index")


def statistics():
    return {}
