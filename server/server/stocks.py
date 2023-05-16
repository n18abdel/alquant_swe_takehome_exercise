from datetime import datetime, timedelta

import pandas as pd
import yfinance as yf

DEFAULT_SYMBOLS = ["AAPL", "MSFT", "TSLA"]
DEFAULT_START = "2022-05-08"

NUM_PERIODS_PER_YEAR = 252


def fetch_stock_data(symbols, start):
    yesterday = datetime.today() - timedelta(days=1)
    df = yf.download(symbols, start=start, end=yesterday).loc[:, "Close"]
    return df


def performance(symbols=DEFAULT_SYMBOLS, start=DEFAULT_START):
    df = fetch_stock_data(symbols, start)
    df.index = df.index.strftime("%Y-%m-%d")
    normalized_df = (df / df.iloc[0]) * 100
    stocks = {col: normalized_df.loc[:, col].to_list() for col in normalized_df}
    return {"timestamps": normalized_df.index.to_list(), "stocks": stocks}


def statistics(symbols=DEFAULT_SYMBOLS, start=DEFAULT_START):
    df = fetch_stock_data(symbols, start)
    cumulative_return = (df.iloc[-1] / df.iloc[0]) - 1

    number_of_days = df.shape[0]
    number_of_years = number_of_days / NUM_PERIODS_PER_YEAR
    annualized_return = (df.iloc[-1] / df.iloc[0]) ** (1 / number_of_years) - 1

    returns = df.pct_change()
    volatility = returns.std()
    annualized_volatility = volatility * (NUM_PERIODS_PER_YEAR**0.5)
    return (
        pd.concat(
            (cumulative_return, annualized_return, annualized_volatility),
            axis=1,
            keys=["cumulative_return", "annualized_return", "annualized_volatility"],
        )
        .round(4)
        .to_dict("index")
    )
