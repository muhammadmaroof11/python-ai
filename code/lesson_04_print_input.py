"""
Lesson 1.4: Business Prompt Builder (Sample)

A lightweight interactive tool designed for agencies to capture core business
context from a client and immediately synthesize a targeted prompt ready for
any Large Language Model (e.g., Llama 3.2, Claude, or ChatGPT).
"""

# We capture specific pain points directly from the stakeholder so the resulting prompt avoids generic AI advice.
user_name = input("Your name: ")
business_type = input("Business type: ")
business_problem = input("Biggest problem: ")
business_budget= int(input("Budget: "))

print(f"\nWelcome, {user_name}!")
print("--- Your AI Prompt ---")

# Decoupling raw input variables into an f-string template ensures the prompt is modular and easily plugged into LangChain or Ollama later.
prompt = f"Suggest 3 AI solutions for a {business_type} that struggles with {business_problem} considering the {business_budget} PKR per month as the budget constraint."
print(prompt)
