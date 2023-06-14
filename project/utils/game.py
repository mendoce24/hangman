import random

class Hangman:
    """Class to administrate the game Hangman"""

    def __init__(self):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = []
        self.lives = 5
        self.correctly_guessed_letters = ["_"]
        self.wrongly_guessed_letters = []
        self.turn_count  = 0
        self.error_count = 0

    def play(self):
        """method that asks the player to enter a letter."""
        
        #valid that the character is a letter
        while True : 
            letter = input("Enter a letter, please: ")
            if letter.isalpha():
                break
            print("Enter a valid letter, please!")

        # If the player guessed a letter well, add it to the correctly_guessed_letters list. If not, add it to the wrongly_guessed_letters list and add 1 to error_count. 
        self.turn_count += 1

        if letter in self.word_to_find :
            indexes_val = self.indexes(self.word_to_find, letter)
            for i in indexes_val: 
                self.correctly_guessed_letters[i]=letter
        else:
            self.wrongly_guessed_letters.append(letter)
            self.error_count += 1
    
    def game_over(self):
        """method that will stop the game and print game over...."""
        print("game over!")

    def well_played(self):
        """method that will print You found the word: {word_to_find_here} in {turn_count_here} turns with {error_count_here} errors!."""
        print(f"You found the word: '{''.join(self.word_to_find)}' in {self.turn_count} turns with {self.error_count} errors!.")

    def indexes(self, iterable, obj):
        """Get the index or indexes of object in a list"""
        result = []
        for index, elem in enumerate(iterable):
            if elem == obj:
                result.append(index)
        return result

    def start_game(self):
        """will print correctly_guessed_letters, bad_guessed_letters, life, error_count and turn_count at the end of each turn."""

        #Get one word to guess from a list
        self.word_to_find = list(random.choice(self.possible_words))
        self.correctly_guessed_letters *= len(self.word_to_find)

        print("try to guess this word: ", " ".join(self.correctly_guessed_letters))

        while self.error_count < self.lives :
            self.play()
            print(f"\nPlay : {' '.join(self.correctly_guessed_letters)} \n Wrong letters: {', '.join(self.wrongly_guessed_letters)} \n Lives: {self.lives - self.error_count} \n Error: {self.error_count} \n Turn: {self.turn_count}")

            if not ("_" in self.correctly_guessed_letters):
                self.well_played()
                break
            elif self.error_count == self.lives:
                self.game_over()
    

