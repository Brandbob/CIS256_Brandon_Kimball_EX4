import random

word_list = ["Joe", "Mister", "Beast", "Burger", "Airplane", "Calipers"]
current_word = ""
guesses = []

def select_word() -> str:
    return word_list[random.randint(0, len(word_list) - 1)]

def is_letter_in_current_word(letter: str) -> bool:
    return letter.lower() in current_word.lower()

def display_word_in_progress():
    word = ""
    for letter in current_word:
        if letter.lower() in guesses:
            word += letter
        else:
            word += "_"
    print(word)

current_word = select_word()

while(True):
    print("\nWord:")
    display_word_in_progress()
    letter = input("Guess a letter: ").lower()
    if letter in guesses:
        print("Already guessed this letter.")
        continue
    else:
        guesses.append(letter)

    if is_letter_in_current_word(letter):
        print("Correct!")
    else:
        print("Wrong! Try again.")
    
    has_won = True
    for char in current_word.lower():
        if char.lower() not in guesses:
            has_won = False
            break
    
    if not has_won:
        continue
    print("\nYou win!")
    print(f"The word is {current_word}")
    break
