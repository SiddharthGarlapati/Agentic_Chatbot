# 🤖 Agentic AI Chatbot

An **Agentic AI Chatbot application** built using **LangGraph, LangChain, and Streamlit**, designed to demonstrate how **different AI use cases can be modeled as different execution graphs**.

Each use case constructs and runs its **own LangGraph**, enabling modular, scalable, and production-oriented agent workflows.

---

## 🚀 Overview

This application showcases how **agentic AI systems** can be designed by composing:
- LLM reasoning
- Tool usage
- Memory
- Conditional execution
- Multi-step workflows

Instead of a single monolithic chatbot, this app supports **multiple AI use cases**, each implemented as a **separate graph**.

---

## 🧠 Core Idea

> **Different AI problems require different reasoning flows.**  
> This project models each flow explicitly using **LangGraph**.

Examples:
- A basic conversational flow
- A tool-augmented reasoning flow
- A retrieval-based, task-specific flow

Each flow is:
- Independent
- Graph-driven
- Easy to extend or debug

---

## 🧩 Supported Use Cases

### 1️⃣ Basic Chatbot
- Simple conversational AI
- Direct interaction with an LLM
- Single-step reasoning
- No tools or external dependencies

**Graph characteristics**
- User → LLM → Response
- Stateless execution

---

### 2️⃣ Chatbot with Tools
- Agentic chatbot capable of calling external tools
- Dynamic tool selection
- Conditional branching based on LLM decisions

**Graph characteristics**
- User → Agent Node
- Conditional tool execution
- Tool → LLM feedback loop
- Controlled termination

---

### 3️⃣ AI News Explorer
- Task-specific agent for AI news summarization
- Uses external search tools
- Produces structured, summarized outputs
- Time-based query control (Daily / Weekly / Monthly)

**Graph characteristics**
- Trigger node (fetch news)
- Tool-based retrieval
- Summarization node
- Final response node

---


