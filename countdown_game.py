from collections import Counter
import random

ROUNDS = 4

VOWEL_STACK = [
    "A","A","A","E","E","E",
    "I","I","I","O","O","O",
    "U","U","U","U"
]

CONSONANT_STACK = [
    "B","B","C","C","D","D","D","D","F","F","G","G","G",
    "H","H","J","K","L","L","L","L","M","M","N","N","N",
    "P","P","Q","R","R","R","R","S","S","S","S","T","T","T",
    "V","V","W","W","X","Y","Y","Z"
]

def load_dictionary(file):
    """Load dictionary words using a set."""
    with open(file) as f:
        return set(f.read().split())

def get_user_input():
    """Let the user choose 9 letters (vowel or consonant) and draw randomly."""
    
    letters = []
    vowels_count = 0
    consonants_count = 0

    print("\nChoose 9 letters. Type 'v' for vowel, 'c' for consonant.")

    while len(letters) < 9:
        choice = input(f"Pick letter {len(letters)+1}/9 (v/c): ").strip().lower()

        if choice not in ("v", "c"):
            print("Invalid choice. Type 'v' or 'c'.")
            continue

        stack = VOWEL_STACK if choice == "v" else CONSONANT_STACK
        letter = random.choice(stack)
        letters.append(letter)

        if choice == "v":
            vowels_count += 1
        else:
            consonants_count += 1

        print("\nLetters drawn:")
        print(" ".join(letter.upper() for letter in letters))

    if vowels_count < 3 or consonants_count < 4:
        print("You must choose at least 3 vowels and 4 consonants. Starting over.")
        return get_user_input()

    return letters

def find_matching_words(letters, dictionary):
    """Return all dictionary words that can be formed from the letters."""
    
    letters_counter = Counter(letters)
    matching_words = []

    for word in dictionary:
        word_counter = Counter(word)
        if all(word_counter[c] <= letters_counter.get(c, 0) for c in word):
            matching_words.append(word)

    return matching_words


def display_results(letters, matching_words):
    """Show longest words and return round score."""

    if not matching_words:
        print("No valid words can be formed from these letters.")
        return 0

    max_length = max(len(word) for word in matching_words)
    longest_words = [word for word in matching_words if len(word) == max_length]

    print(f"Longest words ({max_length} letters):")
    print(", ".join(longest_words))
    print(f"Round Score: {max_length}")

    return 18 if max_length == 9 else max_length


def start_game():
    print("Welcome to the Countdown Letters Game!")

    dictionary = load_dictionary("words_alpha.txt")
    total_score = 0

    for round_num in range(1, ROUNDS + 1):
        print(f"\n--- Round {round_num} ---")
        
        letters = get_user_input()
        letters_str = "".join(letter.lower() for letter in letters)
        matching_words = find_matching_words(letters_str, dictionary)
        round_score = display_results(letters_str, matching_words)

        total_score += round_score

    print("\n------ Game Over ------")
    print(f"You completed {ROUNDS} rounds with a total score of {total_score}.\n")


if __name__ == "__main__":
    start_game()
