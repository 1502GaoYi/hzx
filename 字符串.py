def count_chars(text):
    char_dict = {}
    for char in text:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

# text = "abd25+222"
text = input()
result = count_chars(text)
# print(result)

sum = 0
for i in result:
    # print(result[i])
    # print(len(text))
    if result[i] == 1:
        sum +=1
# print(sum)
if sum == len(text):
    print('YES')
else:
    print('NO')




