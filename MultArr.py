def multArr(lis):
    res = 1
    for i in lis:
        res *= lis[i-1]
    return res     
lis = [1,2,3,4,5]
print(multArr(lis))
