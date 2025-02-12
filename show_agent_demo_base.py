from dotenv import load_dotenv
load_dotenv()
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool

def fce(a: float, b: float) -> float:
    return a*b

def ad(a: float, b:float) -> float:
    return a+b

multiply_tool = FunctionTool.from_defaults(fn=fce)
add_tool = FunctionTool.from_defaults(fn=ad)

llm = OpenAI(model="gpt-3.5-turbo", temperature=0)
agent = ReActAgent.from_tools([multiply_tool, add_tool], llm=llm, verbose=True)

def get_calculation_response(a: float, b: float):
    query = f"What is {a} + ({b} * 8)? Use a tool to calculate every step."
    response = agent.chat(query)
    return response