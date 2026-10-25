# Module 1, Checkpoint 1: Quick Checks (Lessons 1.1 to 1.4)

**Course:** Python for AI · **Module 1:** Python Basics for GenAI and Agentic AI · **Updated:** Oct 2026

> **Student version.** Answer on your own first, without AI tools or notes. The goal is to find what you have not understood yet, not to get full marks.

**Format per lesson:** 5 MCQs + 1 "Predict the Output" · **Time:** 5 minutes · **Marks:** 6 per lesson

**How to answer:** write your answers in a file `docs/my-answers-module-1.md` like this:

```text
1.1: Q1 b, Q2 c, Q3 ..., Q6 Hello ...
```

**Predict the Output rule:** write your answer **before** running the code. Then run it with `uv run` and check yourself.

---

## Lesson 1.1: Welcome to GenAI & Agentic AI

**Q1.** Which best describes **Agentic AI**?
- a) A chatbot that gives one reply to one question
- b) AI that plans, uses tools and acts in a loop until a goal is done
- c) Software that trains new AI models from scratch
- d) AI that only generates images

**Q2.** At its core, a Large Language Model (LLM) works by:
- a) Searching Google for every answer
- b) Following rules written by programmers
- c) Predicting the next token
- d) Copying answers from a fixed database

**Q3.** An agent books a table, but two steps later it has forgotten which restaurant the user chose. Using **Agent = LLM + Tools + Memory + Loop**, which part is failing?
- a) LLM
- b) Tools
- c) Memory
- d) Loop

**Q4.** A bakery owner wants a WhatsApp bot that answers customer questions within a month. What is the most practical plan?
- a) Train a new language model on the bakery's data first
- b) Study deep learning maths for a year, then build it
- c) Connect an existing model to the bakery's information through an API
- d) Wait until AI is cheaper

**Q5.** An AI gives a confident answer that is completely wrong. This is called:
- a) A token
- b) A hallucination
- c) A prompt
- d) A context window

**Q6. Predict the Output**
```python
tool = "Ollama"
print(f"{tool} runs AI on my laptop.")
```

---

## Lesson 1.2: Setting Up Your AI Dev Toolkit

**Q1.** You join a team. Their repo has `pyproject.toml` and `uv.lock`. Which **one** tool can install the right Python version **and** all the packages?
- a) pip
- b) Git
- c) uv
- d) VS Code

**Q2.** You just installed Ollama on Windows, but the open terminal says `ollama: command not found`. What should you try **first**?
- a) Reinstall Windows
- b) Close and reopen the terminal
- c) Install Ollama with pip
- d) Buy a faster laptop

**Q3.** Why does the course use Python 3.13 instead of the newest version?
- a) Newer versions are paid
- b) AI libraries need time to support new versions, so pros use a stable one
- c) 3.13 is the only version uv supports
- d) Newer versions do not have `print()`

**Q4.** A law firm wants AI to summarise contracts, but the contracts must never leave their office. What do you suggest?
- a) Paste the contracts into a chatbot website
- b) Run a model locally with Ollama
- c) Upload the contracts to a public GitHub repo
- d) Email the contracts to yourself and summarise them at home

**Q5.** Why should your `git config` email match your GitHub account email?
- a) Git will not install otherwise
- b) So your commits are linked to your GitHub profile
- c) To make code run faster
- d) It is required by Python

**Q6. Predict the Output**
Your project's `.python-version` file says `3.13`. You run these commands inside the project. Which Python version does the last line print, 3.12 or 3.13, and why?
```bash
uv python install 3.12 3.13
uv run python --version
```

---

## Lesson 1.3: Your First Python Project with uv

**Q1.** Your script works on your laptop but crashes on a client's laptop, because they installed a newer version of one package. Which file, committed to the repo, would have prevented this?
- a) `README.md`
- b) `uv.lock`
- c) `main.py`
- d) `.gitignore`

**Q2.** A teammate's GitHub repo is 900 MB because they pushed their `.venv/` folder. Which file should have stopped this?
- a) `pyproject.toml`
- b) `.gitignore`
- c) `uv.lock`
- d) `.python-version`

**Q3.** You want to add the `requests` package to your uv project. Which command is correct?
- a) `pip install requests`
- b) `uv add requests`
- c) `git add requests`
- d) `python requests`

**Q4.** Which file tells uv which Python version this project uses?
- a) `uv.lock`
- b) `.python-version`
- c) `README.md`
- d) `main.py`

**Q5.** You open a new terminal, forget to activate `.venv`, and run `uv run main.py`. What happens?
- a) An error: the environment is not active
- b) It runs using the project's own `.venv`
- c) It runs with whatever Python the laptop has, ignoring the project
- d) It deletes `.venv` and creates a new one

**Q6. Predict the Output**
```python
course = "Python for AI"
lesson = 3
print(f"{course}, lesson {lesson}: my first project")
```

---

## Lesson 1.4: Talking to Python: print, input and Comments

**Q1.** The user types `3.5` into `price = input("Price: ")`. What is the type of `price`?
- a) float
- b) int
- c) str
- d) It depends on what the user types

**Q2.** What does this print?
```python
print("AI", "is", "fun", sep="_", end="!")
```
- a) `AI is fun!`
- b) `AI_is_fun!`
- c) `AI_is_fun_!`
- d) `AI_is_fun`

**Q3.** `price = 250`, then `print("Price: " + price + " PKR")` gives an error. Which line fixes it?
- a) `print("Price: " - price - " PKR")`
- b) `print(f"Price: {price} PKR")`
- c) `print(Price: price PKR)`
- d) `print("Price: " + "price" + 250)`

**Q4.** Which is the **best** comment?
- a) `max_tokens = 150  # set max_tokens to 150`
- b) `max_tokens = 150  # short limit so replies fit on a phone screen`
- c) `max_tokens = 150  # max tokens`
- d) `max_tokens = 150  # number`

**Q5.** The user types `2.5` into `qty = int(input("Quantity: "))`. What happens?
- a) SyntaxError
- b) No error: `qty` becomes `2`
- c) ValueError
- d) NameError

**Q6. Predict the Output**
The user types `20`.
```python
age = input("Age: ")
print(age + "1")
```

---

## After the Check

- Answers are discussed in the **next class warm-up**.
- Got a question wrong? Re-read that lesson's section in `docs/` and redo its Code Task.
- Commit your answers file: `git commit -m "Module 1 quick checks"`

**Self-score guide**

| Score (per lesson) | Meaning |
|---|---|
| 6 | Mastered, move on |
| 4 to 5 | Good, review what you missed |
| 0 to 3 | Re-read the lesson and ask in class |
