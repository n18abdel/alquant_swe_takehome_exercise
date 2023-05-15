import yfinance as yf


def performance(symbols=["AAPL", "MSFT", "TSLA"], start="2023-05-08"):
    df = yf.download(symbols, start=start).loc[:, "Close"]
    df.index = df.index.strftime("%Y-%m-%d")
    normalized_df = (df / df.iloc[0]) * 100
    stocks = {col: normalized_df.loc[:, col].to_list() for col in normalized_df}
    return {"timestamps": normalized_df.index.to_list(), "stocks": stocks}


def statistics():
    return {}
