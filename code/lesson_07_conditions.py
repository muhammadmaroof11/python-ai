"""
Lesson 1.7: Smart Model Router (Sample)

Demonstrates conditional decision-making (if / elif / else) in AI engineering.
Routes client workloads based on privacy requirements, technical complexity,
and token limits to balance cost, security, and response quality.
"""

# 1. Capture and sanitize user inputs
# Normalizing case and whitespace ensures robust routing even if the user types ' Code ' or 'CHAT'.
raw_task = input("Task (code / private / chat): ")
task_type = raw_task.strip().lower()

tokens = int(input("Estimated tokens: "))

# Optional stretch: Check user subscription status
# Using logical operators (and) allows us to enforce tier-based rate limiting before dispatching queries.
user_tier = input("Is this a paid user? (yes/no): ").strip().lower()
is_paid = user_tier in ("yes", "y", "true")

if not is_paid and tokens > 2000:
    print("Upgrade to send long requests.")

# 2. Token length guardrail
# Checking token count before calling an API prevents unexpected cost spikes and avoids exceeding model context windows.
if tokens > 4000:
    print("Warning: long request, consider shortening it.")
else:
    print("Length is fine.")

# 3. Model routing logic
# We route sensitive enterprise data to a local LLM for zero cost and zero data leakage,
# heavy programming tasks to high-reasoning frontier models, and everyday chat to lightweight economical models.
if task_type == "private":
    model_name = "llama3.2 (local, Ollama)"
    price_per_1k = 0.0  # Local inference has zero API token fees
elif task_type == "code":
    model_name = "claude (cloud, strong at code)"
    price_per_1k = 0.80  # Example PKR rate per 1,000 tokens
elif task_type == "chat":
    model_name = "gpt-4o-mini (cloud, lightweight chat)"
    price_per_1k = 0.20
else:
    # Safe fallback for unrecognized task types
    model_name = "llama3.2 (local fallback)"
    price_per_1k = 0.0

# 4. Cost calculation and display
cost = (tokens / 1000) * price_per_1k

print(f"Chosen model: {model_name}")
print(f"Estimated cost: {cost:.2f} PKR")
