# COMP1405Z Hangman Algorithm
# William Lee

# global variables
refined_list = []
letter_freq = {}
wrong_letters = []
guessed_letters = []
prev_guess_word = ""
prev_guess_letter = ""


# round initialization, called at the start of each round. initializes global variables and parses word list
def initround(in_string, wordlist):
    global refined_list, letter_freq, wrong_letters, guessed_letters, prev_guess_word, prev_guess_letter

    letter_freq = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

    refined_list.clear()

    for word in wordlist:
        if len(word) == len(in_string):
            for char in word:
                letter_freq[char] += 1
            refined_list.append(word)

    wrong_letters.clear()
    guessed_letters.clear()
    prev_guess_word = in_string
    prev_guess_letter = ""


# returns true if the inputted word is a valid hangman guess for string
def check_word(guess, word):
    global letter_freq

    valid_word = True

    # if the word has a wrong letter, it cannot be a valid guess
    for j in range(len(word)):
        if (guess[j] in wrong_letters) or (guess[j] != "_" and guess[j] != word[j]):
            valid_word = False
            break

    if not valid_word:
        for c in word:
            letter_freq[c] -= 1

    return valid_word


# with given word list, finds the most frequent letter. does not include already guessed letters
def find_most_freq():
    most_common = max((k for k in letter_freq if k not in guessed_letters), key=letter_freq.get)

    return most_common


# makes best guess for hangman based on the refined word list's most common letter
def makeguess(in_string):
    global wrong_letters, guessed_letters, refined_list, prev_guess_word, prev_guess_letter

    # if the last guess was right, refine the list anew with the string (only if the list still needs sorting)
    # otherwise, add the last guess to wrong_letters list
    if in_string != prev_guess_word:
        if len(refined_list) > 1:
            refined_list[:] = [word for word in refined_list if check_word(in_string, word)]

    else:
        wrong_letters.append(prev_guess_letter)
    guessed_letters.append(prev_guess_letter)

    prev_guess_letter = find_most_freq()

    return find_most_freq()
