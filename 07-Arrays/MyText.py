def number_of_words(text):
    text = str(text)
    array_of_words = text.split()
    words = len(array_of_words)

    return words

def words_from_longest_to_shortest(text):
    words = str(text).split()
    sorted_words = sorted(words, key=len, reverse=True)

    return sorted_words

def alphabetical_order(text):
    words = str(text).split()
    alphabetical_words = sorted(words)

    return alphabetical_words
