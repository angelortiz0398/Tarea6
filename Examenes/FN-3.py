def Unicos(lis):
    LisN = []
    for i in range(len(lis)):
        conta = 0
        for j in range(0,len(lis)):
            if lis[i] == lis[j]:
                conta +=1
        if conta == 1:
            LisN.append(lis[i])
    return LisN

def main():
    list_o = [9, 3, 1, 3, 2, 9]
    #list_o = [6, 2, 2, 2, 1, 8]
    #list_o = [1]
    print(Unicos(list_o))

if __name__ == '__main__':
    main()