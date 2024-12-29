from phi.tools.yfinance import YFinanceTools
from yfinance import Ticker
import json

def getnews(symbol:str):
    """
    :param symbol:
    :return:
    """
    ticker = YFinanceTools(
        stock_price=False,
        analyst_recommendations=True,
        company_info=True,
        company_news=True,
        historical_prices=True
    )
    # ticker = Ticker(ticker=symbol)
    return json.dumps(ticker.get_income_statements(symbol=symbol))
    # return ticker.get_income_statements(symbol=symbol)
    # return json.dumps(ticker.income_stmt())
# print(getnews("NVDA"))
