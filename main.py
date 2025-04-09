import random
import os
import time
from colorama import Fore, Style, init
from words import word_list

# Initialize colorama for colored terminal output
init(autoreset=True)

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_word():
    word = random.choice(word_list)
    return word.upper()

def display_logo():
    """Display an attractive logo at the beginning of the game."""
    clear_screen()
    logo = f"""{Fore.CYAN}
    ██   ██  █████  ███    ██  ██████  ███    ███  █████  ███    ██ 
    ██   ██ ██   ██ ████   ██ ██       ████  ████ ██   ██ ████   ██ 
    ███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██ 
    ██   ██ ██   ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██ 
    ██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████ 
    {Style.RESET_ALL}
    """
    print(logo)
    print(f"{Fore.YELLOW}=" * 70)
    print(f"{Fore.WHITE}Can you guess the word before the hangman is complete?")
    print(f"{Fore.YELLOW}=" * 70)
    time.sleep(1)

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    
    display_logo()
    
    while not guessed and tries > 0:
        clear_screen()
        
        # Display game information header
        print(f"{Fore.CYAN}=" * 70)
        print(f"{Fore.WHITE}HANGMAN GAME - Remaining Attempts: {get_colored_attempts(tries)}")
        print(f"{Fore.CYAN}=" * 70)
        
        # Display the hangman
        print(display_hangman(tries))
        
        # Display current word state with colorful formatting
        print(f"\n{Fore.CYAN}Word: {Style.BRIGHT}", end="")
        for char in word_completion:
            if char == "_":
                print(f"{Fore.WHITE}{char} ", end="")
            else:
                print(f"{Fore.GREEN}{char} ", end="")
        print(Style.RESET_ALL)
        
        # Display guessed letters
        if guessed_letters:
            print(f"\n{Fore.YELLOW}Letters guessed: ", end="")
            for letter in sorted(guessed_letters):
                print(f"{letter} ", end="")
            print()
        
        # Display guessed words
        if guessed_words:
            print(f"{Fore.YELLOW}Words guessed: ", end="")
            for word in guessed_words:
                print(f"{word} ", end="")
            print()
        
        # Get player's guess
        print(f"\n{Fore.WHITE}Enter your guess:")
        guess = input("> ").upper()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                clear_screen()
                print(f"{Fore.YELLOW}You already guessed the letter {Fore.WHITE}{guess}")
                time.sleep(1)
            elif guess not in word:
                print(f"{Fore.RED}{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
                time.sleep(1)
            else:
                print(f"{Fore.GREEN}Good job! {Fore.WHITE}{guess} {Fore.GREEN}is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
                time.sleep(1)
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                clear_screen()
                print(f"{Fore.YELLOW}You already guessed the word {Fore.WHITE}{guess}")
                time.sleep(1)
            elif guess != word:
                print(f"{Fore.RED}{guess} is not the word.")
                tries -= 1
                guessed_words.append(guess)
                time.sleep(1)
            else:
                guessed = True
                word_completion = word
        else:
            clear_screen()
            print(f"{Fore.RED}Not a valid guess. Please enter a single letter or the full word.")
            time.sleep(1.5)
    
    # Game over screen
    clear_screen()
    print(display_hangman(tries))
    
    if guessed:
        display_win_message(word)
    else:
        display_lose_message(word)

def get_colored_attempts(tries):
    """Return colored text depending on the number of tries left."""
    if tries >= 5:
        return f"{Fore.GREEN}{tries}{Style.RESET_ALL}"
    elif tries >= 3:
        return f"{Fore.YELLOW}{tries}{Style.RESET_ALL}"
    else:
        return f"{Fore.RED}{tries}{Style.RESET_ALL}"

def display_win_message(word):
    """Display a victory message."""
    print(f"{Fore.GREEN}=" * 70)
    win_text = f"""
    {Fore.YELLOW}██    ██  ██████  ██    ██     ██     ██ ██ ███    ██ ██
    {Fore.YELLOW} ██  ██  ██    ██ ██    ██     ██     ██ ██ ████   ██ ██
    {Fore.YELLOW}  ████   ██    ██ ██    ██     ██  █  ██ ██ ██ ██  ██ ██
    {Fore.YELLOW}   ██    ██    ██ ██    ██     ██ ███ ██ ██ ██  ██ ██  
    {Fore.YELLOW}   ██     ██████   ██████       ███ ███  ██ ██   ████ ██
    """
    print(win_text)
    print(f"{Fore.GREEN}=" * 70)
    print(f"\n{Fore.WHITE}Congratulations! You guessed the word: {Fore.GREEN}{word}{Style.RESET_ALL}!")
    print(f"{Fore.GREEN}=" * 70)

def display_lose_message(word):
    """Display a defeat message."""
    print(f"{Fore.RED}=" * 70)
    lose_text = f"""
    {Fore.RED} ██████   █████  ███    ███ ███████      ██████  ██    ██ ███████ ██████  
    {Fore.RED}██       ██   ██ ████  ████ ██          ██    ██ ██    ██ ██      ██   ██ 
    {Fore.RED}██   ███ ███████ ██ ████ ██ █████       ██    ██ ██    ██ █████   ██████  
    {Fore.RED}██    ██ ██   ██ ██  ██  ██ ██          ██    ██  ██  ██  ██      ██   ██ 
    {Fore.RED} ██████  ██   ██ ██      ██ ███████      ██████    ████   ███████ ██   ██ 
    """
    print(lose_text)
    print(f"{Fore.RED}=" * 70)
    print(f"\n{Fore.WHITE}Oh no! You ran out of attempts.")
    print(f"The word was: {Fore.YELLOW}{word}{Style.RESET_ALL}")
    print(f"{Fore.RED}=" * 70)

def display_hangman(tries):
    stages = [
        # 0 tries left (final state: head, torso, both arms, and both legs)
        f"""{Fore.RED}
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
        """,
        # 1 try left
        f"""{Fore.RED}
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
        """,
        # 2 tries left
        f"""{Fore.YELLOW}
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
        """,
        # 3 tries left
        f"""{Fore.YELLOW}
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
        """,
        # 4 tries left
        f"""{Fore.GREEN}
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
        """,
        # 5 tries left
        f"""{Fore.GREEN}
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
        """,
        # 6 tries left (initial empty state)
        f"""{Fore.GREEN}
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
        """
    ]
    return stages[tries]

def main():
    while True:
        word = get_word()
        play(word)
        
        print(f"\n{Fore.CYAN}Would you like to play again? (Y/N)")
        if input("> ").upper() != "Y":
            break
    
    # Goodbye message
    clear_screen()
    print(f"{Fore.CYAN}=" * 70)
    print(f"{Fore.YELLOW}Thank you for playing Hangman! See you next time.")
    print(f"{Fore.CYAN}=" * 70)

if __name__ == "__main__":
    main()