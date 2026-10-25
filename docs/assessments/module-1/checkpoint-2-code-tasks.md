# Module 1, Checkpoint 2: Code Tasks (Lessons 1.5 to 1.8)

**Course:** Python for AI · **Module 1:** Python Basics for GenAI and Agentic AI · **Updated:** Oct 2026

> **Student version.** Every task is a small piece of real client-style work. Build it yourself, push it to GitHub, and it becomes part of your portfolio. Task 1.8 is your **Module 1 final**: a chatbot for a real local business.

---

## Rules for Every Task

| Rule | Why |
|---|---|
| Files go in `code/` (scripts) or `docs/` (notes, screenshots) | Clean, professional repo |
| Run with `uv run <file>.py` before submitting | Code that does not run = 0 marks |
| One commit per task with a clear message | Commit history shows consistency |
| AI tools allowed, but you must explain **every line** | You will be asked in class |
| Use only what Lessons 1.1 to 1.8 teach | Shows you understand your own code |
| Submit = push to your public `python-ai` repo | No WhatsApp files |

**Commit message format:** `Task 1.5: model profile card`

**Marks:** 10 per task · **Deadline:** before the next class

---

## Task 1.5: AI Model Profile Card

**File:** `code/lesson_05_variables.py`

**Client story:** A client asks: "Which AI model should we use, and what will it cost per chat?" You prepare a one-screen profile card with a cost estimate.

**Requirements**
1. Store a model profile using **all 4 types**:
   - model name (`str`)
   - context window in tokens (`int`)
   - example price per 1K tokens in PKR (`float`)
   - runs locally (`bool`)
2. Print each one with an f-string **and** its `type()`
3. Ask the user how many tokens a chat uses with `int(input())`
4. Print the estimated cost, rounded to 2 decimals with `round()`
5. Docstring and at least 2 "why" comments
6. Use `snake_case` names, and never reuse built-in names like `input` or `type`

**Expected output (your model and numbers will differ)**
```text
--- AI Model Profile Card ---
Model: llama3.2 <class 'str'>
Context window: 128000 tokens <class 'int'>
Price per 1K tokens: 0.5 PKR <class 'float'>
Runs locally: True <class 'bool'>
Tokens per chat: 1500
Estimated cost: 0.75 PKR
```

**Checklist**
- [ ] All 4 types used: `str`, `int`, `float`, `bool`
- [ ] Every value printed with an f-string and its `type()`
- [ ] Tokens converted with `int(input())`
- [ ] Cost rounded to 2 decimals
- [ ] Docstring + 2 "why" comments

**Stretch:** ask for chats per day and print the estimated **monthly** cost (30 days).

**Tip:** look up a real model's context window on https://ollama.com/library. Label your price as an example.

---

## Task 1.6: Prompt Cleaner

**File:** `code/lesson_06_strings_prompts.py`

**Client story:** Customers type messy questions with extra spaces and random capitals. Before anything goes to an AI, the agency wants it cleaned, measured and safely sized.

**Requirements**
1. Ask the user for their **name** and a **messy question**
2. Clean the name with `.strip().title()` and the question with `.strip().capitalize()`
3. Print the number of characters (`len()`) and the estimated tokens (characters / 4, rounded)
4. Print whether the question mentions "python" in any capitals, using `in` and `.lower()`
5. Build and print a **multi-line f-string** prompt that greets the user by name, with the question limited to **150 characters** using slicing
6. Docstring and at least 2 "why" comments

**Expected output**
```text
Your name:   ayesha KHAN
Your question:    how do i LEARN python for ai?
========================================
Cleaned question: How do i learn python for ai?
Characters: 29, about 7 tokens
Mentions Python: True
========================================
You are a friendly Python tutor.
Greet Ayesha Khan by name and answer in 3 short lines.
Question: How do i learn python for ai?
```

**Checklist**
- [ ] Name and question both cleaned
- [ ] Characters and estimated tokens printed
- [ ] "python" check works with any capitals
- [ ] Multi-line f-string prompt with `[:150]` slicing
- [ ] Docstring + 2 "why" comments

**Stretch:** replace a bad word before building the prompt, for example `.replace("stupid", "***")`, and print the estimated cost with 2 decimals using `:.2f`.

---

## Task 1.7: Smart Model Router

