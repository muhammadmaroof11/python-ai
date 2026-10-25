# Module 1, Checkpoint 2: Quick Checks (Lessons 1.5 to 1.8)

**Course:** Python for AI · **Module 1:** Python Basics for GenAI and Agentic AI · **Updated:** Oct 2026

> **Student version.** Answer on your own first, without AI tools or notes. The goal is to find what you have not understood yet, not to get full marks.

**Format per lesson:** 5 MCQs + 1 "Predict the Output" · **Time:** 5 minutes · **Marks:** 6 per lesson

**How to answer:** add your answers to `docs/my-answers-module-1.md` like this:

```text
1.5: Q1 ?, Q2 ?, Q3 ?, Q4 ?, Q5 ?, Q6 (your predicted output)
```

**Predict the Output rule:** write your answer **before** running the code. Then run it with `uv run` and check yourself.

---

## Lesson 1.5: Variables and Data Types

**Q1.** What is the type of `max_tokens` after `max_tokens = 500.0`?
- a) int
- b) float
- c) str
- d) bool

**Q2.** What does `int(7.99)` return?
- a) 8
- b) 7
- c) 7.99
- d) ValueError

**Q3.** Which is a valid variable name?
- a) `1st_prompt`
- b) `user-name`
- c) `user_name_2`
- d) `class name`

**Q4.** What does `bool("0")` return?
- a) False
- b) True
- c) 0
- d) TypeError

**Q5.** The user types `50` into `chats = input("Chats per day: ")`. Why does `chats + 10` crash with a `TypeError`?
- a) Python cannot add numbers
- b) `input()` returns text, and text cannot be added to a number
- c) `chats` is a float
- d) `+` only works with lists

**Q6. Predict the Output**
```python
price = 2.5
qty = "4"
total = price * int(qty)
print(total)
```

---

## Lesson 1.6: Working with Text (Strings)

**Q1.** What does `"Sweet Crumbs"[0:5]` return?
- a) `"Swee"`
- b) `"Sweet"`
- c) `"Sweet "`
- d) `"weet "`

**Q2.** `text = "Lahore"`. What is `text[-2]`?
- a) `"e"`
- b) `"r"`
- c) `"L"`
- d) IndexError

**Q3.** Which turns `"  ayesha KHAN "` into `"Ayesha Khan"`?
- a) `.strip().lower()`
- b) `.strip().title()`
- c) `.title()`
- d) `.capitalize()`

**Q4.** What does this print?
```python
city = "lahore"
city.title()
print(city)
```
- a) `Lahore`
- b) `lahore`
- c) `LAHORE`
- d) Error

**Q5.** `message = "Do you have SUGAR-FREE cake?"`. Which check correctly finds "sugar-free"?
- a) `"sugar-free" in message`
- b) `"sugar-free" in message.lower()`
- c) `message == "sugar-free"`
- d) `message.endswith("sugar-free")`

**Q6. Predict the Output**
```python
bill = 98765.4321
chats = 2500000
print(f"{bill:.1f} PKR for {chats:,} chats")
```

---

## Lesson 1.7: Operators and Making Decisions

**Q1.** What does `23 // 4` give?
- a) 5.75
- b) 5
- c) 6
- d) 3

**Q2.** What does `23 % 4` give?
- a) 5
- b) 3
- c) 0.75
- d) 1

**Q3.** Which line checks that `plan` is **not** `"free"`?
- a) `if plan = "free":`
- b) `if plan != "free":`
- c) `if plan == not "free":`
- d) `if not plan = "free":`

**Q4.** The code says `if city == "Lahore" or "Karachi":` and the user's city is `"Multan"`. What happens?
- a) The condition is False, because Multan is neither city
- b) The condition is True, because `"Karachi"` on its own is a non-empty string
- c) Python raises an error
- d) Python asks the user again

**Q5.** What does this print?
```python
tokens = 3500
if tokens > 1000:
    print("Medium")
elif tokens > 3000:
    print("Long")
else:
    print("Short")
```
- a) `Medium`
- b) `Long`
- c) `Medium` and `Long`
- d) `Short`

**Q6. Predict the Output**
```python
is_paid = False
tokens = 2500
if not is_paid and tokens > 2000:
    print("Upgrade")
elif tokens > 2000:
    print("Long request")
else:
    print("OK")
```

---

## Lesson 1.8: Mini Project: Rule-Based Chatbot

**Q1.** You delete the `break` line from the `bye` rule. The user types `bye`. What happens?
- a) The program ends normally
- b) The bot says goodbye, then asks for the next message again
- c) SyntaxError
- d) Python closes the terminal

**Q2.** Your bot has `if message == "bye": break`, but typing `Bye ` does not stop it. What is the most likely cause?
- a) `break` is spelled wrong
- b) The message was not cleaned with `.strip().lower()`
- c) `while True` should be `while False`
- d) The bot needs more `elif` rules

**Q3.** The complaint rule is `elif "late" in message:`. A customer types `do you have chocolate cake?`. What happens, and why?
- a) The price rule answers, because "cake" is a product
- b) The complaint rule fires, because "late" hides inside "chocolate"
- c) Python raises an error
- d) The fallback answers, because no rule matches

**Q4.** The rules are in this order. A customer types `i want a refund, the price was wrong`. Which reply prints, and what should change?
```python
if "price" in message:
    print("Cakes start at 1,500 PKR.")
elif "refund" in message:
    print("A manager will call you.")
```
- a) The price reply; move the refund rule first
- b) The manager reply; nothing needs to change
- c) Both replies print
- d) Nothing prints

**Q5.** Where should `count = 0` go in a chatbot that counts messages?
- a) Inside the loop, as the first line
- b) Once, **before** the loop
- c) After `break`
- d) Inside the `else` block

**Q6. Predict the Output**
The user types `HOURS?`, then `where are you`, then `  Bye`.
```python
count = 0
unanswered = 0
while True:
    text = input("You: ").strip().lower()
    count += 1
    if text == "bye":
        break
    elif "hour" in text:
        print("Open 9 to 5")
    else:
        unanswered += 1
print(f"{count} messages, {unanswered} unanswered")
```
What is the last line printed?

---

## After the Check

- Answers are discussed in the **next class warm-up**.
- Got a question wrong? Re-read that lesson's section in `docs/` and redo its Code Task.
- Commit your answers file: `git commit -m "Module 1 quick checks part 2"`

**Self-score guide**

| Score (per lesson) | Meaning |
|---|---|
| 6 | Mastered, move on |
| 4 to 5 | Good, review what you missed |
| 0 to 3 | Re-read the lesson and ask in class |
