"""
Lesson 1.6: Prompt Cleaner & Token Sanitizer (Sample)

Demonstrates real-world string sanitization techniques before inputs reach an LLM:
trimming whitespace, normalizing case, detecting keywords, estimating token overhead,
and enforcing strict character slice limits to prevent prompt injection or context overflow.
"""

# 1. Capture messy client inputs
raw_name = input("Your name: ")
raw_question = input("Your question: ")

# We sanitize whitespace and casing so the LLM receives predictable, clean tokens instead of wasting context on trailing spaces.
cleaned_name = raw_name.strip().title()
cleaned_question = raw_question.strip().capitalize()

# Optional stretch: Filter harmful or unprofessional words before prompt assembly
sanitized_question = cleaned_question.replace("stupid", "***")

# 2. Token and keyword estimation
# Rule of thumb: 1 token is roughly 4 characters in English; estimating this locally prevents expensive over-budget API calls.
char_count = len(sanitized_question)
estimated_tokens = round(char_count / 4)

# Normalizing to lowercase before substring search ensures case-insensitive keyword detection
mentions_python = "python" in sanitized_question.lower()

# 3. Print analysis report
print("=" * 40)
print(f"Cleaned question: {sanitized_question}")
print(f"Characters: {char_count}, about {estimated_tokens} tokens")
print(f"Mentions Python: {mentions_python}")

# Stretch: calculate estimated prompt cost formatted to 2 decimal places using :.2f
cost_pkr = (estimated_tokens / 1000) * 0.50
print(f"Estimated token cost: {cost_pkr:.2f} PKR")
print("=" * 40)

# 4. Construct safe multi-line prompt
# We slice [:150] as a defensive boundary against prompt injection or excessively long user inputs that inflate API costs.
tutor_prompt = f"""You are a friendly Python tutor.
Greet {cleaned_name} by name and answer in 3 short lines.
Question: {sanitized_question[:150]}"""

print(tutor_prompt)
