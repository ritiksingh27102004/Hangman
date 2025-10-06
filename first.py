import random

def play_hangman():
    """
    This function runs a simple text-based Hangman game.
    """
    # --- 1. Game Setup ---
    # List of words for the game
    words = ["python", "java", "swift", "kotlin", "ruby"]
    
    # Randomly select a word from the list
    secret_word = random.choice(words)
    word_length = len(secret_word)
    
    # Player's state
    guesses_left = 6
    guessed_letters = []  # To keep track of letters already guessed
    
    # Create a list of underscores to represent the hidden word
    display = ["_"] * word_length
    
    print("--- Welcome to Hangman! 👋 ---")
    print(f"I'm thinking of a word that is {word_length} letters long.")
    print(f"You have {guesses_left} incorrect guesses.")

    # --- 2. Main Game Loop ---
    game_over = False
    while not game_over:
        
        print("\n" + "="*30)
        # Display the current state of the word (e.g., "_ p p _ _")
        print("Word: " + " ".join(display))
        
        # Get a guess from the player
        guess = input("Guess a letter: ").lower()

        # --- 3. Input Validation and Logic ---
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print(f"⚠ You've already guessed '{guess}'. Try another letter.")
            continue
        
        # Add the new guess to our list of guessed letters
        guessed_letters.append(guess)

        # Check if the guessed letter is in the secret word
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word. ✅")
            # Update the display list with the correctly guessed letter
            for i in range(word_length):
                if secret_word[i] == guess:
                    display[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word. ❌")
            # Decrement the number of guesses left
            guesses_left -= 1
            print(f"You have {guesses_left} incorrect guesses left.")

        # --- 4. Check for Win/Loss Condition ---
        # If there are no more underscores, the player has won
        if "_" not in display:
            print("\n🎉 Congratulations! You guessed the word correctly!")
            game_over = True
        
        # If the player has no guesses left, they have lost
        if guesses_left == 0:
            print("\n😭 Game Over! You ran out of guesses.")
            game_over = True

    # Reveal the secret word at the end of the game
    print(f"The secret word was: '{secret_word}'")

# --- Run the game ---
play_hangman()