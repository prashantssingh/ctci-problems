# QUESTION:
# Given a string, write a function to check if it is a permutatin of a palindrome. A palindrome is
# a word or phrase that is the same forwards and backwards. 
# You can ignore casing and non-letter characters.
# 
# EXAMPLE:
# Input:                    Output:
# Tact Coa                  True (permutations - "taco cat", "atco cta")

def palindrome_permutation(str):
    chars_dict = dict()
    for char in str:
        chars_dict[char] = chars_dict.get(char, 0) + 1

    odd_counter = 0
    for freq in chars_dict.values():
        if (freq % 2 == 1) and (odd_counter + 1) > 1:
            return False

    return True