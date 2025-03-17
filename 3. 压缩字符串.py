#计算每个字符的最大个数
from collections import Counter

str1 = input()
count = Counter(str1)
count = dict(count)
# print(count)

k = 0



str2 = ''
for char in count:
    str2 = str2+char+str(count[char])
    # print(char)
    # print(str(count[char]))

if len(str1)> len(str2):
    print(str2)

else:
    print("N0")


