# QUESTION:
# Implement a method to perfrom basic string compression using the counts of repeated characters.
# For example, the string "aabcccccaaa" would become "a2b1c5a3". If the "compressed" string would
# not become smaller that the original string, your method should return the original string. You
# can assume the string has only uppercase and lowercase letters (a-z).

def compress(string):
    if not string: return ""

    compressed_string = ""
    i = 0
    while i < len(string):
        curr_char, count = string[i], 0
        while curr_char == string[i] and i < len(string)-1:
            count += 1 
            i += 1
            
        compressed_string += curr_char + str(count)
        print(curr_char, count, i, compressed_string)

    if len(string) <= len(compressed_string):
        return string

    return compressed_string

if __name__ == "__main__":
    print(compress("aabcccccaaa"))          # should print a2b1c5a3
