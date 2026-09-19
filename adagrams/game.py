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






def uses_available_letters(word, letter_bank):
    pass


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

draw_letters()
