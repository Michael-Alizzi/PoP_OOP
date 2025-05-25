import re

class TextClass:

    def __init__(self, text):
        self.words = text.split()

    def num_words(self):
        return len(self.words)

    def num_chars(self):
        return len(re.findall(r"[a-zA-Z0-9\-']", ''.join(self.words)))

    def word_length(self):
        return self.num_chars()/self.num_words()

text_input = input("Please enter your text: ")

text = TextClass(text_input)

print(f"Number of words: {text.num_words()}")

print(f"Number of characters: {text.num_chars()}")

print(f"Average word length: {text.word_length()}")