# COMP1405Z Hangman Algorithm
# William Lee

# global variables
refined_list = []
wrong_letters = []
letters = []
prev_guess = ""
most_common = ""


# round initialization, called at the start of each round. initializes global variables and parses word list
def initround(string, wordlist):
    global refined_list, wrong_letters, letters, prev_guess, most_common

    refined_list = [word for word in wordlist if len(word) == len(string)]
    wrong_letters.clear()
    letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    prev_guess = string
    most_common = ""


# returns true if the guess made in the previous turn altered the guess string (was correct)
# additionally, updates prev_guess with current string, indicating it is the latest correct guess to compare off of
def was_correct(string):
    global prev_guess

    if string != prev_guess:
        prev_guess = string
        return True
    else:
        return False


# returns true if the inputted word is a valid hangman guess for string
def check_word(string, word):
    is_valid = True

    # if the word has a wrong letter, it cannot be a valid guess
    for char in word:
        if char in wrong_letters:
            is_valid = False
            break

    # otherwise, run some more checks
    if is_valid:
        # initialize list of all letters in the orig string so their indexes can be parsed
        orig_chars = [char for char in string]

        # first check if char positions of orig line up with compare; disregard 'blank' characters
        # then check if filled in characters of orig ("correct" characters) are in wrong positions of compare.
        for j in range(len(word)):
            if orig_chars[j] != "_" and orig_chars[j] != word[j]:
                is_valid = False
                break

            # finds valid positions for given letter, and if the character is outside such a position, word is invalid
            if word[j] in orig_chars:
                if j not in [i for i, x in enumerate(orig_chars) if x == word[j]]:
                    is_valid = False
                    break

    return is_valid


# with given word list, finds the most frequent letter. does not include already guessed letters
def find_most_freq(list_input):
    global most_common, letters

    letter_freqs = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

    # increments one count for each letter found in every word, but only if not guessed already
    for word in list_input:
        for char in word:
            if char in letters:
                letter_freqs[char] += 1

    # remove the most common letter from the letters list, since it will already have been guessed
    most_common = max(letter_freqs, key=letter_freqs.get)
    letters.remove(most_common)

    return most_common


# makes best guess for hangman based on the refined word list's most common letter
def makeguess(string):
    global wrong_letters, refined_list

    # if the last guess was right, refine the list anew with the string (only if the list still needs sorting)
    # otherwise, add the last guess to wrong_letters list
    if not was_correct(string):
        wrong_letters.append(most_common)

    else:
        if len(refined_list) > 1:
            refined_list[:] = [word for word in refined_list if check_word(string, word)]

    return find_most_freq(refined_list)
