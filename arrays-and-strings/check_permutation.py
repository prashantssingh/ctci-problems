# QUESTION:
# Given two strings, write a method to decide if one is a permutation of the other

# using sorting
# def check_permutation(str1, str2):
#     if len(str1) != len(str2): 
#         return False
#     str1_list = list(str1.lower())
#     str2_list = list(str2.lower())
# 
#     str1_list.sort()
#     str2_list.sort()
#     if str1_list == str2_list:
#         return True
# 
#     return False

# using list as hashmap/dict
def check_permutation(str1, str2):
    if len(str1) != len(str2): 
        return False

    str1 = str1.lower()
    str2 = str2.lower()
    
    str1_char_freq = [0] * 24
    for char in str1:
        str1_char_freq[ord(char) - ord('a')] += 1

    for char in str2:
        str1_char_freq[ord(char) - ord('a')] -= 1
        if str1_char_freq[ord(char) - ord('a')] < 0:
            return False

    return True

if __name__ == "__main__":
    print(check_permutation("abc", "cba"))          # should print True
    print(check_permutation("abc", "CBA"))          # should print True 
    print(check_permutation("abc", "abd"))          # should print False