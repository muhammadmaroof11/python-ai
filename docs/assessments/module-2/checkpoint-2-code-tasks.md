# Module 2, Checkpoint 2: Code Tasks (Lessons 2.5 to 2.8)

**Course:** Python for AI · **Module 2:** Core Python for Building LLM Apps · **Updated:** Oct 2026

> **Student version.** These tasks turn your bot into a real product: reusable skills, saved data, clean structured output, and an agent that uses tools. Build each one for **your own business** from Module 1, push it to GitHub, and it becomes part of your portfolio.

---

## Rules for Every Task

| Rule | Why |
|---|---|
| Files go in `code/` (scripts, data files) or `docs/` (notes, screenshots) | Clean, professional repo |
| Run with `uv run <file>.py` from the `code` folder before submitting | File paths like `"faq.json"` are relative to the folder you run from |
| Ollama app running, `llama3.2` (or another model with **tools** support) pulled | Every task calls a local model; Task 2.8 needs tool support |
| Commit `pyproject.toml` and `uv.lock` when you add a package | Anyone can install your project with `uv sync` |
| Private data files (`chat_history.json`, `errors.log`, `orders.json`) go in `.gitignore` | Customer data never reaches a public repo |
| One commit per task with a clear message | Commit history shows consistency |
| AI tools allowed, but you must explain **every line** | You will be asked in class |
| Submit = push to your public `python-ai` repo | No WhatsApp files |

**Commit message format:** `Task 2.5: AI skills toolkit`

**Marks:** 10 per task · **Deadline:** before the next class

**About the expected outputs:** AI answers will differ every time you run. Your **structure** (labels, order, checks, numbers) should match.

---

## Task 2.5: AI Skills Toolkit

**File:** `code/lesson_2_5_ai_skills.py`

**Client story:** A marketing agency uses AI for the same jobs every day (summaries, translations, review replies), and every staff member writes the prompts differently. They want one toolkit with tested, reusable skills.

**Requirements**
1. Create the models **once, at the top**: a precise one (low temperature) and a creative one (high temperature)
2. An `ask_ai(prompt, system=..., creative_mode=False)` function that picks the model, calls it and **returns** `response.text`
3. At least **3 skills** built on `ask_ai()` for your business (for example `summarize`, `translate`, `reply_to_review`), each with a type-hinted parameter, a docstring and a `return`
4. At least one skill with a **default** parameter (for example `language: str = "Urdu"`)
5. At least one function that does **not** need the AI (for example `estimate_tokens`), with at least **2 `assert` tests**
6. A menu loop with one command per skill and `bye`, and a `usage` dictionary that counts how often each skill is used; print the counts with a `for` loop at the end
7. Docstring at the top and at least 3 "why" comments

**Expected output (example business: Sweet Crumbs bakery; AI answers will differ)**
```text
Sweet Crumbs AI Toolkit. Commands: /summarize, /translate, /reply, bye
Command: /translate
Text to translate: Your order is ready for pickup.
Language (Enter for Urdu):
AI: آپ کا آرڈر لینے کے لیے تیار ہے۔
Command: /reply
Customer review: Cake was great but delivery was late.
AI: Thank you for the kind words about our cake! We are sorry about the delay and are working to make delivery faster.
    (review was about 9 tokens)
Command: /dance
Unknown command. Try /summarize, /translate, /reply or bye.
Command: bye
Skills used today:
  summarize: 0
  translate: 1
  reply: 1
```

**Checklist**
- [ ] Models created once, at the top, not inside a function
- [ ] `ask_ai()` returns text; skills `return`, the main program `print`s
- [ ] 3+ skills with type hints and docstrings
- [ ] A default parameter, and the default is used when the user presses Enter
- [ ] A function with 2+ `assert` tests that need no AI
- [ ] `usage` dictionary counts every skill; report printed with a `for` loop
- [ ] Docstring + 3 "why" comments

**Stretch:** add a `/batch` command that runs one skill over a **list** of 3 reviews in a `for` loop, and prints each result with `enumerate`.

---

## Task 2.6: Saved Bot

