
aum = 0
path = []

def  DFS(depth,m,n):      #m类有9个，n类有16个
    global aum
    if depth == 7:  #都访问完了
        if m == 0 and n == 0:
            aum = aum+1
            # print(path)
            # print()

        # else:
        #     return

    else:
        for i in range(0,m+1):    #m类分配啦
            for j in range(0, n + 1):   #n类分配啦
                if i+j>=2 and i+j<=5:
                    path.append([m-i, n-j])
                    DFS(depth+1, m-i, n-j)

DFS(0,9,16)
print(aum)