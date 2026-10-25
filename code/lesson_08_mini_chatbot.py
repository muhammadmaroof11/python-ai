"""
Lesson 1.8: Business Helper Bot (Module 1 Final - Sample)

An interactive rule-based customer support assistant for 'City Care Clinic'.
Demonstrates stateful conversational loops (while True), memory preservation,
priority intent routing (complaints first), defensive keyword matching,
and AI fallback telemetry to prepare for LLM integration in Module 2.
"""

BOT_NAME = "City Care Bot"
BUSINESS_NAME = "City Care Clinic"

print(f"{BOT_NAME}: Hi! Ask about timings, fees, location, or appointments. Type 'bye' to exit.")

# 1. Conversation Memory: Storing context before entering the loop
# We capture the customer's name once before starting the loop so the bot maintains personalized state without asking repeatedly.
raw_name = input(f"{BOT_NAME}: What is your name? ").strip().title()
user_name = raw_name if raw_name else "Valued Patient"
print(f"{BOT_NAME}: Nice to meet you, {user_name}!")

# Conversation metrics & analytics
message_count = 0
unanswered_count = 0
complaint_count = 0

# 2. Main Chatbot Loop
while True:
    raw_message = input(f"{user_name}: ")
    message = raw_message.strip().lower()
    
    # Ignore accidental empty submits
    if not message:
        print(f"{BOT_NAME}: Please type a question or type 'bye' to leave.")
        continue

    message_count += 1

    # Exit Intent
    if message == "bye" or message == "exit":
        print(f"{BOT_NAME}: Take care, {user_name}! Wishing you good health.")
        break

    # Stretch Goal: Immediate Human Handover Trigger
    if "agent" in message or "human" in message:
        print(f"{BOT_NAME}: Connecting you to a human support agent right away. Please hold...")
        break

    # 3. Priority Triage: Complaints & Escalations
    # High-priority rules come first so frustrated customers are immediately acknowledged, preventing order/pricing rules from intercepting complaints (e.g. 'late appointment').
    if "refund" in message or "complaint" in message or "late" in message or "bad" in message:
        complaint_count += 1
        print(f"{BOT_NAME}: Sorry about that. The clinic manager will call you today to resolve this.")

    # 4. Standard FAQ Intents
    elif "timing" in message or "hour" in message or "open" in message or "time" in message:
        print(f"{BOT_NAME}: We are open 10 am to 8 pm, Monday to Saturday.")

    elif "fee" in message or "cost" in message or "price" in message or "how much" in message:
        print(f"{BOT_NAME}: General consultation fee is 2,000 PKR. Specialist consultations start at 3,500 PKR.")

    elif "where" in message or "location" in message or "address" in message:
        print(f"{BOT_NAME}: We are located at 45 Medical Complex, Jail Road, Lahore.")

    elif "appointment" in message or "book" in message or "doctor" in message and "book" in message:
        print(f"{BOT_NAME}: To book an appointment, call (042) 3578-9000 or reply with your preferred day.")

    # 5. Defensive Keyword Matching for Short Greetings
    # Exact equality (==) or startswith prevents false-positive collisions where substring 'hi' mistakenly triggers inside words like 'which' or 'this'.
    elif message in ("hi", "hello", "hey") or message.startswith("salam"):
        print(f"{BOT_NAME}: Hello again, {user_name}! How can I help you today?")

    # 6. Fallback & Telemetry for Future LLM Routing
    # Tracking unanswered queries identifies coverage gaps in our static rules and crafts the prompt template ready for Module 2 LLM routing.
    else:
        unanswered_count += 1
        llm_prompt = f"You are the friendly assistant of {BUSINESS_NAME}. Answer in 2 lines: {raw_message}"
        print(f"{BOT_NAME}: I am not sure yet. In Module 2, an AI will answer:")
        print(f"  Prompt -> \"{llm_prompt}\"")

# 7. Post-Chat Analytical Summary
print("=" * 40)
print(f"Chat summary: {message_count} messages, {unanswered_count} unanswered, {complaint_count} complaints.")
