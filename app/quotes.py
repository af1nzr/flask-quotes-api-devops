import random

quotes = [
    "Stay hungry, stay foolish. – Steve Jobs",
    "Talk is cheap. Show me the code. – Linus Torvalds",
    "Programs must be written for people to read. – Harold Abelson",
    "Simplicity is the soul of efficiency. – Austin Freeman",
    "Before software can be reusable it first has to be usable. – Ralph Johnson"
]

def get_random_quote():
    return random.choice(quotes)
