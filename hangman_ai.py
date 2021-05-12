# COMP1405Z Hangman Algorithm
# William Lee

# global variables
refined_list = []
wrong_letters = []
active_letters = []
prev_guess = ""
most_common = ""


# round initialization, called at the start of each round. initializes global variables and parses word list
def initround(in_string, wordlist):
    global refined_list, wrong_letters, active_letters, most_common, prev_guess

    refined_list = [word for word in wordlist if len(word) == len(in_string)]
    wrong_letters.clear()
    active_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    prev_guess = in_string
    most_common = ""


# returns true if the inputted word is a valid hangman guess for string
def check_word(guess, word):
    # if the word has a wrong letter, it cannot be a valid guess
    for char in word:
        if char in wrong_letters:
            return False

    # unneeded?
    # otherwise, initialize list of all letters in the orig string so their indexes can be parsed
    # guess_chars = [char for char in guess]

    # check if char positions of guess line up with the given word
    for j in range(len(word)):
        if guess[j] != "_" and guess[j] != word[j]:
            return False

        """# finds valid positions for given letter, and if the character is outside such a position, word is invalid
        if word[j] in guess_chars:
            if j not in [i for i, x in enumerate(guess_chars) if x == word[j]]:
                return False"""

    return True


# with given word list, finds the most frequent letter. does not include already guessed letters
def find_most_freq(list_input):
    global most_common, active_letters

    letter_freqs = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

    # increments one count for each letter found in every word, but only if not guessed already
    for word in list_input:
        for char in word:
            if char in active_letters:
                letter_freqs[char] += 1

    # remove the most common letter from the letters list, since it will already have been guessed
    most_common = max(letter_freqs, key=letter_freqs.get)
    active_letters.remove(most_common)

    return most_common


# makes best guess for hangman based on the refined word list's most common letter
def makeguess(in_string):
    global wrong_letters, refined_list, prev_guess

    # if the last guess was right, refine the list anew with the string (only if the list still needs sorting)
    # otherwise, add the last guess to wrong_letters list
    if in_string != prev_guess:
        if len(refined_list) > 1:
            refined_list[:] = [word for word in refined_list if check_word(in_string, word)]
    else:
        prev_guess = in_string
        wrong_letters.append(most_common)

    return find_most_freq(refined_list)
