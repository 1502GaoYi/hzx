import os
import sys
from collections import Counter
# 请在此输入您的代码
n=int(input())
m=input().split()

#输入

list = sorted(m)

a = ''
for i in range(n,0,-1):
    # str1 = ''+str(list[i])
    # int(list[i])

    a = a+list[i-1]
print((a))


'''
3
13 312 343


'''

