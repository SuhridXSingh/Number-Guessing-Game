# Number Guessing Game 🔢

An interactive command-line game where the user tries to guess a secret number chosen by the computer within a given range.

## Features

-   The computer generates a random secret number at the start of the game.
-   The user is prompted to enter their guess.
-   The program provides "higher" or "lower" hints to guide the user.
-   The game ends when the user correctly guesses the number.

---

## How to Run

1.  Clone the repository.
2.  Navigate to the project directory in your terminal.
3.  Run the script with the command:
    ```shell
    python number_guesser.py
    ```

---

## Concepts Learned

-   **User Input & Type Conversion:** Capturing user input and converting it from a string to an integer with `int(input())`.
-   **Looping:** Using a `while` loop to continue the game until the correct number is guessed.
-   **Random Number Generation:** Using `random.randint()` to create the secret number.
-   **Conditional Logic:** Implementing the "higher/lower" hints with `if/elif/else` statements.
