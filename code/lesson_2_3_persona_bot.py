"""
Lesson 2.3: Persona Bot with Real Facts

Demonstrates grounding LLMs with deterministic, verified business facts
stored in Python dictionaries to prevent hallucinations. Includes runtime
persona switching, local dictionary lookup bypasses, and conversational memory.
"""

from langchain.chat_models import init_chat_model

# 1. Centralized configuration dictionary
# Decoupling runtime hyperparameters into a config dictionary enables easy environment tuning without altering core logic.
config = {
    "model": "llama3.2",
    "temperature": 0.2,
    "max_history": 8,
    "default_persona": "friendly"
}

# 2. Ground-truth business facts
# Grounding the model with verified dictionaries prevents the AI from inventing non-existent items or hallucinatory pricing.
facts = {
    "business_name": "Sweet Crumbs Bakery",
    "location": "Main Boulevard, Gulberg, Lahore",
    "timings": "9 am to 10 pm daily",
    "delivery": "Free delivery across Lahore on orders over 1,500 PKR",
    "contact": "WhatsApp 0300-1234567",
    "prices": {
        "cupcake": 250,
        "brownie": 300,
        "chocolate cake": 1500,
        "donut": 200,
    }
}

# 3. Persona definitions
personas = {
    "friendly": "warm and cheerful, uses simple words and friendly emojis",
    "formal": "professional, courteous, concise, and business-like",
    "sales": "excited, persuasive, and always suggests one extra complementary item to buy"
}

current_style = personas[config["default_persona"]]

def build_system_message(persona_description: str) -> str:
    """Builds an instruction-tuned system message injecting verified facts and persona constraints."""
    price_catalog = ", ".join([f"{item.title()}: {price} PKR" for item, price in facts["prices"].items()])
    return (
        f"You are the customer assistant for {facts['business_name']} in {facts['location']}. "
        f"Timings: {facts['timings']}. Delivery: {facts['delivery']}. Contact: {facts['contact']}. "
        f"Official Menu & Prices: {price_catalog}. "
        f"Persona Style: {persona_description}. "
        "STRICT GROUNDING INSTRUCTION: Only answer using the exact facts provided above. "
        "If a customer inquires about an item, flavor, or service NOT listed in the menu, "
        "politely state that it is not available. Never invent or guess prices. "
        "Keep responses within 2 short lines."
    )

# 4. Initialize LLM and conversation memory
llm = init_chat_model(config["model"], model_provider="ollama", temperature=config["temperature"])

messages = [
    {"role": "system", 
     "content": build_system_message(current_style)}
]

print("Bot ready. Commands: /persona friendly|formal|sales, /price <item>, /add <item> <price>, bye")

# 5. Interactive conversational loop
while True:
    raw_input = input("You: ").strip()

    if not raw_input:
        continue

    # Command: Exit
    if raw_input.lower() == "bye":
        print("Bot: Goodbye!")
        break

    # Command: Switch Persona
    # Using .get() with a default fallback guarantees the application will never crash on an invalid user persona key.
    if raw_input.lower().startswith("/persona"):
        parts = raw_input.split(maxsplit=1)
        requested = parts[1].strip().lower() if len(parts) > 1 else config["default_persona"]
        current_style = personas.get(requested, personas[config["default_persona"]])
        messages[0]["content"] = build_system_message(current_style)
        print(f"Bot: Style changed to: {current_style}")
        continue

    # Command: Exact Price Lookup
    # Bypassing the LLM for exact price checks saves API tokens and guarantees 100% mathematical accuracy.
    if raw_input.lower().startswith("/price"):
        parts = raw_input.split(maxsplit=1)
        item_query = parts[1].strip().lower() if len(parts) > 1 else ""
        if item_query in facts["prices"]:
            print(f"Bot: {item_query.title()} costs {facts['prices'][item_query]} PKR.")
        else:
            print(f"Bot: Sorry, {item_query} is not on our menu.")
        continue

    # Stretch Goal: Dynamic Menu Insertion
    if raw_input.lower().startswith("/add"):
        parts = raw_input.split()
        if len(parts) >= 3 and parts[-1].isdigit():
            new_item = " ".join(parts[1:-1]).strip().lower()
            new_price = int(parts[-1])
            facts["prices"][new_item] = new_price
            messages[0]["content"] = build_system_message(current_style)
            print(f"Bot: Added {new_item.title()} ({new_price} PKR) to menu and updated system prompt.")
        else:
            print("Bot: Usage: /add <item name> <price in PKR>")
        continue

    # 6. Normal LLM conversational turn
    messages.append({"role": "user", "content": raw_input})

    # Sliding-window memory pruning
    if len(messages) > config["max_history"] + 1:
        messages = [messages[0]] + messages[1:][-config["max_history"]:]

    response = llm.invoke(messages)
    assistant_reply = response.content
    print(f"Bot: {assistant_reply}")

    messages.append({"role": "assistant", "content": assistant_reply})
