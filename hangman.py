import sys
import random
from rich.console import Console
from rich.panel import Panel

class HangmanGame:
    HANGMAN_PICS = [
        """
         ------
         |    |
         |    
         |   
         |    
         |   
        ---""",
        """
         ------
         |    |
         |    O
         |   
         |    
         |   
        ---""",
        """
         ------
         |    |
         |    O
         |    |
         |    
         |   
        ---""",
        """
         ------
         |    |
         |    O
         |   /|
         |    
         |   
        ---""",
        """
         ------
         |    |
         |    O
         |   /|\\
         |    
         |   
        ---""",
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / 
         |   
        ---""",
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |   
        ---"""
    ]

    def __init__(self):
        self.console = Console()
        self.words = ["python", "java", "abdul-basit", "javascript"]
        self.word = random.choice(self.words)
        self.guessed_letters = set()
        self.attempts = len(self.HANGMAN_PICS) - 1

    def display_progress(self):
        return " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])

    def print_hangman(self):
        self.console.print(Panel(self.HANGMAN_PICS[len(self.HANGMAN_PICS) - self.attempts - 1], title="Hangman Progress"))

    def get_user_input(self):
        try:
            return input("Guess a letter: ").strip().lower()
        except (OSError, EOFError):
            self.console.print("[bold red]Error: Input is not available![/bold red]")
            sys.exit(1)

    def play(self):
        self.console.print(Panel("[bold cyan]Welcome to Hangman![/bold cyan]", style="bold magenta"))
        
        while self.attempts > 0:
            self.print_hangman()
            self.console.print(f"\n[bold yellow]Word:[/bold yellow] {self.display_progress()}")
            guess = self.get_user_input()

            if len(guess) != 1 or not guess.isalpha():
                self.console.print("[bold red]Invalid input! Please enter a single letter.[/bold red]")
                continue

            if guess in self.guessed_letters:
                self.console.print("[bold yellow]You already guessed that letter![/bold yellow]")
                continue

            self.guessed_letters.add(guess)

            if guess in self.word:
                self.console.print("[bold green]Good job! The letter is in the word.[/bold green]")
            else:
                self.attempts -= 1
                self.console.print(f"[bold red]Wrong guess! You have {self.attempts} attempts left.[/bold red]")

            if all(letter in self.guessed_letters for letter in self.word):
                self.console.print(f"[bold green]🎉 Congratulations! You guessed the word: {self.word}[/bold green]")
                return

        self.console.print(f"[bold red]😢 Game over! The word was: {self.word}[/bold red]")

if __name__ == "__main__":
    game = HangmanGame()
    game.play()