**Files:** `code/faq.json`, `code/lesson_2_6_saved_bot.py`, `.gitignore`

**Client story:** The owner wants to change prices without calling you, and customers want the bot to remember yesterday's chat. And it must **never** show a red error to a customer.

**Requirements**
1. `faq.json` with at least 5 keys for your business, including a nested `prices` dictionary
2. Load the facts with `json.load` and build the system message from them; exit with a clear message if the file is missing
3. Load old chat history from `chat_history.json`; handle the file being **missing** and being **damaged**
4. Save the history after every turn with `indent=2` and `ensure_ascii=False` (plain dictionaries only)
5. Handle `httpx.ConnectError` and `ollama.ResponseError` with friendly messages, and append each error to `errors.log`
6. Add `chat_history.json` and `errors.log` to `.gitignore`
7. Docstring and at least 3 "why" comments
8. Let a classmate run **Break the Bot** (Lesson 2.6, Section 7) on it, fix what breaks, then push

**Expected output (two runs; AI answers will differ)**
```text
Sweet Crumbs Bot: Ask me anything. Commands: /reset, bye
You: My name is Sara. Do you deliver?
Bot: Hi Sara! Yes, delivery is free for orders over 3,000 PKR.
You: bye
Bot: Goodbye! Your chat is saved.
```
```text
Loaded 2 old messages.
Sweet Crumbs Bot: Ask me anything. Commands: /reset, bye
You: What is my name?
Bot: Your name is Sara.
You: bye
Bot: Goodbye! Your chat is saved.
```

**Break the Bot results (with the Ollama app closed, and with a damaged history file)**
```text
History file was damaged. Starting a fresh chat.
Sweet Crumbs Bot: Ask me anything. Commands: /reset, bye
You: hi
Bot: I am offline right now. Please open the Ollama app and try again.
```

**Checklist**
- [ ] Facts come from `faq.json`; changing a price there changes the bot's answer
- [ ] Missing `faq.json` gives a clear message, not a traceback
- [ ] Missing **and** damaged history both handled
- [ ] History saved every turn, readable (`indent=2`, `ensure_ascii=False`)
- [ ] `httpx.ConnectError` and `ollama.ResponseError` caught, logged to `errors.log`
- [ ] Unanswered question removed from history when the AI fails
- [ ] `.gitignore` updated
- [ ] Break the Bot done, every crash fixed
- [ ] Docstring + 3 "why" comments

**Stretch:** add `/export`, which writes the chat as a readable transcript to `transcript.txt` (one line per message: `user: ...` / `assistant: ...`) using a `for` loop.

---

## Task 2.7: Order Extractor

**File:** `code/lesson_2_7_extractor.py`

**Client story:** The business gets 50 WhatsApp orders a day in mixed English and Roman Urdu. Staff copy them into a notebook by hand and make mistakes. Your extractor turns them into clean, checked data with correct totals.

**Requirements**
1. A `PRICES` (or services) dictionary with at least 3 items
2. A list of at least **5** messy customer messages:
   - one normal order
   - one with 2 or more items
   - one with an item **not** on your menu
   - one that is **not** an order
   - one in Roman Urdu
3. A JSON schema, and an extractor model created with `format=` your schema and temperature `0`
4. Check every reply:
   - the JSON is valid (`json.JSONDecodeError` handled)
   - keys are read with `.get()`
   - every item is on your menu
   - the customer name really is in the message
5. Calculate totals **in Python** with your prices, and save the orders to `orders.json`
6. Print a short report: orders found, total value, and every `CHECK` warning
7. Docstring and at least 3 "why" comments
8. Run the **Hallucination Hunt** (Lesson 2.7, Section 7) and save what you found in `docs/hallucination-hunt.md`

**Expected output (AI extraction may differ)**
```text
Message: Salam! 2 cupcakes aur 1 chocolate cake chahiye. Ali, house 12 Gulberg
  2 x cupcake = 500 PKR
  1 x chocolate cake = 1500 PKR
  Customer: Ali, Address: house 12 Gulberg
  Total: 2000 PKR

Message: 1 pizza and 2 brownies, Bilal, Model Town
  2 x brownie = 600 PKR
  Customer: Bilal, Address: Model Town
  Total: 600 PKR
  CHECK: 'pizza' is not on the menu

Message: hi do you deliver to Johar Town?
  Not an order: needs a human reply.

==================================================
Orders found: 2 | Total value: 2,600 PKR | Checks: 1
Saved 2 orders to orders.json
```

