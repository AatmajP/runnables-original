from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#ParallelRunnable is a class that allows you to run multiple runnables in 
#parallel. It takes a list of runnables as input and runs them in parallel,
#returning a dictionary of the results.

#LambdaRunnable is a class that allows you to create a runnable from a
#lambda function. It takes a lambda function as input and returns a runnable
from langchain_core.runnables import ParallelRunnable, LambdaRunnable