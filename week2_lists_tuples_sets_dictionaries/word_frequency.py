"""
Name: Michael Alizzi
Student Id: 5651718
Word Frequency
"""

import re

def second_element(collection):
    """Returns the second element from a collection."""
    return collection[1]

with open("text.txt", "r", encoding="utf-8") as text:
    raw_text = text.read()

    # Return a list with items only containing individual alphabetic (a-zA-Z)/
    # numeric characters (0-9), whitespace (\s), "-" (\-) or "'" (')
    character_list = re.findall(r"[a-zA-Z0-9\s\-']", raw_text)

    # Join the items together into a new string
    new_text = ''.join(character_list)

    # Split the new punctuation-free text into a list containing words, with
    # whitespace as the separator
    word_list = new_text.split()

    # Capitalise every word in the list
    cap_text_list = [word.capitalize() for word in word_list]

    # Remove duplicate values using a set
    new_text_set = set(cap_text_list)

    # Create an empty dictionary to hold word and counts
    dict_count = {}

    # loop through the set to count the number of times each word appears in
    # the capitalised list
    for word in new_text_set:
        word_count = cap_text_list.count(word)
        dict_count[word] = word_count

    # Sort the dictionary by its values using the function above
    dict_count_sorted = dict(
        sorted(
            dict_count.items(),
            key=second_element,
            reverse=True
        )
    )

    for word, word_count in dict_count_sorted.items():
        print(f"{word}: {word_count}")
