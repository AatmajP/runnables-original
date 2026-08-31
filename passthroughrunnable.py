from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#RunnablePassthrough is a class that allows you to create a runnable that 
# simply passes through the input to the output. It takes no input and 
# returns the input as output.
#the RunnablePassthrough class is useful for testing and debugging, as it 
#allows you to see the input and output of a runnable without any modifications.
 
from langchain_core.runnables import RunnableParallel,RunnablePassthrough