from random import randint

LETTER_POOL = {
    'A': 9,
    'B': 2,
    'C': 2,
    'D': 4,
    'E': 12,
    'F': 2,
    'G': 3,
    'H': 2,
    'I': 9,
    'J': 1,
    'K': 1,
    'L': 4,
    'M': 2,
    'N': 6,
    'O': 8,
    'P': 2,
    'Q': 1,
    'R': 6,
    'S': 4,
    'T': 6,
    'U': 4,
    'V': 2,
    'W': 2,
    'X': 1,
    'Y': 2,
    'Z': 1
}

def draw_letters():
    #empty list to hold available letters
    letter_pool = []
    #loop through letters
    for letter in LETTER_POOL:
        #loop through however many times that letter is there
        for i in range(LETTER_POOL[letter]):
            #add to list
            letter_pool.append(letter)
    #empty list for player's 10 letters
    letters = []

    #repeat 10 times
    for i in range(10):
        #pick a random index
        random_index = randint(0, len(letter_pool) - 1)
        #use that random index to get the letter at that position
        letter = letter_pool[random_index]
        #add to players hand
        letters.append(letter)
        #and remove from available pool
        letter_pool.remove(letter)
    #return the player's 10-letter hand
    return letters

def uses_available_letters(word, letter_bank):
    #make a copy of the letter bank
    available_letters = letter_bank[:]
    #convert the word to the same case
    word = word.casefold()

    #loop through each letter
    for letter in word:
        #convert to uppercase to match letter bank
        letter = letter.upper()
        #is letter available in bank
        if letter in available_letters:
            #remove
            available_letters.remove(letter)
        else:
            return False
    #after checking every letter in the word, then the word can be created
    return True


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass
