# Module 2, Checkpoint 1: Code Tasks (Lessons 2.1 to 2.4)

**Course:** Python for AI · **Module 2:** Core Python for Building LLM Apps · **Updated:** Oct 2026

> **Student version.** From now on your code talks to a **real AI**. Every task is a small piece of client-style work. Build it yourself, push it to GitHub, and it becomes part of your portfolio.

---

## Rules for Every Task

| Rule | Why |
|---|---|
| Files go in `code/` (scripts) or `docs/` (notes, screenshots) | Clean, professional repo |
| Run with `uv run <file>.py` before submitting | Code that does not run = 0 marks |
| Ollama app running, `llama3.2` (or `llama3.2:1b`) pulled | Every task calls a local model |
| Commit `pyproject.toml` and `uv.lock` together with your code | Anyone can install your project with `uv sync` |
| One commit per task with a clear message | Commit history shows consistency |
| AI tools allowed, but you must explain **every line** | You will be asked in class |
| Submit = push to your public `python-ai` repo | No WhatsApp files |

**Commit message format:** `Task 2.1: AI tutor`

**Marks:** 10 per task · **Deadline:** before the next class

**About the expected outputs:** AI answers will differ every time you run, and so will the token counts and times. Your **structure** (labels, order, numbers printed) should match.

---

## Task 2.1: AI Tutor

**File:** `code/lesson_2_1_first_ai_call.py`

**Client story:** A tuition centre wants a tutor that explains any topic at the right level for each student, and they want to know how much each answer "costs" in tokens.

**Requirements**
1. Ask the user for a topic and a level (beginner or expert), and clean both with `.strip()`
2. Build a system message that sets the AI's role **and** the answer length
3. Create the model with `init_chat_model`, using temperature `0.2`, and call it with `.invoke()`
4. Print the answer, then the total tokens and the time in seconds (1 decimal)
5. Docstring and at least 2 "why" comments
6. Commit `pyproject.toml`, `uv.lock` and your file, and push

**Expected output (AI answers will differ)**
```text
Topic:   python lists
Level (beginner or expert): beginner
========================================
A list stores many values in one variable, like a shopping list.
You write it with square brackets: fruits = ["apple", "mango"].
You can add items with .append() and read them by position.
========================================
96 tokens in 2.4 seconds
```

**Checklist**
- [ ] Topic and level cleaned with `.strip()`
- [ ] System message sets the role and the length, and uses the level
- [ ] `init_chat_model(..., temperature=0.2)` and `.invoke()`
- [ ] Answer printed with `response.text`
- [ ] Tokens from `usage_metadata["total_tokens"]`, seconds from `total_duration` with `:.1f`
- [ ] `pyproject.toml` and `uv.lock` committed
- [ ] Docstring + 2 "why" comments

**Stretch:** upgrade your Module 1 project (`code/project_m1_prompt_kit.py`) so it sends Prompt 1 to the AI and prints the answer, instead of you copy-pasting it.

---

## Task 2.2: Personal Tutor with Memory

**File:** `code/lesson_2_2_chat_memory.py`

**Client story:** Students complain that the tutor "forgets" what they said one message ago. The centre wants a tutor that remembers the conversation, but without the cost growing forever.

**Requirements**
1. Start a `messages` list with a system message that sets the tutor's role and answer length
2. In a `while True` loop, append each user message, call `llm.invoke(messages)`, then append the AI reply
3. Commands:
   - `bye` exits
   - `/reset` clears memory but **keeps the system message**
   - `/count` prints how many messages are in memory
4. Keep only the system message plus the last 8 messages
5. After each answer, print the tokens sent (`usage_metadata["input_tokens"]`)
6. Docstring and at least 3 "why" comments
7. Run the **memory test** below before pushing

**Memory test (from Lesson 2.2, Section 6)**
1. `My name is Ali and I love chocolate`
2. `What cake do you suggest for me?`
3. `What is my name?` (the tutor must remember)
4. `/reset`, then `What is my name?` again (the tutor must **not** know)

**Expected output (AI answers will differ)**
```text
Tutor: Ask me anything. Commands: /reset, /count, bye
You: My name is Ali and I love chocolate
Tutor: Nice to meet you, Ali! Chocolate lovers make great bakers.
       (tokens sent: 48)
You: What is my name?
Tutor: Your name is Ali.
       (tokens sent: 79)
You: /count
Tutor: 5 messages in memory.
You: /reset
Tutor: Memory cleared.
You: What is my name?
Tutor: I don't know your name yet. What should I call you?
       (tokens sent: 38)
You: bye
Tutor: Goodbye!
```

**Checklist**
- [ ] System message is `messages[0]` and survives `/reset` and trimming
- [ ] User **and** assistant messages are appended
- [ ] `/count` uses `len(messages)`
- [ ] Trimming: `[messages[0]] + messages[1:][-8:]`
- [ ] Tokens sent printed after every answer
- [ ] Memory test done: remembers, then forgets after `/reset`
- [ ] Docstring + 3 "why" comments

**Stretch:** keep a second list, `questions`, with only the user's questions. On `bye`, print how many questions were asked and the first and last question.

---

## Task 2.3: Persona Bot with Real Facts

