str1 = input("")
str2 = input("")

str1 = str1.upper()
str2 = str2.upper()


str1 = ''.join(sorted(str1))
str2 = ''.join(sorted(str2))

if str1 == str2:
    print("YES")
else:
    print("NO")