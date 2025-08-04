import os
from dotenv import load_dotenv
from langchain_together import ChatTogether

# Load environment variable
load_dotenv()

# Initialize the Together chat model

llm=ChatTogether(  
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
    temperature=0.7,
    max_tokens=None,
)
model =llm  # Start chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = model.invoke(user_input)
    print("Bot:", response.content)
