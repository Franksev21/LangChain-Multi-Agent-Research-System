from langchain_core.tools import Tool
import requests
from  dotenv import load_dotenv
import os
from tavily import TavilyClient
import re


load_dotenv()

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def web_search(query: str) -> str:
    """
    Perform a web search using the Tavily API.

    Args:
        query (str): The search query.

    Returns:
        str: The search results.
    """
    results = tavily_client.search(query, max_results=5)
    print(results)
