import random

def word_from_lists():
    categories = {
        "Bollywood Movies": ["Dilwale Dulhania Le Jayenge", "3 Idiots", "Sholay", "Kabhi Khushi Kabhie Gham", "Lagaan", "Dangal", "Zindagi Na Milegi Dobara", "Taare Zameen Par", "Kuch Kuch Hota Hai", "Barfi"],
        "Household Items": ["Table", "Chair", "Sofa", "Bed", "Lamp", "Refrigerator", "Microwave", "Toaster", "Washing Machine", "Dishwasher"],
        "Cars": ["Toyota Corolla", "Honda Civic", "Ford Mustang", "Chevrolet Camaro", "Tesla Model S", "BMW 3 Series", "Audi A4", "Mercedes-Benz C-Class", "Volkswagen Golf", "Hyundai Elantra"],
        "Fruits": ["Apple", "Banana", "Orange", "Grapes", "Mango", "Pineapple", "Strawberry", "Blueberry", "Watermelon", "Peach"],
        "Countries": ["United States", "Canada", "India", "Australia", "Germany", "France", "Japan", "China", "Brazil", "South Africa"]
    }
    category_name = random.choice(list(categories.keys()))
    word = random.choice(categories[category_name])
    return category_name, word

def display_the_word(word, guessed_letters):
    vowels = "aeiou"
    display = ""
    word = word.lower()  # Convert word to lowercase

    for char in word:
        if char in vowels or char in guessed_letters:
            display += char
        elif char == " ":
            display += " "
        else:
            display += "_"
    return display

def playgame(word):
    allowed_guesses = 6
    guessed_letters = set()
    current_display = display_the_word(word, guessed_letters)

    print("Welcome to Hangman!")
    print(current_display)

    while allowed_guesses > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word.lower():
            current_display = display_the_word(word, guessed_letters)
            print("Good guess!")
        else:
            allowed_guesses -= 1
            print(f"Incorrect guess. You have {allowed_guesses} guesses left.")

        print(current_display)

        if '_' not in current_display:
            print("Congratulations! You've guessed the word!")
            break
    else:
        print(f"Game over. The word was '{word}'.")

def hangman():
    category_name, word = word_from_lists()
    print(f"Category: {category_name}")
    playgame(word)

print("*********************** HANGMAN THE GAME *********************")

mode = input("Press ENTER to start game (q to quit): ")

if mode == 'q':
    quit()
else:
    hangman()
