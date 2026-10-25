"""
Lesson 1.5: AI Model Profile Card

A client-facing estimation script that presents model specifications
using Python's 4 primitive types (str, int, float, bool) and calculates
per-chat and monthly operational costs based on expected token volume.
"""

# We store explicit primitive types so the client can audit hardware fit (context window) and data privacy (local vs cloud).
model_name = "llama3.2"
context_window = 128000
price_per_1k_tokens = 0.50
runs_locally = True

print("--- AI Model Profile Card ---")
print(f"Model: {model_name} {type(model_name)}")
print(f"Context window: {context_window} tokens {type(context_window)}")
print(f"Price per 1K tokens: {price_per_1k_tokens} PKR {type(price_per_1k_tokens)}")
print(f"Runs locally: {runs_locally} {type(runs_locally)}")

tokens_per_chat = int(input("\nTokens per chat: "))

# Normalizing by 1,000 matches token provider pricing models, while rounding to 2 decimals prevents floating-point inaccuracies in client invoices.
cost_per_chat = round((tokens_per_chat / 1000) * price_per_1k_tokens, 2)
print(f"Estimated cost: {cost_per_chat} PKR")

# We project monthly costs over 30 days to provide the client with a clear predictable operational budget.
chats_per_day = int(input("Chats per day: "))
monthly_cost = round(cost_per_chat * chats_per_day * 30, 2)
print(f"Estimated monthly cost (30 days): {monthly_cost} PKR")
