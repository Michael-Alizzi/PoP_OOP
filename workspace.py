def reverse_word(word):
    reversed = ""
    for letter in word:
            print(reversed)
            reversed = letter + reversed
    return reversed

def is_palindrome(word):
        return word == reverse_word(word)

print(reverse_word('moon'))

print(is_palindrome(['moon']))