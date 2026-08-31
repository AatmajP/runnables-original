from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain.tools import tool 
from langchain_core.messages import HumanMessage
#from rich import print 

#1 Creating a tool

@tool
def text_length_tool(text:str) -> int:
    """
    Returns the number of character in a given text"""
    return len(text)

#this tool dont have any model
tools = {
    "text_length_tool" : text_length_tool
}
llm = ChatMistralAI(model = "mistral-small-2603")

#tool binding 

#this binds the tool to the llm, allowing the llm to use the 
# tool when generating responses.
llm_with_tool = llm.bind_tools([text_length_tool])
