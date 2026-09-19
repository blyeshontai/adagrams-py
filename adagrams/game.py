from random import randint

'''
ANAGRAM
a word or phrase formed by rearranging the letters of a different word or phrase.
a player is given a random set of letters and must make an anagram using those letters.
Each submitted word will score points.
Do not use sample, choice, or select, or max
'''

# ----- WAVE 1 -----
'''
build a hand of 10 letters for the user.
array of 10 strings, 1 letter, random, based on table
'''


# letters and frequency provided
distribution_of_letters = {
    "A" : 9, "N" : 6, "B" : 2, "O" : 8,
    "C" : 2, "P" : 2, "D" : 4, "Q" : 1,
    "E" : 12, "R" : 6, "F" : 2, "S" : 4,
    "G" : 3, "T" : 6, "H" : 2, "U" : 4,
    "I" : 9, "V" : 2, "J" : 1, "W" : 2,
    "K" : 1, "X" : 1, "L" : 4, "Y" : 2,
    "M" : 2, "Z" : 1 }

# build a hand of 10 letters for the user
def draw_letters():

    # holds all letters based on count
    master_letter_list = []

    # users assigned letters
    hand = []

    # dont use a previous index when looping
    ints_used = []

    # add letters to master list
    for char in distribution_of_letters:
        for value in range(distribution_of_letters[char]):
            master_letter_list.append(char)

    # add 10 random letters to hand
    while len(hand) < 10:

        random_num = randint(0,len(master_letter_list)-1)

        # dont use a previous index
        if random_num not in ints_used:
            hand.append(master_letter_list[random_num])
            ints_used.append(random_num)
        else:
            continue

    return(hand)





# ----- WAVE 2 -----
'''
Check if word given only uses chars from hand letter_bank
returns T or F
'''
# check input word uses available char's
def uses_available_letters(word, letter_bank):
    # create a new modifiable list
    letter_bank_copy = letter_bank[:]
    # initialize function
    used_right_letters = False
    # account for case sensitivity
    refined_word = word.upper()

    # loop through word and check if it's in letter bank
    for i in refined_word:
        if i in letter_bank_copy:
            letter_bank_copy.remove(i)
            used_right_letters = True
        #not in letter_bank return false
        else:
            used_right_letters = False
            break

    return(used_right_letters)


# ----- WAVE 3 -----
'''
returns an int representing the number of points based on letter point value sum
if len(word) == 7, 8, 9, or 10. bonus 8 points.
'''
# return score of a word
def score_word(word):

    # score chart provided as a hashmap
    score_chart ={
        "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
        "D": 2, "G": 2,
        "B": 3, "C": 3, "M": 3, "P": 3,
        "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
        "K": 5,
        "J": 8, "X": 8,
        "Q": 10, "Z": 10}

    # initialize num of points
    num_of_points = 0
    refined_word = word.upper()

    if len(refined_word) == 7 or len(refined_word) == 8 or len(refined_word) == 9 or len(refined_word) == 10:
        num_of_points += 8
    else:
        num_of_points += 0
    for i in refined_word:
            num_of_points += score_chart[i]

    return(num_of_points)




def get_highest_word_score(word_list):
    pass
