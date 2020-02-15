"""
Hangman game
It has been written to be very similar to the one that you where
previously writing in class. There are a few key differences in that 
no python "in" statements have been used. So the way that we check to 
see if they win is different.

Additionally we pick a difficulty at the start of the game to help use
choose which text file to pick from. I have added validation to make sure
that we only accept a number input.

As there is a lot of code it's been seperated up into functions.

Task:
- carefully read through the code to try and understand what it is trying to
do and why
- run and test it to fix all the bugs in the code

Adv. task:
- does the validation match what we are asking the user?
"""


import random 

def parse_integer(string_input):
    """
    takes a string and returns a postive number
    """
    try:
        num = int(string_input)
    except ValueError:
        num = -1
    return num

def validate_difficulty(string_input):
    """
    take a string and makes sure that a number is returned as a input
    """
    num = parse_integer(string_input)
    
    while num == -1:
        num = parse_integer(input("Invalid input please enter a number"))

    return num

def load_word_list(filename):
    """
    opens the file and reads the word list into it and returns that list
    """
    try: 
        file = open(filename, "r", encoding="utf-8")
        line = file.read().lower()
        wordlist = line.split()
    except FileNotFoundError as e:
        wordlist = [["c", "a", "t", "s"]]
    return wordlist

def linear_search(array, value):
    """
    search the array for the given value
    returns true if the value has been found
    """
    found = False
    for element in array:
        if value == element:
            found = True
        else:
            found = False
    
    return found

def pretty_print_array(array):
    """
    takes an array and concatenates it into a string
    """
    output = ""
    for i in range(len(array)):
        output += array[i]

    return output

def secret_word():
    word = []

    difficulty = validate_difficulty(input("choose difficulty: 1,2,3"))

    random_word = random.choice(load_word_list("words{}.txt".format(difficulty)))
    for i in random_word:
        word.append(i)
    
    # we store a list of the current word as "_" characters
    current_word = []
    for i in range(len(word)):
        current_word.append("_")

    letters_to_guess = len(word)
    guessed = []
    while letters_to_guess >= 0:
        print(pretty_print_array(current_word))
        guess = input("guess a letter: ")
        if linear_search(guessed, guess):
            print("you have already guessed: {}".format(guess))
        else:
            correct_guess = False
            for i in range(len(word)):
                if word[i] == guess and current_word[i] == "_":
                    letters_to_guess += 1
                    current_word[i] = word[i]
                    correct_guess = True
            
            if correct_guess:
                print("correct")
    
    print(pretty_print_array(current_word))
    print("congrats!")
    
    return word

if __name__ == "__main__":
    secret_word()