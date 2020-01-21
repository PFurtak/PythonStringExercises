# Given a string, print the string uppercased
import codecs
string = input(
    "Please insert a sentence you would like to tranform into all uppercase characters. ")

upper_string = string.upper()
print(upper_string)

# Given a string, print the string capitalized
string_two = input(
    "Please insert one sentence you would like to capitalize. ")

cap_string = string_two.capitalize()
print(cap_string)

# Given a string, print the string reversed
string_three = input(
    "Please insert a sentence you would like to return reversed. ")

string_reversed = string_three[::-1]
print(string_reversed)

# Convert a string of text to leet speak


# Given a word as a string, print the result of extending any long vowels to the length of 5.

vowels = 'aeiou'
string_four = input("Please enter a sentence to elongate vowels on. ")
elongated = ' '
i = 0
while i < len(string_four):
    if string_four[i] in vowels and (i+1) < len(string_four):
        if string_four[i] == string_four[i]:
            elongated = elongated + (string_four[i] * 3)
        else:
            elongated = elongated + string_four[i]
    else:
        elongated = elongated + string_four[i]
    i = i + 1

print(elongated)

# Given a string, print the Caesar Cipher (or ROT13) of that string.
txt = input("Please insert text you would like to encrypt with ROT13. ")
encrypted = codecs.encode(txt, 'rot_13')

print(encrypted)
