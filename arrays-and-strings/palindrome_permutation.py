# QUESTION:
# Given a string, write a function to check if it is a permutatin of a palindrome. A palindrome is
# a word or phrase that is the same forwards and backwards. 
# You can ignore casing and non-letter characters.
# 
# EXAMPLE:
# Input:                    Output:
# Tact Coa                  True (permutations - "taco cat", "atco cta")

def palindrome_permutation(string):
    string = "".join(string.split())
    print(string)
    chars_dict = dict()
    for char in string:
        chars_dict[char] = chars_dict.get(char, 0) + 1

    print(chars_dict)
    odd_counter = 0
    for freq in chars_dict.values():
        print(freq, odd_counter)
        if freq % 2 == 1:
            if odd_counter + 1 > 1:
                return False
            odd_counter += 1

    return True

if __name__ == "__main__":
    print(palindrome_permutation("taco cat"))               # should print True
    print(palindrome_permutation("car car car"))            # should print False
    print(palindrome_permutation("catr car car"))           # should print True

