"""Number Guessing Game - Week 1 project.

Concepts used: variables, input/output, conditionals, loops,
dictionaries, the random module, and basic input validation.
"""

import random

DIFFICULTIES = {
    "easy": {"low": 1, "high": 20, "attempts": 8},
    "medium": {"low": 1, "high": 50, "attempts": 6},
    "hard": {"low": 1, "high": 100, "attempts": 5},
}


def choose_difficulty() -> dict:
    """Ask the player to pick a difficulty until the input is valid."""
    while True:
        choice = input("Choose difficulty (easy/medium/hard): ").strip().lower()
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]
        print("Invalid choice. Please try again.")


def ask_guess(low: int, high: int) -> int:
    """Keep asking until the player enters an integer in range."""
    while True:
        raw = input(f"Your guess ({low}-{high}): ").strip()
        if not raw.lstrip("-").isdigit():
            print("Please enter a whole number.")
            continue
        guess = int(raw)
        if not low <= guess <= high:
            print(f"Number must be between {low} and {high}.")
            continue
        return guess


def play_round() -> bool:
    """Play one round. Returns True if the player wins."""
    settings = choose_difficulty()
    low, high, attempts = settings["low"], settings["high"], settings["attempts"]
    secret = random.randint(low, high)

    print(f"\nI'm thinking of a number between {low} and {high}.")
    print(f"You have {attempts} attempts.\n")

    for attempt in range(1, attempts + 1):
        guess = ask_guess(low, high)
        if guess == secret:
            print(f"🎉 Correct! You got it in {attempt} attempt(s).")
            return True
        hint = "higher" if guess < secret else "lower"
        remaining = attempts - attempt
        print(f"Try {hint}. Attempts left: {remaining}")

    print(f"Out of attempts. The number was {secret}.")
    return False


def main() -> None:
    wins = games = 0
    print("=== Number Guessing Game ===")
    while True:
        games += 1
        if play_round():
            wins += 1
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            break
    print(f"\nThanks for playing! Score: {wins}/{games} wins.")


if __name__ == "__main__":
    main()
