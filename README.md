# Sample Logging Project

The standard Python [logging](https://docs.python.org/3/library/logging.html) library is used widely in python programs for logging errors, displaying warning messages and debugging.

This simple demo shows how I use this library, instead of reinventing the wheel, to log information in a file with a custom name, location, and format from a running program.

A simple Q&A game, which I named `busybody`, is instantiated and run in `main.py`.  A random set of questions is posed and answers collected and logged. Each time the game is run, the log file is overwritten.

The directory structure for the root project:
```bash
tree
.
├── README.md
├── busybody.py			# houses the busybody game
├── logger.py			# houses the Logger class
├── logs
│   ├── busybody.log		# generated by the Logger object
│   └── tictactoe.log		# generated by the Logger object
├── main.py			# main python execution module
├── poetry.lock			# generated poetry dependency file
├── poetry.toml			# poetry configuration file
└── pyproject.toml		# poetry dependency file
└── tictactoe.py		# houses the tictactoe game
```

# Development Environment
This project uses 
- [poetry](https://python-poetry.org/)
- [pyenv](https://github.com/pyenv/pyenv)
- [python](https://www.python.org/) version greater than `3.8.1`

to manage dependencies and create a virtual environment. 

# Testing
To run this program, type `python main.py` in the terminal.

# Sample Game Session
```bash
$ python main.py
1 Busybody
2 TicTacToe
q quit
Pick a game: 2
1 2 3
4 5 6
7 8 9
Type q to quit or Enter a number: 5
1 2 3
4 o 6
7 x 9
Type q to quit or Enter a number: 1
o 2 x
4 o 6
7 x 9
Type q to quit or Enter a number: 9
o 2 x
4 o 6
7 x o
You won!
1 Busybody
2 TicTacToe
q quit
Pick a game: 1
Type q to quit: What is your favorite season? summer
Type q to quit: Which day were you born? don't know
Type q to quit: What is your favorite food? lasagna
Type q to quit: What is your favorite sport? skiing
Type q to quit: Where do you work? remote
Type q to quit: What is your Zodiac sign? secret
Type q to quit: Where do you live? usa
Type q to quit: How old are you? very old
Type q to quit: What is your name? anonymous
Type q to quit: Where do you go for vacation? moon
No more questions...
All done!
1 Busybody
2 TicTacToe
q quit
Pick a game: 2
1 2 3
4 5 6
7 8 9
Type q to quit or Enter a number: 5
1 2 3
4 x 6
7 8 o
Type q to quit or Enter a number: 7
1 2 3
o x 6
x 8 o
Type q to quit or Enter a number: 3
1 2 x
o x 6
x 8 o
You won!
1 Busybody
2 TicTacToe
q quit
Pick a game: q
Goodbye
```

# Sample Logged Output
```bash
$ cat logs/busybody.log
Type q to quit: What is your Zodiac sign?
scorpio
Type q to quit: Which day were you born?
not telling
Type q to quit: What is your favorite season?
spring
Type q to quit: Where do you go for vacation?
Israel
Type q to quit: What is your name?

Type q to quit: How old are you?

Type q to quit: Where do you work?
kevala
Type q to quit: Where do you live?
usa
Type q to quit: What is your favorite food?
curry
Type q to quit: What is your favorite sport?
tennis
```

```bash
$ cat logs/tictactoe.log
1 2 3
4 5 6
7 8 9

You are o
1 2 3
4 o 6
7 x 9

You are o
o 2 x
4 o 6
7 x 9

You are o
o 2 x
4 o 6
7 x o

You won!
1 2 3
4 5 6
7 8 9

You are x
1 2 3
4 x 6
7 8 o

You are x
1 2 3
o x 6
x 8 o

You are x
1 2 x
o x 6
x 8 o

You won!
```
