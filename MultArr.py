def multArr(lis):
    res = 1
    if len(lis) != 0:
        for i in lis:
            res *= lis[i-1]
    else:
        res = 0
    return res     
lis = [1,2,3,4,5]
print(multArr(lis))
