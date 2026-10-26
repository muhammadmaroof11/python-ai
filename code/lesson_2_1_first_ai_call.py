"""
Lesson 2.1: First AI Call (AI Tutor)

Demonstrates making a live, single-turn LLM call via LangChain and Ollama.
Takes a learning topic and skill level, constructs an instruction-tuned
system prompt, invokes the local model, and audits token consumption and latency.
"""

from langchain.chat_models import init_chat_model

# 1. Capture and sanitize user inputs
# Stripping whitespace prevents unintended newline or formatting artifacts in prompt payloads.
raw_topic = input("Topic: ").strip()
raw_level = input("Level (beginner or expert): ").strip().lower()

# Default to beginner if the user provides unexpected text
level = raw_level if raw_level in ("beginner", "expert") else "beginner"

# 2. Build the system prompt
# We define the system role and explicit length constraints to prevent verbose, rambling answers and reduce latency.
system_prompt = (
    f"You are a friendly, patient academic tutor. "
    f"Explain the topic clearly for a {level} student. "
    "Answer in exactly 3 short, easy-to-read sentences."
)

# 3. Initialize the model
# Temperature 0.2 keeps the explanation focused, factual, and deterministic rather than overly creative.
llm = init_chat_model("llama3.2", model_provider="ollama", temperature=0.2)

# 4. Invoke the model
response = llm.invoke([
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": raw_topic}
])

# 5. Telemetry & performance metrics
# Tracking token usage and inference duration is crucial for monitoring operational cost and latency.
total_tokens = response.usage_metadata.get("total_tokens", 0)
total_duration_ns = response.response_metadata.get("total_duration", 0)
seconds = total_duration_ns / 1_000_000_000

# 6. Display results
print("=" * 40)
print(response.text)
print("=" * 40)
print(f"{total_tokens} tokens in {seconds:.1f} seconds")
