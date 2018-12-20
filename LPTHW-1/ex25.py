def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    return sorted(words)

def print_first_word(words):
    word = words.pop(0)
    print(word)

def print_last_word(words):
    word = words.pop(-1)
    print(word)

def sort_sen(sentence):
    """sorts sentence alphabetically"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = break_words(sentence)
    sorted = sort_words(words)
    print_first_word(words)
    print_last_word(words)
    return None


sentence = "All good things come to those who wait."



#ehy not working??

print_first_and_last_sorted(sentence)
#print(sort_sen(sentence))
