from itertools import permutations
from collections import Counter

class CoundownGame:
    def __init__(self):
        self.rounds = 4

    def load_dictionary(self, file):
        """Load dictionary words using a set."""
        with open(file) as f:
            return set(f.read().split())
        
    def get_user_input(self, round_number, num_letters=6):
        """User prompt and validates input."""
        print(f"\nRound {round_number} ")

        while True:
            user_string = input(f"Input {num_letters} letters (vowels or consonants):\n")
            user_input = user_string.replace(" ", "").lower()

            if len(user_input) != num_letters:
                print(f"Enter exactly {num_letters} letters.")
                continue
            #Checks if all input are alphabet characters
            if not user_input.isalpha():
                print("Only alphabetical characters accepted.")
                continue

            return user_input


    def find_matching_words(self, letters, dictionary):
        """Find all words in the dictionary that can be made with the given letters."""

        #Count all the occurrences of each letter the user input
        letters_counter = Counter(letters)
        
        matching_words = []

        #Iterates through each word in the dictionary
        for word in dictionary:
            word_counter = Counter(word)
            valid = True

            # Check each letter in the word
            for char in word:
                # If the word uses more of a letter than the letters provided
                if word_counter[char] > letters_counter.get(char, 0):
                    valid = False
                    break

            if valid:
                matching_words.append(word)

        return matching_words

    def display_results(self, letters, matching_words):
        """Display letters and longest length matching words to the user."""
        print(f"Letters: {' '.join(letters.upper())}")

        if matching_words:
            #Checks for the lenght of the longest word which would be the score for the current round
            max_length = max(len(word) for word in matching_words)
            longest_words = [word for word in matching_words if len(word) == max_length]

            print(f"Longest words ({max_length} letters):")
            print(", ".join(longest_words))
            print(f"Round Score: {max_length}")

            return max_length
        else:
            print("No valid words can be formed from these letters.")
            return 0

    def start_game(self):
        """Starts the game and display total score to the user."""

        with open("words_alpha.txt") as f:
            dictionary = set(f.read().split())

        print("Welcome to the Countdown Letters Game!")

        total_score = 0

        for i in range(1, self.rounds):  
            letters = self.get_user_input(i)
            if not letters:
                return

            matching_words = self.find_matching_words(letters, dictionary)
            round_score = self.display_results(letters, matching_words)
            total_score += round_score


        print(f"\nGame Over")
        print(f"You completed 4 rounds with a total score of {total_score}. \n")    


if __name__ == "__main__":
    game = CoundownGame()
    game.start_game()
