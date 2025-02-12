# TheAgentShow

# Interactive MCalci with ReAct Agent (LLMIndex)

This project demonstrates the power of the **ReAct Agent** in performing step-by-step calculations using a **Large Language Model (LLM)**. The agent utilizes the LLMIndex library, which allows the use of custom tools and functions to solve complex problems interactively.

## Overview

The goal of this project is to create an interactive UI using **Streamlit** that leverages the ReAct Agent for performing calculations. Users can input two numbers, and the agent will calculate the result step-by-step, using custom tools for multiplication and addition.

## Features

- **Interactive UI**: Built with **Streamlit**, allowing users to input numbers and trigger calculations.
- **ReAct Agent**: Uses the ReAct Agent from **LLMIndex** to break down complex problems into smaller steps, applying specific functions like multiplication and addition.
- **Dynamic Calculation**: The agent calculates the result using a combination of predefined functions and LLM-driven reasoning.
- **Step-by-Step Calculation**: Each step of the calculation process is displayed to help users understand how the final result is derived.

## How it Works

This app uses the **ReAct Agent** from LLMIndex to interact with two tools:
1. **Multiplication Tool**: Multiplies two numbers.
2. **Addition Tool**: Adds two numbers together.

The user enters two numbers (a and b), and the agent breaks down the problem. For example, the agent will calculate `a + (b * 8)` step by step, using the multiplication tool and addition tool.

## Prerequisites

Before running the app, you need to set up the following:

1. **Python 3.8+**
2. **Streamlit** for creating the UI.
3. **LLMIndex** and other dependencies:
   - `llama_index`
   - `openai`
   - `python-dotenv` for managing environment variables.

### Installing the Required Libraries

You can install all the dependencies by running:

```bash
pip install streamlit llama_index openai python-dotenv
