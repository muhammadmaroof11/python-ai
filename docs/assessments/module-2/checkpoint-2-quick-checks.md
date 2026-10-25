# Module 2, Checkpoint 2: Quick Checks (Lessons 2.5 to 2.8)

**Course:** Python for AI · **Module 2:** Core Python for Building LLM Apps · **Updated:** Oct 2026

> **Student version.** Answer on your own first, without AI tools or notes. The goal is to find what you have not understood yet, not to get full marks.

**Format per lesson:** 5 MCQs + 1 "Predict the Output" · **Time:** 5 minutes · **Marks:** 6 per lesson

**How to answer:** add your answers to `docs/my-answers-module-2.md` like this:

```text
2.5: Q1 ?, Q2 ?, Q3 ?, Q4 ?, Q5 ?, Q6 (your predicted output)
```

**Predict the Output rule:** write your answer **before** running the code. Then run it with `uv run` and check yourself.

---

## Lesson 2.5: Functions = Reusable AI Skills

**Q1.** What does a function give back if it has no `return` line?
- a) `0`
- b) An empty string
- c) `None`
- d) An error

**Q2.** Why does `def build(task="Explain", audience):` fail?
- a) Functions cannot have two parameters
- b) A parameter without a default cannot come after one with a default
- c) `task` is a reserved word
- d) Defaults must be numbers

**Q3.** You run `print(summarize)` and see `<function summarize at 0x10a3...>`. What went wrong?
- a) The AI is offline
- b) You forgot the brackets and the text: it should be `summarize(text)`
- c) The function has no docstring
- d) `summarize` must return a number

**Q4.** `def build_prompt(task, audience="beginners", lines=3)`. Which call gives "... for beginners in 2 lines."?
- a) `build_prompt("Explain loops", 2)`
- b) `build_prompt("Explain loops", lines=2)`
- c) `build_prompt(lines=2)`
- d) `build_prompt("Explain loops", "2 lines")`

**Q5.** A client has 6 scripts that each copy the same 5 lines to call the AI. What is the professional fix?
- a) Keep copying; it works
- b) Write one `ask_ai()` function and build skills like `summarize()` on top of it
- c) Put all 6 scripts into one very long file
- d) Use a higher temperature

**Q6. Predict the Output**
```python
def add_tax(price: int, rate: float = 0.1) -> float:
    """Add tax to a price."""
    return price + price * rate


def show(price: float):
    print(f"Total: {price}")


total = add_tax(1000)
result = show(total)
print(result)
```

---

## Lesson 2.6: Files, JSON and Errors

**Q1.** You want every error to be **added** to `errors.log` without deleting the old ones. Which mode?
- a) `"r"`
- b) `"w"`
- c) `"a"`
- d) `"x"`

**Q2.** Why do we save chats with `json.dump(..., ensure_ascii=False)`?
- a) It makes the file smaller
- b) Urdu and other languages stay readable in the file instead of `ش...` codes
- c) It is required for `indent=2`
- d) It encrypts the file

**Q3.** Why is a bare `except:` (with no error name) a bad habit?
- a) It is slower
- b) It also hides your own bugs, so you never see what really broke
- c) Python does not allow it
- d) It only works with files

**Q4.** Your bot shows `httpx.ConnectError` when you ask a question. What does it mean?
- a) The JSON file is damaged
- b) The Ollama app is not running, so LangChain cannot reach it
- c) The model name is wrong
- d) The question was too long

**Q5.** Why do `chat_history.json` and `errors.log` go into `.gitignore`?
- a) Git cannot store JSON
- b) They hold private customer chats and should never reach a public repo
- c) They are too big for GitHub
- d) `uv` needs it

**Q6. Predict the Output**
```python
import json

row = json.loads('{"items": ["250", "abc", "300"]}')
total = 0
for text in row["items"]:
    try:
        total += int(text)
    except ValueError:
        print(f"Skipped {text}")
print(total)
```

---

## Lesson 2.7: Structured Output

**Q1.** Why is the extractor model created with `temperature=0`?
- a) It makes the model faster
- b) The same message should give the same data every time
- c) JSON only works at temperature 0
- d) It uses fewer tokens

**Q2.** What does `init_chat_model(..., format=ORDER_SCHEMA)` do?
- a) Formats the answer in bold
- b) Makes the model reply in the exact JSON shape described by the schema
- c) Checks that the prices are correct
- d) Saves the answer to a file

**Q3.** The message is `"3 brownies please, DHA phase 5"`, but the JSON says `"customer": "Ahmed"`. What is the right action?
- a) Trust it; the JSON is valid
- b) Flag it for a human check: the name is not in the message, so the AI invented it
- c) Raise the temperature
- d) Delete the order silently

**Q4.** Who should calculate the order total?
- a) The AI, it is good at maths
- b) Python, using **your** `PRICES` dictionary
- c) The customer
- d) Whoever is faster

**Q5.** `json.loads("Sure! Here is your order")` raises which error?
- a) `ValueError: not a number`
- b) `json.JSONDecodeError`
- c) `KeyError`
- d) No error

**Q6. Predict the Output**
```python
PRICES = {"cupcake": 250, "brownie": 300}
order = {"customer": "Sara", "items": [{"name": "cupcake", "quantity": 2}, {"name": "pizza", "quantity": 1}]}

total = 0
for item in order.get("items", []):
    if item["name"] not in PRICES:
        print(f"CHECK: {item['name']} is not on the menu")
        continue
    total += PRICES[item["name"]] * item["quantity"]
print(total, order.get("address", "(missing)"))
```

---

## Lesson 2.8: Your First Agent

**Q1.** How does the model decide **which** tool to call?
- a) It picks one at random
- b) It reads each tool's name and docstring
- c) It always calls the first tool
- d) It reads your Python code inside the function

**Q2.** After adding `@tool` to `get_price`, how do you run it yourself?
- a) `get_price("cupcake")`
- b) `get_price.invoke({"item": "cupcake"})`
- c) `get_price["cupcake"]`
- d) `tool(get_price, "cupcake")`

**Q3.** What must every `"tool"` message you send back include?
- a) The model name
- b) `"tool_call_id": call["id"]`, so the model knows which request the result answers
- c) The temperature
- d) The system message

**Q4.** Why does the agent loop use `MAX_STEPS`?
- a) To make the agent faster
- b) To stop the agent if it keeps calling tools without ever answering
- c) To limit how many customers can chat
- d) Tools only work 5 times

**Q5.** Which tool should ask a human for approval before it runs?
- a) `get_price`
- b) `order_status`
- c) `place_order`, because it spends money and changes data
- d) None, agents should be fully automatic

**Q6. Predict the Output**
```python
MAX_STEPS = 3
replies = ["tool", "tool", "tool", "answer"]

for step in range(MAX_STEPS):
    print(f"step {step}: {replies[step]}")
    if replies[step] == "answer":
        break
else:
    print("Gave up: a human will help")
```

---

## After the Check

- Answers are discussed in the **next class warm-up**.
- Got a question wrong? Re-read that lesson's section in `docs/` and redo its Code Task.
- Commit your answers file: `git commit -m "Module 2 checkpoint 2 quick checks"`

**Self-score guide**

| Score (per lesson) | Meaning |
|---|---|
| 6 | Mastered, move on |
| 4 to 5 | Good, review what you missed |
| 0 to 3 | Re-read the lesson and ask in class |
