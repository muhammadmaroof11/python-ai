
from langchain.chat_models import init_chat_model

MODEL_NAME = "llama3.2"

llm = init_chat_model(
    model=MODEL_NAME,
    model_provider="ollama",
    temperature=0.3
)

print(f"Model '{MODEL_NAME}' is ready. Type 'exit' to quit.")

total_input_tokens = 0
total_output_tokens = 0
messages = []

while True:
    content = input("\nYour Turn: ")

    if content.strip().lower() == "exit":
        print(f"\nTotal input tokens: {total_input_tokens}")
        print(f"Total output tokens: {total_output_tokens}")
        print(f"Total processed tokens: "
              f"{total_input_tokens + total_output_tokens}")
        print("Exiting...")
        break

    # Store user message
    messages.append({
        "role": "user",
        "content": content
    })

    print("AI: ", end="", flush=True)

    response_chunks = []
    response_metadata = {}

    # Stream response and capture Ollama's usage metadata
    for chunk in llm.stream(messages):
        print(chunk.content, end="", flush=True)
        response_chunks.append(chunk.content)

        if chunk.response_metadata:
            response_metadata.update(chunk.response_metadata)

    print()

    # Combine chunks into the complete response
    full_response = "".join(response_chunks)

    # Store assistant response in conversation history
    messages.append({
        "role": "assistant",
        "content": full_response
    })

    # Read actual usage reported by Ollama
    input_tokens = response_metadata.get("prompt_eval_count")
    output_tokens = response_metadata.get("eval_count")

    if input_tokens is not None and output_tokens is not None:
        total_input_tokens += input_tokens
        total_output_tokens += output_tokens

        print(
            f"[Input tokens: {input_tokens} | "
            f"Output tokens: {output_tokens} | "
            f"Session total: "
            f"{total_input_tokens + total_output_tokens}]"
        )
    else:
        print("Token usage metadata unavailable for this response.")
        print("Metadata received:", response_metadata)