**Checklist**
- [ ] 5+ messages covering all five cases
- [ ] Schema passed with `format=`, temperature `0`
- [ ] `json.loads` inside `try / except json.JSONDecodeError`
- [ ] Keys read with `.get()` and a default
- [ ] Off-menu items flagged with `CHECK`, never priced
- [ ] Invented customer names flagged
- [ ] Totals calculated in Python, saved to `orders.json`
- [ ] Report with orders, total value and checks
- [ ] Hallucination Hunt results saved
- [ ] Docstring + 3 "why" comments

**Stretch:** also write `orders.csv` (one line per item: `customer,item,quantity,line_total`) using a `for` loop and f-strings, then open it in Excel or Google Sheets.

---

## Task 2.8: Your First Agent

**File:** `code/lesson_2_8_first_agent.py`

**Client story:** The owner wants an assistant that does not just talk, but **does things**: looks up real data, checks orders, and places new ones, but never spends money without the owner saying yes.

**Requirements**
1. At least **3 tools** with `@tool(parse_docstring=True)`, type hints and a full docstring with `Args:`:
   - one that **reads** data (prices, services, hours)
   - one that **checks** something (booking, order or stock status)
   - one that **acts** (book, order or save) and asks for **your approval** before doing it
2. A `TOOLS` dictionary, `bind_tools`, and the agent loop with `MAX_STEPS` (and `for ... else` for the fallback reply)
3. Handle an unknown tool name and wrong arguments (`ValidationError`) without crashing
4. Print every tool call as `[tool] name(args) -> result`
5. Memory across questions, and `bye` to exit
6. Docstring at the top and at least 3 "why" comments
7. Run the **Watch the Agent Think** activity (Lesson 2.8, Section 7) on your agent, and record how many times it picked the right tool

**Expected output (the tools the agent picks may differ)**
```text
Sweet Crumbs Agent: ask about prices, orders, or place an order. Type 'bye' to exit.
You: Compare the price of a brownie and a cupcake
  [tool] get_price({'item': 'brownie'}) -> brownie costs 300 PKR
  [tool] get_price({'item': 'cupcake'}) -> cupcake costs 250 PKR
Agent: A brownie is 300 PKR and a cupcake is 250 PKR, so the cupcake is 50 PKR cheaper.
You: Where is my order A102?
  [tool] order_status({'order_id': 'A102'}) -> Order A102 is out for delivery
Agent: Your order A102 is out for delivery.
You: I am Ali, I want 2 brownies
  [approve] 2 x brownie for Ali = 600 PKR. Place it? (yes/no) yes
  [tool] place_order({'item': 'brownie', 'quantity': 2, 'customer': 'Ali'}) -> Order A104 placed: 2 x brownie, total 600 PKR
Agent: Done, Ali! Your order A104 for 2 brownies is placed. Total: 600 PKR.
You: bye
```

**Checklist**
- [ ] 3+ tools: read, check, act
- [ ] Every tool has type hints and a docstring with `Args:`
- [ ] The act tool asks for approval with `input()` and returns a clear message if you say no
- [ ] `TOOLS` dictionary + `bind_tools`
- [ ] Agent loop with `MAX_STEPS` and a `for ... else` fallback
- [ ] `"tool"` messages include `tool_call_id`
- [ ] Unknown tool and `ValidationError` handled
- [ ] Every tool call printed
- [ ] Activity done and results recorded
- [ ] Docstring + 3 "why" comments

**Stretch:** add a 4th tool that reads `faq.json` from Task 2.6, so the agent can answer any FAQ from the owner's file.

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

**Checkpoint 2 project:** after these four tasks, build the [AI Business Assistant](checkpoint-2-project-business-assistant.md), your Module 2 final.
