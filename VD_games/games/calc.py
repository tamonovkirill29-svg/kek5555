#!/usr/bin/env python
import random


OPERATIONS = [
    ("+", lambda a, b: a + b),
    ("-", lambda a, b: a - b),
    ("*", lambda a, b: a * b),
]


def get_question_and_answer():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operation, func = random.choice(OPERATIONS)
    question = f"{num1} {operation} {num2}"
    correct_answer = str(func(num1, num2))
    return question, correct_answer


def get_game_description():
    return "What is the result of the expression?"
