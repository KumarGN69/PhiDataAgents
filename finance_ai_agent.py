import openai
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.model.ollama import Ollama
from phi.tools.yfinance import YFinanceTools
from langchain_ollama import OllamaLLM, ChatOllama
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

llm = Ollama(
        id="llama3.2",
        name='Ollama',
        host= 'http://localhost:11434',
        model="llama3.2",
        # format="json",
        temperature=0.0
        )
# Initialize the agent
finance_agent = Agent(
    name="Finance AI Agent",
    # model=OpenAIChat(id="gpt-4o"),
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
finance_agent.print_response("Share the TSLA stock price and analyst recommendations", stream=True)