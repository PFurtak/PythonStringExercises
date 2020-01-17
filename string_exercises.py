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


#######REVISIT####################################################################
# Given a paragraph of text, convert to "Leet speak"
# A => 4 | E => 3 | G => 6 | I => 1 | O => 0 | S => 5 | T => 7
leet_table = {"a": "4", "e": "3", "g": "6",
              "i": "1", "o": "0", "s": "5", "t": "7"}
paragraph = input(
    "Please insert a block of text you would like to translate to 1337 sp34k. ")

leet_paragraph = paragraph.maketrans(leet_table)

print(leet_paragraph)

# Given a word as a string, print the result of extending any long vowels to the length of 5.

# Given a string, print the Caesar Cipher (or ROT13) of that string.
# Decrypt the following text: "lbh zhfg hayrnea jung lbh unir yrnearq"

txt = input("Please insert text you would like to encrypt with ROT13. ")
encrypted = codecs.encode(txt, 'rot_13')

print(encrypted)


#######REVISIT####################################################################
