# Sample Logging Project

The standard Python [logging](https://docs.python.org/3/library/logging.html) library is used widely to log various types of information in python programs for loging errors, debugging and displaying warning messages.

This simple demo shows how I use this library, instead of reinventing the wheel, to log information from a running program in a file with a custom name, location, and format.

A simple Q&A game, which I named `busybody`, is instantiated and run in `main.py`.  A random set of questions is posed and answers collected and logged. Each time the game is run, the log file is overwritten.

The directory structure for the root project:
```bash
tree
.
├── README.md
├── busybody.log		# generated log file from running a Game instance
├── game.py			# houses a Python class, Game
├── logger.py			# houses a Python class, Logger
├── main.py			# instantiation and execution of Game class
├── poetry.lock			# generated poetry dependency file
├── poetry.toml			# poetry configuration file
└── pyproject.toml		# poetry dependency file
```

# Development Environment
This project uses 
- [poetry](https://python-poetry.org/)
- [pyenv](https://github.com/pyenv/pyenv)
- [python](https://www.python.org/) `3.11.1`

to manage dependencies and create a virtual environment. 

# Testing
To run this program, type `python main.py` in the terminal.
