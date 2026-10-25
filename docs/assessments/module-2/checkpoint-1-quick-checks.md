# Module 2, Checkpoint 1: Quick Checks (Lessons 2.1 to 2.4)

**Course:** Python for AI · **Module 2:** Core Python for Building LLM Apps · **Updated:** Oct 2026

> **Student version.** Answer on your own first, without AI tools or notes. The goal is to find what you have not understood yet, not to get full marks.

**Format per lesson:** 5 MCQs + 1 "Predict the Output" · **Time:** 5 minutes · **Marks:** 6 per lesson

**How to answer:** write your answers in a file `docs/my-answers-module-2.md` like this:

```text
2.1: Q1 ?, Q2 ?, Q3 ?, Q4 ?, Q5 ?, Q6 (your predicted output)
```

**Predict the Output rule:** write your answer **before** running the code. Then run it with `uv run` and check yourself.

---

## Lesson 2.1: Your First AI Call

**Q1.** Your app runs on Ollama today. A client wants it on Claude next month. With LangChain, what do you change?
- a) Rewrite the whole app in a new library
- b) The model name and `model_provider` in `init_chat_model`
- c) Reinstall Python
- d) Nothing can be changed; Ollama apps only work with Ollama

**Q2.** After `reply = llm.invoke(messages)`, where is the AI's answer as text?
- a) `reply`
- b) `reply.text`
- c) `reply["answer"]`
- d) `messages[-1]`

**Q3.** A bank's bot must explain the same fee policy the same way every time. Which setting fits best?
- a) `temperature=1.2`
- b) `temperature=0.1`
- c) Streaming
- d) A longer system message only

**Q4.** Your script stops with `httpx.ConnectError: [Errno 111] Connection refused`. What do you check **first**?
- a) Is the Ollama app running?
- b) Reinstall LangChain
- c) Change the temperature
- d) Delete `uv.lock`

**Q5.** Why does streaming (`llm.stream`) feel faster to users?
- a) The model thinks faster
- b) The answer appears word by word as it is written, instead of all at the end
- c) It uses fewer tokens
- d) It skips the system message

**Q6. Predict the Output**
```python
usage = {"input_tokens": 120, "output_tokens": 80, "total_tokens": 200}
duration = 3_500_000_000
print(f"{usage['total_tokens']} tokens in {duration / 1_000_000_000:.1f} seconds")
```

---

## Lesson 2.2: Chat History with Lists

**Q1.** `tools = ["search", "calculator", "weather"]`. What is `tools[-2]`?
- a) `"search"`
- b) `"calculator"`
- c) `"weather"`
- d) IndexError

**Q2.** What is `history` after these two lines?
```python
history = ["hi"]
history = history.append("bye")
```
- a) `["hi", "bye"]`
- b) `None`
- c) `["bye"]`
- d) Error

**Q3.** A support bot asks for the order number, then two messages later asks for it again. What is the most likely cause?
- a) The model is broken
- b) The bot does not send the earlier messages in the history, so the model never sees the order number
- c) The temperature is too high
- d) The model has too many tokens

**Q4.** Why do pros trim history with `[messages[0]] + messages[-6:]` instead of just `messages[-6:]`?
- a) To keep the system message (the bot's rules), which would otherwise be cut
- b) Because slices only work with 6
- c) To make the list longer
- d) There is no difference

**Q5.** A chatbot sends all 60 past messages on every turn. What is the main problem?
- a) Python cannot store 60 items
- b) Each call gets slower and more expensive, and may overflow the context window
- c) The model becomes smarter
- d) Nothing

**Q6. Predict the Output**
```python
history = ["sys", "u1", "a1", "u2", "a2", "u3"]
short = [history[0]] + history[-3:]
print(short, len(history))
```

---

## Lesson 2.3: Messages are Dictionaries

**Q1.** `menu = {"tea": 80, "coffee": 250}`. What does `menu.get("juice", 0)` return?
- a) `None`
- b) `0`
- c) `KeyError`
- d) `"juice"`

**Q2.** Same `menu`. What does `menu["juice"]` do?
- a) Returns `0`
- b) Returns `None`
- c) Raises `KeyError`
- d) Adds `"juice"` to the menu

**Q3.** Which line adds samosas at 60 PKR to `menu`?
- a) `menu.add("samosa", 60)`
- b) `menu["samosa"] = 60`
- c) `menu.append({"samosa": 60})`
- d) `menu = "samosa": 60`

**Q4.** `order = {"customer": {"name": "Ali", "city": "Multan"}, "items": ["tea", "cake"]}`. Which reads `"Multan"`?
- a) `order["city"]`
- b) `order["customer"]["city"]`
- c) `order.customer.city`
- d) `order[1]["city"]`

**Q5.** A clinic's bot keeps inventing consultation fees. What is the best fix?
- a) Raise the temperature
- b) Put the real fees from a dictionary into the system message and tell the AI to only use them
- c) Use a bigger font
- d) Remove the system message

**Q6. Predict the Output**
```python
stock = {"cupcake": 12, "brownie": 0}
stock["cupcake"] = stock["cupcake"] - 5
stock["donut"] = 8
print(stock, len(stock), "brownie" in stock)
```

---

## Lesson 2.4: Loops that Talk

**Q1.** What does `list(range(3, 7))` give?
- a) `[3, 4, 5, 6, 7]`
- b) `[3, 4, 5, 6]`
- c) `[4, 5, 6, 7]`
- d) `[3, 7]`

**Q2.** You need both the item name and its price from `prices = {"tea": 80, "cake": 900}`. Which loop gives both?
- a) `for item in prices:`
- b) `for item, price in prices.items():`
- c) `for item, price in prices:`
- d) `for price in prices.values():`

**Q3.** What does this print?
```python
for price in [100, 200, 300]:
    total = 0
    total += price
print(total)
```
- a) `600`
- b) `300`
- c) `0`
- d) Error

**Q4.** In a batch job, which statement skips one item but keeps the loop going?
- a) `break`
- b) `continue`
- c) `stop`
- d) `return`

**Q5.** In a batch writer, why is `init_chat_model(...)` written **before** the loop?
- a) Python requires it
- b) The model is created once and reused for every item, instead of being created again each round
- c) It makes the AI answers longer
- d) Loops cannot contain function calls

**Q6. Predict the Output**
```python
reviews = ["great", "late again", "", "loved it"]
count = 0
for number, review in enumerate(reviews, start=1):
    if review == "":
        continue
    if "late" in review:
        print(f"{number}: complaint")
    count += 1
print(count)
```

---

## After the Check

- Answers are discussed in the **next class warm-up**.
- Got a question wrong? Re-read that lesson's section in `docs/` and redo its Code Task.
- Commit your answers file: `git commit -m "Module 2 checkpoint 1 quick checks"`

**Self-score guide**

| Score (per lesson) | Meaning |
|---|---|
| 6 | Mastered, move on |
| 4 to 5 | Good, review what you missed |
| 0 to 3 | Re-read the lesson and ask in class |
