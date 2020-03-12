# QUESTION:
# Implement an algorithm to determine if a stringing has all unique characters.
# 
# BONUS: What if you cannot use additional data stringuctures?

# using Set datastringucture
# def is_unique(string):
#     string = string.lower()
#     chars_set = set()
#     for char in string:
#         if char in chars_set:
#             return False
# 
#         chars_set.add(char)
# 
#     return True


# using array as hashmap/dictionary
def is_unique(string):
    char_freq = [0] * 24
    string = string.lower()
    for char in string:
        char_index = ord(char) - ord('a')
        if char_freq[char_index] > 0:
            return False

        char_freq[char_index] += 1

    return True

if __name__ == "__main__":
    print(is_unique("abcdef"))          # should print True
    print(is_unique("abcabc"))          # should print False
    print(is_unique("abcABC"))          # should print False
    