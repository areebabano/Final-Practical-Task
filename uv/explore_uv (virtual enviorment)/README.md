# UV Project Setup and Usage Guide

Welcome to the **UV Project** guide! This README will walk you through everything you need to know to create, setup, and run Python projects using the `uv` tool and Visual Studio Code (VS Code).

---

## What is `uv`?

`uv` is a powerful CLI tool designed to help you manage Python projects with ease. It offers commands to:

- Initialize new projects with best practices
- Create and manage virtual environments
- Run your Python packages easily
- And much more
---

## Prerequisites

Before you begin, make sure you have:

- Python installed (preferably Python 3.7+)
- VS Code installed
- `uv` installed (installation instructions below)

---

## Installation of `uv`

You can install the `uv` CLI tool using pip:

pip install uv

To verify installation and check the version:

uv version

This will display the currently installed version of `uv`.

---

## Step 1: Initialize a New UV Project

Create a new Python project with `uv` using the following command:

uv init --package explore-uv

- This command creates a project folder named `explore-uv`.
- It sets up the project structure with your source code inside a `src` directory.
- This structure follows Python packaging best practices.

---

## Step 2: Navigate to Your Project Directory

Move into your project directory:

cd explore-uv

---

## Step 3: Open Project in VS Code

Open the current directory in VS Code using:

code .

Alternatively, you can open VS Code and manually open the `explore-uv` folder.

---

## Step 4: Create a Virtual Environment

To isolate your project dependencies and avoid conflicts, create a virtual environment:

uv venv

This command creates a `.venv` directory inside your project, which contains the virtual environment.

---

## Step 5: Activate the Virtual Environment

Activate the virtual environment before installing packages or running your code.

- On macOS/Linux:

source .venv/bin/activate

- On Windows:

.venv\Scripts\activate

Once activated, your terminal prompt will usually change to show that you are inside the virtual environment.

---

## Step 6: Select Python Interpreter in VS Code

VS Code needs to know which Python interpreter to use:

1. Open the command palette in VS Code (Ctrl + Shift + P or Cmd + Shift + P on Mac).
2. Search for and select Python: Select Interpreter.
3. Choose the interpreter located inside your virtual environment:
   - Example: ./.venv/bin/python (macOS/Linux)
   - Or .\.venv\Scripts\python.exe (Windows)

This ensures that VS Code runs your code with the virtual environment's Python and packages.

---

## Step 7: Run Your Project

You can run your Python package using:

uv run explore-uv

This command executes the main package inside the `src` folder.

---

## Additional Helpful `uv` Commands

- Get help and see available commands:

uv help

- Check the version of `uv`:

uv version

- Deactivate virtual environment:

deactivate

---

## Summary

| Task                          | Command                           |
|------------------------------ |---------------------------------- |
| Install `uv`                  | pip install uv                    |
| Check `uv` version            | uv version                        |
| Create new project            | uv init --package explore-uv      |
| Change directory              | cd explore-uv                     |
| Open VS Code                  | code .                            |
| Create virtual environment    | uv venv                           |
| Activate virtual environment  | source .venv/bin/activate (Mac/Linux) or .venv\Scripts\activate (Windows) |
| Select Python interpreter in VS Code    | Use command palette -> Python: Select Interpreter -> Choose `.venv` interpreter |
| Run project                             | uv run explore-uv                 |

---

## Troubleshooting Tips

- If `code .` is not working, make sure you have VS Code command line tools installed. On VS Code, press Ctrl+Shift+P and search for Shell Command: Install 'code' command in  PATH.
- If your virtual environment is not activating, ensure that `.venv` folder exists and that you are running the activation command correctly for your OS.
- Always select the correct Python interpreter in VS Code to avoid confusion with system Python.
- Use `uv help` anytime to see what commands are available with the `uv` tool.

---

## Learn More

For more advanced usage and features, refer to the official `uv` documentation or run:

uv help

---

😊Happy coding with **UV** and Python! 🚀
