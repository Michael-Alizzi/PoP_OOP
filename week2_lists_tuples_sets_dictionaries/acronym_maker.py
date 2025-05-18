name = input("What is the name? ")

name_list = name.split()

first_letter_list = []

for word in name_list:

    first_letter_cap = word.capitalize()

    first_letter_list.append(first_letter_cap[0])

print(''.join(first_letter_list))