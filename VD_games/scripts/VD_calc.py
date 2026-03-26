#!/usr/bin/env python
from VD_games.engine import run_game
from VD_games.games.calc import get_question_and_answer, get_game_description


def main():
    run_game(get_question_and_answer, get_game_description())


if __name__ == "__main__":
    main()
