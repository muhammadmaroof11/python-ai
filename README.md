# Python for AI

**Student:** Muhammad Maroof  
**Course:** Python for AI (The School of AI) — Module 1: Python Basics for GenAI and Agentic AI  
**Goal:** Building intelligent, reliable AI agents and automation workflows to solve real-world business challenges.

---

## Getting Started

### Prerequisites
- [uv](https://docs.astral.sh/uv/) package manager
- Python 3.13+
- [Git](https://git-scm.com/)
- [Ollama](https://ollama.com/) (with `llama3.2` model installed)

### Setup & Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/muhammadmaroof11/python-ai.git
   cd python-ai
   ```
2. **Synchronize environment dependencies:**
   ```bash
   uv sync
   ```
3. **Run the entry point:**
   ```bash
   uv run main.py
   ```

### Running Lesson Scripts
Any script in the `code/` directory can be executed with `uv run`:
```bash
cd code
uv run lesson_08_mini_chatbot.py
```

---

## Lessons Completed (Module 1)

- [x] **Lesson 1.1: AI Career Intro** (`code/lesson_01_intro.py`)  
  *Core Python syntax, f-strings, and career introduction.*
- [x] **Lesson 1.2: Toolkit Proof** (`code/lesson_02_toolkit.py`, `docs/setup-check.png`, `docs/ollama-first-chat.md`)  
  *Development environment verification across Python, uv, Git, Ollama, VS Code, and Claude Code.*
- [x] **Lesson 1.3: Client-Ready Repo** (`main.py`, `pyproject.toml`, `uv.lock`)  
  *Clean repository architecture, uv-managed project setup, and version pinning.*
- [x] **Lesson 1.4: Business Prompt Builder** (`code/lesson_04_print_input.py`, `docs/prompt-test.md`)  
  *Interactive prompt engineering with user inputs and Ollama testing under budget constraints.*
- [x] **Lesson 1.5: AI Model Profile Card** (`code/lesson_05_variables.py`)  
  *Primitive data types (str, int, float, bool), type inspection, and per-chat / monthly cost modeling.*
- [x] **Lesson 1.6: Prompt Cleaner & Token Sanitizer** (`code/lesson_06_strings_prompts.py`)  
  *Defensive string manipulation (.strip, .title, .capitalize), substring checks, and token slicing limits.*
- [x] **Lesson 1.7: Smart Model Router** (`code/lesson_07_conditions.py`)  
  *Conditional task dispatching (private local vs cloud code vs general chat) with token usage thresholds.*
- [x] **Lesson 1.8: Business Helper Bot** (`code/lesson_08_mini_chatbot.py`)  
  *Stateful while loops, priority complaint triage, human handoff, and fallback telemetry.*

---

## Task 1.8: Chatbot Intent Design Table

**Business:** City Care Clinic  
**Assistant:** City Care Bot

| Intent | What User Wants | Keywords to Look For | Bot Response |
|---|---|---|---|
| **Complaint / Escalation** | Report a delay, medical report issue, or service concern | `refund`, `complaint`, `late`, `bad` | *"Sorry about that. The clinic manager will call you today to resolve this."* |
| **Timings / Hours** | Inquire about clinic opening and closing hours | `timing`, `hour`, `open`, `time` | *"We are open 10 am to 8 pm, Monday to Saturday."* |
| **Fees / Pricing** | Check charges for general and specialist doctor visits | `fee`, `cost`, `price`, `how much` | *"General consultation fee is 2,000 PKR. Specialist consultations start at 3,500 PKR."* |
| **Location / Address** | Find physical clinic address and directions | `where`, `location`, `address` | *"We are located at 45 Medical Complex, Jail Road, Lahore."* |
| **Appointments** | Schedule or book a doctor appointment | `appointment`, `book` | *"To book an appointment, call (042) 3578-9000 or reply with your preferred day."* |
| **Greeting** | Initiate conversation or say hello | `hi`, `hello`, `hey`, `salam` | *"Hello again, {name}! How can I help you today?"* |
| **Human Handover (Stretch)** | Request immediate live staff support | `agent`, `human` | *"Connecting you to a human support agent right away. Please hold..."* |
| **Exit** | End the interaction | `bye`, `exit` | *"Take care, {name}! Wishing you good health."* (displays message & complaint metrics) |
| **Fallback** | Unrecognized clinical inquiry or question | *(No keyword match)* | Increments unanswered counter and synthesizes Module 2 LLM prompt template. |

---

## Repository Structure

```text
python-ai/
├── code/                         # Lesson scripts and project code
│   ├── lesson_01_intro.py
│   ├── lesson_02_toolkit.py
│   ├── lesson_04_print_input.py
│   ├── lesson_05_variables.py
│   ├── lesson_06_strings_prompts.py
│   ├── lesson_07_conditions.py
│   └── lesson_08_mini_chatbot.py
├── docs/                         # Notes, screenshots, test results, lesson guides
│   ├── 01-python-basics/         # Lessons 1.1 to 1.8
│   ├── 02-talk-to-ai/            # Lessons 2.1 to 2.8
│   ├── assessments/              # Checkpoints 1 & 2 task briefs
│   ├── setup-check.png           # Environment verification screenshot
│   ├── ollama-first-chat.md      # Task 1.2 Ollama chat & reflection
│   └── prompt-test.md            # Task 1.4 Ollama response test
├── notebooks/                    # Jupyter notebooks (.gitkeep)
├── .gitignore                    # Ignores .venv/ and compilation caches
├── .python-version               # Python 3.13 pin
├── main.py                       # Project entry point
├── pyproject.toml                # uv project configuration
├── uv.lock                       # Pinned dependency lockfile
└── README.md                     # Project overview and portfolio documentation
```
