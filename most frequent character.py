#Brian Webb
#ITEC 209
#4/2/2023
#Most Frequent Character

string = input("Enter a string: ")
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
most_common_char = max(char_count, key=char_count.get)
print("The character that appears most frequently in the string is:", most_common_char)
