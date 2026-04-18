# holbertonschool-web_back_end

Python Type Annotations Project
📌 Description
This project focuses on understanding and applying type annotations in Python 3.
It demonstrates how to write clean, readable, and maintainable code by specifying variable types and function signatures.
The project also introduces duck typing and the use of mypy for static type checking.

🎯 Learning Objectives
By completing this project, you will be able to:
•
Understand and use type annotations in Python 3
•
Define function signatures with proper types
•
Apply the concept of duck typing
•
Validate Python code using mypy
•
Write well-documented and structured Python modules

🛠️ Requirements
•
Python 3.9
•
Ubuntu 20.04 LTS
•
Code editor (vi, vim, or emacs)
•
pycodestyle (version 2.5)
•
mypy (for type checking)

📂 Project Structure
Each Python file in this project:
•
Starts with:
#!/usr/bin/env python3
•
Ends with a new line
•
Is executable
•
Contains proper documentation (docstrings):
•
Module level

✍️ Example
Basic Type Annotation
def add(a: float, b: float) -> float:
"""Returns the sum of two floating-point numbers."""
return a + b

🦆 Duck Typing
Python follows a flexible typing system:
"If it behaves like a duck, it is a duck."
Example:
def get_length(obj):
return len(obj)
This function works with any object that supports len().

🔍 Type Checking with mypy
To check your code:
mypy your_file.py
Example error:
add("hello", 5) # Invalid: string instead of float

📏 Code Style
All code must follow pycodestyle (v2.5):
pycodestyle your_file.py

📚 Documentation
Every module, class, and function must include a clear and meaningful docstring.
Example:
"""This module provides basic mathematical operations."""

🚀 Conclusion
This project builds a strong foundation for writing clean, typed, and maintainable Python code, preparing you for real-world software development and large-scale projects.
