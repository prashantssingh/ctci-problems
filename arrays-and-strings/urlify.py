# QUESTIONS:
# Write a method to replace all spaces in a string with "%20". You may assume that the string 
# has sufficient space at the end to hold the additional characters, and that you are given the 
# "true" length of the string

# using lists
def urlify(str, str_len):
    chars_list = list(str)
    for i in range(str_len):
        if chars_list[i].isspace():
            chars_list[i] = "%20"

    return ("").join(chars_list)

if __name__ == "__main__":
    print(urlify("Mr John Smith    ", 13))          # should print True