**File:** `code/lesson_07_conditions.py`

**Client story:** A company is paying too much for AI. They want a router that sends private data to a local model, code questions to a strong model, and everything else to a cheap one.

**Requirements**
1. Ask for the task type (`code`, `private` or `chat`) and clean it with `.strip().lower()`
2. Ask for the estimated tokens and convert with `int()`
3. Use `if / elif / else` to choose a model name for each task type
4. Calculate the cost with an example price per 1K tokens; set `price = 0` for the local model
5. If tokens are over 4000, print a warning; otherwise print `Length is fine.`
6. Print the chosen model and the cost with 2 decimals (`:.2f`)
7. Docstring and at least 2 "why" comments

**Expected output (two runs)**
```text
Task (code / private / chat):  Code
Estimated tokens: 5000
Warning: long request, consider shortening it.
Chosen model: claude (cloud, strong at code)
Estimated cost: 4.00 PKR
```
```text
Task (code / private / chat): private
Estimated tokens: 800
Length is fine.
Chosen model: llama3.2 (local, Ollama)
Estimated cost: 0.00 PKR
```

**Checklist**
- [ ] Task type cleaned, so `" Code "` still works
- [ ] `if / elif / else` covers all three task types
- [ ] Local model costs `0.00`
- [ ] Long-request warning above 4000 tokens
- [ ] Cost printed with `:.2f`
- [ ] Docstring + 2 "why" comments

**Stretch:** ask "Is this a paid user? (yes/no)". Free users with more than 2000 tokens get the message `Upgrade to send long requests.` Use `and`.

---

## Task 1.8: Business Helper Bot (Module 1 Final)

**File:** `code/lesson_08_mini_chatbot.py` + a design table in `README.md`

**Client story:** A real local business (family shop, clinic, tuition centre, salon) answers the same questions all day. Build them a chatbot that handles the common ones and shows them which questions still need help.

**Requirements**
1. **Design first:** add a table to your `README.md` with at least **5 intents** (what the user wants, keywords to look for, reply)
2. Ask the user's name **once, before the loop**, and use it in replies
3. Use `while True` with a `bye` exit and `break`
4. Clean every message with `.strip().lower()`
5. Put the complaint or human-handover rule **first**
6. Fallback: count unanswered questions and print the AI prompt you would send in Module 2
7. On exit, print a summary with the message count and the unanswered count
8. Docstring and at least **3** "why" comments
9. Run every test from Lesson 1.8, Section 5, on your bot before pushing

**Expected output (example business: City Care Clinic; yours will differ)**
```text
City Care Bot: Hi! Ask about timings, fees, location or appointments. Type 'bye' to exit.
City Care Bot: What is your name?  sara malik
Sara Malik: What are your TIMINGS?
City Care Bot: We are open 10 am to 8 pm, Monday to Saturday.
Sara Malik:   how much is the fee
City Care Bot: Consultation fee is 2,000 PKR.
Sara Malik: my report is late
City Care Bot: Sorry about that. The clinic manager will call you today.
Sara Malik: which doctor is best?
City Care Bot: I am not sure yet. In Module 2, an AI will answer: You are the friendly assistant of City Care Clinic. Answer in 2 lines: which doctor is best?
Sara Malik: BYE
City Care Bot: Take care, Sara Malik!
========================================
Chat summary: 5 messages, 1 unanswered.
```

**Checklist**
- [ ] README design table with at least 5 intents
- [ ] Name asked once, before the loop
- [ ] `while True` + `break` on `bye`
- [ ] Capitals and extra spaces handled
- [ ] Complaint rule comes first
- [ ] Short words like "hi" checked with `==` or `.startswith()`, not `in`
- [ ] Fallback counts unanswered questions and prints the AI prompt
- [ ] Summary printed on exit
- [ ] Docstring + 3 "why" comments

**Stretch:** add an `agent` or `human` keyword that ends the chat with `Connecting you to a human...`, and count how many complaints the bot received.

---

## Marking (10 per task)

| Criteria | Marks |
|---|---|
| Runs without errors | 4 |
| Meets all requirements | 3 |
| Clean code and clear comments / README | 2 |
| Pushed on time with a clear commit message | 1 |

**Stretch done = +1 bonus** (max 10)

**Need help?** Read the error's last line, re-read the lesson in `docs/`, then ask in class.
