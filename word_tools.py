def count_word(file_txt, counter_word, sens_pref):
    """
    Count the amount of times a word appears in text.
    
    file_txt: the text from a file
    counter_word: the word to search for
    sens_pref: "y" or "n" for case sensitivity
    """

    if sens_pref == "n":
        file_txt = file_txt.lower()
        counter_word = counter_word.lower()

    word_count = file_txt.count(counter_word)

    return word_count

# commented out test cases
# print(count_word("Spam spam SPAM", "spam", "n")) # should be 3
# print(count_word("Spam spam SPAM", "spam", "y")) # should be 1



