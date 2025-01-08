# Multi-Agent-Stock-Market-Analysis-and-Financial-Insights
This project demonstrates the implementation of a multi-agent system designed to analyze stock market trends, provide financial insights, and perform web-based data retrieval. Each agent in the system is tailored for specific roles, leveraging tools and APIs to deliver accurate and actionable outputs.
Features
Stock Analysis Agent:

Fetches real-time stock data.
Analyzes sentiment from news articles using DuckDuckGo search.
Provides buy/sell recommendations based on market trends and sentiment analysis.
Web Search Agent:

Performs web searches to gather relevant information.
Ensures responses are sourced and backed by reliable data.
Finance AI Agent:

Retrieves detailed stock information, including fundamentals, analyst recommendations, and historical data.
Displays results in tabular format for clear and concise insights.
Technology Stack
Python: Core language for development.
Phi Library: For building intelligent agents and integrating tools.
Groq Model: A powerful language model for generating context-aware responses.
YFinance Tools: Fetching financial data and insights.
DuckDuckGo Search API: To gather web-based information.
FastAPI: Backend for serving the multi-agent system as a web application.
AnyIO and Starlette: For asynchronous task handling and web server operations.
