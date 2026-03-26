#!/usr/bin/env python
import random


def generate_progression():
    length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(1, 10)

    progression = []
    for i in range(length):
        progression.append(start + i * step)

    hidden_index = random.randint(0, length - 1)
    hidden_value = progression[hidden_index]

    question_parts = []
    for i, num in enumerate(progression):
        if i == hidden_index:
            question_parts.append("..")
        else:
            question_parts.append(str(num))

    question = " ".join(question_parts)
    correct_answer = str(hidden_value)

    return question, correct_answer


def get_question_and_answer():
    return generate_progression()


def get_game_description():
    return "What number is missing in the progression?"
