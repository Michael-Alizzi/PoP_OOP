import re

sentence = input("What is your sentence? ")

sentence_list = list(sentence)

vowels = ["a", "e", "i", "o", "u"]

for vowel in vowels:
    while vowel in sentence_list:
        sentence_list.remove(vowel)

print(f"Here it is without vowels: {''.join(sentence_list)}")
