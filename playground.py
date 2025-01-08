from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv
import phi.api
import os
from phi.playground import Playground,serve_playground_app
load_dotenv()
phi.api=os.getenv("PHI_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")
# Define stock analysis agent
stock_analysis_agent = Agent(
    name="Stock Analysis Agent",
    role="Analyze stock market data and news sentiment to provide buy/sell advice.",
    model=Groq(id="mixtral-8x7b-32768"),
    tools=[
        YFinanceTools(),
        DuckDuckGo()
    ],
    instructions=["Analyze the stock performance."],
    show_tools_calls=True,
    markdown=True,
)

## web search agent
web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="mixtral-8x7b-32768"),
    tools=[DuckDuckGo()],
    instructions=["Alway include sources"],
    show_tools_calls=True,
    markdown=True,

)

## Financial agent
finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="mixtral-8x7b-32768"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,

)

app=Playground(agents=[stock_analysis_agent,finance_agent,web_search_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app",reload=True)