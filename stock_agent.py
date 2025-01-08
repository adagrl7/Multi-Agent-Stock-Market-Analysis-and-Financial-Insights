from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Define stock analysis agent
stock_analysis_agent = Agent(
    name="Stock Analysis Agent",
    role="Analyze stock market data and news sentiment to provide buy/sell advice.",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(),
        DuckDuckGo()
    ],
    instructions=[
        "Fetch stock data for the given ticker.",
        "Analyze the sentiment of current news articles related to the ticker.",
        "Provide buy or sell advice based on stock trends and sentiment.",
        "Always include sources and justify recommendations."
    ],
    show_tools_calls=True,
    markdown=True,
)

# Define input parameters
def analyze_stock(ticker):
    prompt = f"""
    Analyze the stock performance for {ticker}. 
    1. Fetch real-time stock data and calculate key indicators (RSI, MACD, etc.). 
    2. Search for recent news related to {ticker} and perform sentiment analysis.
    3. Provide buy/sell recommendations based on combined insights.
    """
    response = stock_analysis_agent.print_response(prompt, stream=False)
    print(response)

# Test the function
analyze_stock("AAPL")