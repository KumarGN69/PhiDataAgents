from phi.tools.yfinance import YFinanceTools
import json

def getnews(symbol:str):
    """
    Function to get the latest information from yahoo finance portal
    :param symbol:str stock ticker

    :return: the json format of the information requested
    """
    ticker = YFinanceTools(
        stock_price=False,
        analyst_recommendations=True,
        company_info=True,
        company_news=True,
        historical_prices=True
    )
    return json.dumps(ticker.get_income_statements(symbol=symbol))