**File:** `code/lesson_2_3_persona_bot.py`

**Client story:** Your Module 1 business wants an AI assistant, but the owner is scared it will invent prices. They also want to choose its personality for different customers.

**Requirements**
1. A `facts` dictionary for **your own business** with at least 5 keys, including a nested `prices` dictionary with at least 3 items
2. A `personas` dictionary with at least 3 styles
3. Build the system message from `facts` with an f-string, and tell the AI to **only use these facts**
4. Chat with memory (Task 2.2), using a `config` dictionary for the model name, temperature and memory size
5. `/persona <name>` changes `messages[0]["content"]`, using `.get()` with a default so a wrong name never crashes
6. `/price <item>` answers from the dictionary **without calling the AI**; an unknown item gets a polite "not on our menu"
7. Docstring and at least 3 "why" comments
8. Run the **role play test** below before pushing

**Role play test (from Lesson 2.3, Section 6)**
- Ask the same question three times, switching persona between each: `/persona friendly`, `/persona formal`, `/persona sales`
- Then try `/price` with a real item in capitals, and `/price` with an item that is not on your menu
- Then ask the AI about something **not** in your facts (for example a product you do not sell): does it admit it does not know?

**Expected output (example business: Sweet Crumbs bakery; AI answers will differ)**
```text
Bot ready. Commands: /persona friendly|formal|sales, /price <item>, bye
You: Do you have cupcakes?
Bot: Yes! Our cupcakes are 250 PKR each, baked fresh every morning.
You: /persona sales
Bot: Style changed to: excited, always suggests one extra item to buy
You: Do you have cupcakes?
Bot: Yes, 250 PKR each! Add a brownie for just 300 PKR, a perfect pair!
You: /persona pirate
Bot: Style changed to: warm and cheerful, uses simple words
You: /price Cupcake
Bot: Cupcake costs 250 PKR.
You: /price donut
Bot: Sorry, donut is not on our menu.
You: bye
Bot: Goodbye!
```

**Checklist**
- [ ] `facts` has 5+ keys and a nested `prices` dictionary with 3+ items
- [ ] `personas` has 3+ styles
- [ ] System message is built from `facts` and says "only use these facts"
- [ ] `config` dictionary controls the model, temperature and memory size
- [ ] `/persona` with a wrong name falls back to a default (no `KeyError`)
- [ ] `/price` is answered from the dictionary, works with capitals, handles unknown items
- [ ] Role play test done
- [ ] Docstring + 3 "why" comments

**Stretch:** add `/add <item> <price>` that adds a new item to `facts["prices"]` and **rebuilds the system message**, so the AI knows about it immediately.

---

## Task 2.4: Batch Product Writer

**File:** `code/lesson_2_4_batch_writer.py`

**Client story:** The owner has a price list but no menu descriptions. Writing them by hand takes a whole day. Your script writes all of them in one run and reports the cost.

**Requirements**
1. A dictionary of at least 5 products or services for your business with prices, including **one with price `0`**
2. Loop with `.items()`; skip the price-0 item with `continue` and print that it was skipped
3. Create the model **once, before the loop**; call the AI for a one-sentence description of each item
4. Collect the results in a **list of dictionaries** (item, price, text)
5. Add up the total tokens and the total seconds with accumulators
6. After the loop, print a numbered menu with `enumerate`, then a summary line
7. Docstring and at least 3 "why" comments

**Expected output (AI text, tokens and times will differ)**
```text
Skipping old stock (no price)
==================================================
1. Chocolate Cake (1500 PKR)
   Rich, moist layers of pure chocolate, baked fresh in Lahore every morning.
2. Cupcake (250 PKR)
   A soft, swirled little treat that makes any tea time sweeter.
3. Brownie (300 PKR)
   Fudgy, gooey and packed with chocolate in every single bite.
4. Donut (200 PKR)
   Light, golden and glazed, the perfect sweet start to your day.
==================================================
4 descriptions, 412 tokens, 6.8 seconds
```

**Checklist**
- [ ] 5+ items, one with price `0`
- [ ] `for name, price in products.items():`
- [ ] `continue` skips the price-0 item (no AI call, no tokens spent)
- [ ] Model created once, outside the loop
- [ ] Results stored as a list of dictionaries
- [ ] Token and time accumulators start at 0 **before** the loop
- [ ] Numbered menu with `enumerate(..., start=1)` and a summary line
- [ ] Docstring + 3 "why" comments

**Stretch:** create `code/lesson_2_4_bot_battle.py` with at least 6 test questions for your business. Run each through your Lesson 1.8 style rules and through the AI, print both answers, and count how many questions the rules could not answer.

---

## Marking (10 per task)

| Criteria | Marks |
|---|---|
| Runs without errors | 4 |
| Meets all requirements | 3 |
| Clean code and clear comments | 2 |
| Pushed on time with a clear commit message | 1 |

**Stretch done = +1 bonus** (max 10)

**Need help?** Read the error's last line, check the lesson's "Common Errors" table in `docs/02-talk-to-ai/`, then ask in class.

**Checkpoint 1 project:** after these four tasks, build the [AI Content Studio](checkpoint-1-project-content-studio.md).
