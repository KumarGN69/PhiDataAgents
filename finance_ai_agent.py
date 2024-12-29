from dotenv import load_dotenv
import os
import openai
from phi.agent import Agent
from phi.model.ollama import Ollama
from phi.tools.yfinance import YFinanceTools

# Load environment variables from .env file
load_dotenv()

# intantiate the Ollama object using phiData Ollama integration
llm = Ollama(
        id="llama3.2",
        name='Ollama',
        host= 'http://localhost:11434',
        model="mistral",
        # format="json",
        temperature=0.0
        )

# Initialize the agent
finance_agent = Agent(
    name="Finance AI Agent",
    model = llm,
    tools=[
        YFinanceTools(
            stock_price=False,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
            historical_prices=True
        )
    ],
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
    show_tool_calls=True,
    markdown=False,
)
finance_agent.print_response("Share the NVDA stock price and analyst recommendations", stream=True)