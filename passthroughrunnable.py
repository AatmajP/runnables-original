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

# Components
model = ChatMistralAI(model="mistral-small-2603")
parser = StrOutputParser()


code_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a code generator"),
    ("human", "{topic}")
])

explain_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant who explains code in simple terms"),
    ("human", "Explain the following code in simple words:\n{code}")
])


# Create a sequence of operations 
seq = code_prompt | model | parser

seq2 = RunnableParallel(
    {"code" :  RunnablePassthrough(),
     "explanation" : explain_prompt | model | parser
    }
)

chain = seq | seq2

result = chain.invoke({"topic" : "please write a code of palindrome in python "})

print(result['code'])
print(result['explanation'])