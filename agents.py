from dotenv import load_dotenv
load_dotenv()


#os is used to access environment variables and perform file system operations
import os
#requests is used to make HTTP requests
import requests
from langchain_mistralai import ChatMistralAI
from langchain.tools import tool 
from langchain_core.messages import HumanMessage
from tavily import TavilyClient