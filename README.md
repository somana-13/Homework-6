# Calculator Application - Homework 5

## Overview

This project is an interactive command-line calculator application built using the Command Pattern and Plugin Architecture. It enhances the previous calculator implementation by transforming it from a single-execution script into a fully interactive application using REPL (Read, Evaluate, Print, Loop) principles.

## Features

- Interactive command-line interface with REPL functionality
- Implementation of the Command Pattern for calculator operations
- Plugin Architecture to dynamically load commands
- Core calculator operations: add, subtract, multiply, divide
- Menu command to display available commands
- Extensible design for adding new commands via plugins

## Project Structure

```
./calculator_app/
├── calculator/           # Core calculator functionality
├── commands/             # Command pattern implementation
├── plugins/              # Plugin architecture
├── tests/                # Unit tests
├── calculator_app.py     # Main application with REPL interface
└── requirements.txt      # Project dependencies
```

## Setup and Installation

1. Clone the repository
2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To start the calculator application, run:

```
python calculator_app.py
```

This will launch the interactive REPL interface where you can enter commands.

## Available Commands

- `add <num1> <num2> [num3 ...]` - Add two or more numbers
- `subtract <num1> <num2> [num3 ...]` - Subtract numbers from the first number
- `multiply <num1> <num2> [num3 ...]` - Multiply two or more numbers
- `divide <num1> <num2> [num3 ...]` - Divide the first number by subsequent numbers
- `menu` - Display available commands and usage information
- `exit` or `quit` - Exit the application

## Creating Plugins

To create a new command plugin:

1. Create a new Python file in the `plugins` directory
2. Define a class that inherits from `Command` (from `commands.command_interface`)
3. Implement the required methods: `execute()`, `description` property, and `usage` property
4. The plugin will be automatically loaded when the application starts

Example plugin template:

```python
from commands.command_interface import Command

class MyCustomCommand(Command):
    def execute(self, *args, **kwargs):
        # Implement your command logic here
        return result
    
    @property
    def description(self):
        return "Description of what your command does"
    
    @property
    def usage(self):
        return "mycommand <arg1> <arg2>"
```

## Running Tests

To run all tests with coverage:

```
python -m pytest --cov
```

To run specific test files:

```
python -m pytest tests/test_calculator_app.py
```

For linting:

```
python -m pytest --pylint
```
