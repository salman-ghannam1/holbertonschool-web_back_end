# Python Async Functions

## 📌 Project Overview

This project introduces **asynchronous programming in Python** using the `asyncio` library.
The goal is to understand how to write non-blocking code, run concurrent tasks, and improve performance when dealing with I/O-bound operations.

---

## 🎯 Learning Objectives

By completing this project, you should be able to explain:

- The purpose of `async` and `await`
- How to execute asynchronous programs using `asyncio`
- The difference between coroutines and tasks
- How to run concurrent coroutines
- How to create and manage `asyncio` tasks
- How to measure runtime of async operations
- How to use the `random` module in async contexts

---

## 🧠 Key Concepts

### 1. Asynchronous Programming

Asynchronous programming allows multiple operations to run concurrently without blocking the execution flow.
It is especially useful for:

- Network requests
- File I/O
- APIs
- Distributed systems

---

### 2. Coroutines

A coroutine is a function defined using `async def`.
It does not execute immediately but returns a coroutine object.

```python
async def example():
    await something()
```

---

### 3. Event Loop

The event loop is responsible for:

- Scheduling tasks
- Running coroutines
- Managing execution flow

```python
import asyncio
asyncio.run(main())
```

---

### 4. Tasks

A Task is a wrapper around a coroutine that schedules its execution.

```python
task = asyncio.create_task(coroutine())
```

---

### 5. Concurrency vs Parallelism

- **Concurrency**: Tasks run in overlapping time
- **Parallelism**: Tasks run at the exact same time (multi-core)

This project focuses on concurrency.

---

## 📁 Project Structure

```
python_async_function/
│
├── 0-basic_async_syntax.py
├── 1-concurrent_coroutines.py
├── 2-measure_runtime.py
├── 3-tasks.py
├── 4-tasks.py
└── README.md
```

---

## 📚 Tasks Breakdown

### Task 0: The basics of async

- Create `wait_random`
- Wait for a random delay using `asyncio.sleep`
- Return the delay

---

### Task 1: Execute multiple coroutines

- Implement `wait_n`
- Run multiple coroutines concurrently
- Return results in ascending order using `asyncio.as_completed`

---

### Task 2: Measure runtime

- Implement `measure_time`
- Measure total execution time of `wait_n`
- Return average time per coroutine

---

### Task 3: Tasks

- Implement `task_wait_random`
- Return an `asyncio.Task` instead of a coroutine

---

### Task 4: Tasks with concurrency

- Implement `task_wait_n`
- Similar to `wait_n` but uses tasks instead of coroutines

---

## ⚙️ Requirements

- Python 3.9 (Ubuntu 20.04 LTS)
- All files must be executable
- Code must follow `pycodestyle` (v2.5.x)
- All functions must be type-annotated
- All modules and functions must include proper documentation
- First line of every file must be:

```bash
#!/usr/bin/env python3
```

---

## 🧪 Example Usage

```python
import asyncio
from 1-concurrent_coroutines import wait_n

print(asyncio.run(wait_n(5, 5)))
```

---

## 🚀 Performance Insight

Using async execution:

- Total runtime ≈ max delay
- Instead of sum of delays

This significantly improves performance in real-world systems.

---

## 📌 Real-World Applications

- Web APIs (FastAPI, aiohttp)
- Microservices
- Data pipelines
- Event-driven architectures
- Distributed systems

---

## 👨‍💻 Author

This project is part of the Holberton School curriculum for backend engineering.

---
