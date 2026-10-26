"""
Lesson 2.2: Personal Tutor with Memory

Demonstrates building stateful, multi-turn AI interactions by managing
a conversation history list in Python. Implements dynamic sliding-window
memory management, conversation reset controls, and token monitoring.
"""

from langchain.chat_models import init_chat_model

# 1. Initialize the LLM once before entering the chat loop
# Initializing outside the loop prevents costly model reloads on every user query.
llm = init_chat_model("llama3.2", model_provider="ollama", temperature=0.3)

# 2. System prompt and conversation memory
# The system message is placed at index 0 as a persistent anchor that defines the AI's identity across all turns.
SYSTEM_PROMPT = "You are a friendly personal tutor. Answer in 1 to 2 short lines."
messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

# Stretch goal tracking: store user questions
questions = []

print("Tutor: Ask me anything. Commands: /reset, /count, bye")

# 3. Interactive conversational loop
while True:
    raw_input = input("You: ").strip()

    if not raw_input:
        continue

    # Command: Exit
    if raw_input.lower() == "bye":
        print("Tutor: Goodbye!")
        # Stretch goal summary: report user question statistics
        if questions:
            print(f"\nSession Summary: You asked {len(questions)} question(s).")
            print(f"First question: '{questions[0]}'")
            print(f"Last question: '{questions[-1]}'")
        break

    # Command: Reset conversation memory
    # We slice [messages[0]] to wipe user/assistant dialogue while preserving the foundational system instructions.
    if raw_input.lower() == "/reset":
        messages = [messages[0]]
        print("Tutor: Memory cleared.")
        continue

    # Command: Count memory length
    # Auditing message length helps developers verify that sliding-window memory pruning is working as intended.
    if raw_input.lower() == "/count":
        print(f"Tutor: {len(messages)} messages in memory.")
        continue

    # Normal turn: Record user input
    messages.append({"role": "user", "content": raw_input})
    questions.append(raw_input)

    # 4. Sliding-window memory trimming
    # Keeping only the system message plus the last 8 turns prevents quadratic context growth and stays within token budgets.
    if len(messages) > 9:
        messages = [messages[0]] + messages[1:][-8:]

    # 5. Invoke model with full conversation history
    response = llm.invoke(messages)
    assistant_reply = response.content
    print(f"Tutor: {assistant_reply}")

    # Appending the AI's response is essential so the model can refer back to its own answers in subsequent turns.
    messages.append({"role": "assistant", "content": assistant_reply})

    # 6. Token telemetry
    tokens_sent = response.usage_metadata.get("input_tokens", 0)
    print(f"       (tokens sent: {tokens_sent})")
