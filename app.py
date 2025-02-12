import streamlit as st
from show_agent_demo_base import get_calculation_response

st.set_page_config(page_title="LLM Agent for Algebra Matrix", layout="centered")
st.title("Calculate and Code")
st.write("This is a simple calci that uses the ReAct agent to perform calculations step by step.")


a = st.number_input("Enter the nemo (a):", min_value=-1000, max_value=1000, value=40, step=1)
b = st.number_input("Enter the demo (b):", min_value=-1000, max_value=1000, value=8, step=1)

if st.button("Calculate the Matrix"):
    response = get_calculation_response(a, b)
    
    st.subheader("Calculation Steps:")
    st.write(response)
    
