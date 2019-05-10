
def break_words(stuff):
    """This function will break up words for us，通过空格分开单词"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words单词排序"""
    return  sorted(words)

def print_first_word(words):
    """Prints the first word after popong it off"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popong it off"""
    word = words.pop(-1)
    print(word)

def  sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

