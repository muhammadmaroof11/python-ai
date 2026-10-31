"""
Lesson 2.4: Batch Product Writer

Demonstrates automating batch content generation using Python loops and LLMs.
Iterates over a product catalog, defensibly skips unpriced items using `continue`,
aggregates generated copy into structured dictionary collections, and computes
cumulative token expenditures and processing latency.
"""

from langchain.chat_models import init_chat_model

# 1. Product catalog dictionary
# Centralizing catalog data in key-value pairs allows clean separation between raw pricing data and dynamic marketing copy.
products = {
    "Chocolate Cake": 1500,
    "Cupcake": 250,
    "Old Stock Sampler": 0,  # Zero-price test case for defensive filtering
    "Brownie": 300,
    "Glazed Donut": 200,
}

# 2. Initialize LLM once before the loop
# Creating the client outside the loop prevents redundant connection handshakes and GPU model reload overhead on every item.
llm = init_chat_model("llama3.2", model_provider="ollama", temperature=0.7)

# 3. Accumulators and result collection
# Initializing accumulators before iteration is required to track aggregate operational costs across batch workloads.
menu_items = []
total_tokens = 0
total_seconds = 0.0

# 4. Batch generation loop
for name, price in products.items():
    # Defensive guardrail: Skip unpriced or discontinued inventory to avoid wasting API token budget
    if price == 0:
        print(f"Skipping {name} (no price)")
        continue

    prompt = (
        f"Write exactly one enticing, mouth-watering marketing sentence describing {name} "
        f"available for {price} PKR at Sweet Crumbs bakery in Lahore. Keep it under 20 words."
    )

    response = llm.invoke(prompt)
    clean_description = response.content.strip().replace("\n", " ")

    # Structuring outputs as a list of dictionaries mirrors production JSON schemas ready for databases or web frontends.
    menu_items.append({
        "item": name,
        "price": price,
        "text": clean_description
    })

    # Accumulate token metrics and elapsed duration
    tokens = response.usage_metadata.get("total_tokens", 0)
    duration_ns = response.response_metadata.get("total_duration", 0)
    
    total_tokens += tokens
    total_seconds += duration_ns / 1_000_000_000

# 5. Display the formatted menu and batch analytics
print("=" * 50)
for index, entry in enumerate(menu_items, start=1):
    print(f"{index}. {entry['item']} ({entry['price']} PKR)")
    print(f"   {entry['text']}")
print("=" * 50)
print(f"{len(menu_items)} descriptions, {total_tokens} tokens, {total_seconds:.1f} seconds")
