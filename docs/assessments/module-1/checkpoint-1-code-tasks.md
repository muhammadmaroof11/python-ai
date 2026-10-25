# Module 1, Checkpoint 1: Code Tasks (Lessons 1.1 to 1.4)

**Course:** Python for AI · **Module 1:** Python Basics for GenAI and Agentic AI · **Updated:** Oct 2026

> **Student version.** Every task is a small piece of real client-style work. Build it yourself, push it to GitHub, and it becomes part of your portfolio.

---

## Rules for Every Task

| Rule | Why |
|---|---|
| Files go in `code/` (scripts) or `docs/` (notes, screenshots) | Clean, professional repo |
| Run with `uv run <file>.py` before submitting | Code that does not run = 0 marks |
| One commit per task with a clear message | Commit history shows consistency |
| AI tools allowed, but you must explain **every line** | You will be asked in class |
| Submit = push to your public `python-ai` repo | No WhatsApp files |

**Commit message format:** `Task 1.1: intro script`

**Marks:** 10 per task · **Deadline:** before the next class

---

## Task 1.1: Your AI Career Intro

**File:** `code/lesson_01_intro.py`

**Client story:** A recruiter wants a one-screen introduction from every student in the course.

**Requirements**
1. Store in variables: your name, your dream AI role, one business problem AI could solve
2. Print each one using an f-string
3. Add one final line: why you chose that role

**Expected output (your text will differ)**
```text
Name: Ayesha Khan
Dream AI role: AI Automation Specialist
Problem I want to solve: A bakery takes WhatsApp orders by hand
Why: I want to help local businesses save time with AI.
```

**Checklist**
- [ ] Uses at least 3 variables
- [ ] Uses f-strings
- [ ] Runs with `uv run lesson_01_intro.py`

**Stretch:** add your city and print a final line like `Ayesha from Lahore is building the future with AI.`

---

## Task 1.2: Toolkit Proof

**Files:**
- `docs/setup-check.png` (screenshot)
- `docs/ollama-first-chat.md`
- `code/lesson_02_toolkit.py`

**Client story:** Before starting a project, a client asks: "Show me your setup works."

**Requirements**
1. Run all six version commands and take **one screenshot** of the results:
   ```bash
   uv --version
   uv run python --version
   code --version      # or: agy --version
   git --version
   ollama --version
   claude --version
   ```
2. In Ollama, ask: *"Explain Python in 2 lines for a beginner."* Paste the question, the answer and the model name into `docs/ollama-first-chat.md`
3. In `lesson_02_toolkit.py`, print your toolkit with **your own** versions:

**Expected output**
```text
My AI Dev Toolkit
-----------------
uv: 0.13.0
Python: 3.13.16
Editor: VS Code 1.139.1
Git: 2.56.0
Ollama: 0.40.3
Claude Code: 2.1.296
```

**Checklist**
- [ ] Screenshot shows all six tools working
- [ ] Ollama chat saved with the model name
- [ ] Script runs and shows your real versions

**Stretch:** in `ollama-first-chat.md`, add one line: was the answer correct? Would you show it to a client as is?

---

## Task 1.3: Client-Ready Repo

**Files:** whole project + `README.md`

**Client story:** A client will open your GitHub repo before hiring you. It must look professional in 10 seconds.

**Requirements**
1. Folder structure:
   ```text
   python-ai/
   ├── code/
   ├── notebooks/
   ├── docs/
   ├── .gitignore
   ├── .python-version
   ├── main.py
   ├── pyproject.toml
   ├── uv.lock
   └── README.md
   ```
2. `src/` removed, and `[project.scripts]` + `[build-system]` removed from `pyproject.toml`
3. `uv run main.py` and `uv run lesson_01_intro.py` (from `code/`) both still work
4. `README.md` contains:
   - Your name and course name
   - Your AI goal in one line
   - How to run: `uv run main.py`
   - A list of lessons done so far

**Checklist**
- [ ] `.venv/` is **not** on GitHub
- [ ] No `src/` folder
- [ ] README has a run command
- [ ] Both scripts still run

**Stretch:** add a `notebooks/.gitkeep` and `docs/.gitkeep` file so empty folders show on GitHub.

---

## Task 1.4: Business Prompt Builder

**File:** `code/lesson_04_print_input.py`

**Client story:** A digital agency wants a tiny tool: the user enters business details, and the tool creates a ready-to-use AI prompt.

**Requirements**
1. Docstring at the top describing the file
2. Ask the user for: their name, business type, and one problem the business faces
3. Print a welcome line
4. Build and print this prompt using an f-string:
   *"Suggest 3 AI solutions for a {business} that struggles with {problem}."*
5. At least 2 comments that explain **why**, not what

**Expected output**
```text
Your name: Bilal
Business type: bakery
Biggest problem: late delivery orders

Welcome, Bilal!
--- Your AI Prompt ---
Suggest 3 AI solutions for a bakery that struggles with late delivery orders.
```

**Checklist**
- [ ] Uses `input()` 3 times
- [ ] Prompt built with an f-string
- [ ] Docstring + 2 "why" comments
- [ ] Runs without errors

**Stretch:** ask for a monthly budget in PKR, convert it with `int()`, and add `Budget: {budget} PKR per month.` to the prompt. Then paste the prompt into Ollama and save the answer in `docs/prompt-test.md`.

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
