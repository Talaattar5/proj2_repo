# proj2_repo
# AI Task Planner Agent

## Project Overview

This project was developed using **LangChain**, **Agents**, **LangGraph**, and **Flask**.

The application helps users manage their daily tasks by using AI to:
- Summarize tasks
- Classify tasks
- Prioritize tasks
- Generate a smart execution plan

---

# Technologies Used

- Python
- LangChain
- LangGraph
- OpenAI GPT-4o-mini
- Flask
- HTML
- CSS

---

# Project Structure

```
proj2_repo/
│
├── app.py
├── day2_langgraph.py
├── agent.py
├── count_agent.py
├── sample.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── .env
```

---

# Day 1 – LangChain

## 1. Single Chain

Created a simple summarization chain.

Workflow:

```
User Input
      ↓
 Prompt
      ↓
 ChatOpenAI
      ↓
 Summary
```

---

## 2. Sequential Chain

Built a multi-step workflow.

Steps:

1. Summarize the text
2. Count words
3. Classify the topic

---

# Day 2 – Agents

## Agent 1

Reads a text file and generates a summary.

Example:

```
sample.txt
      ↓
Agent
      ↓
Summary
```

---

## Agent 2

Reads a text file and counts how many times a specific word appears.

Example:

```
sample.txt
Word = education

↓

Result:
The word "education" appears 1 time.
```

---

# LangGraph

Built an AI Task Manager using multiple connected nodes.

Workflow:

```
START
   ↓
Summarize
   ↓
Classify
   ↓
Prioritize
   ↓
Smart Plan
   ↓
END
```

Each node performs one task:

### Summarize Node

Creates a short summary of the user's tasks.

### Classification Node

Classifies tasks into:

- Work
- Study
- Personal

### Priority Node

Assigns a priority:

- High
- Medium
- Low

### Smart Plan Node

Creates the best order for completing the tasks.

---

# Flask Application

Flask provides a simple web interface.

The user enters tasks through the browser.

The application displays:

- Original Task Input
- Summary
- Classification
- Priority
- Smart Plan

---

# Example

Input:

```
Finish the database project report before Thursday.
Study for the networking exam.
Buy groceries.
```

Output:

Summary

- Short summary of all tasks.

Classification

- Work
- Study
- Personal

Priority

- High
- Medium
- Low

Smart Plan

1. Finish database report
2. Study networking
3. Buy groceries

---

# What I Learned

- How LangChain chains work.
- How to build Sequential Chains.
- How AI Agents perform specialized tasks.
- How LangGraph connects multiple AI nodes.
- How state moves between graph nodes.
- How to build a Flask web application.
- How to connect AI models with a web interface.

---

# Future Improvements

- Add reminders.
- Save tasks in a database.
- User authentication.
- Calendar integration.
- Email notifications.
- Mobile-friendly interface.