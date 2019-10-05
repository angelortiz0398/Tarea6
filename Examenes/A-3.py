def Operaciones(lis):
    conta = 0
    negativos = 0
    for i in range(len(lis)):
        if lis[i] >= 0:
            conta+=1
        else:
            negativos += lis[i]
    print(str(conta) + " positivos, " + str(negativos) + " la suma de negativos")
def main():
    #List = [1, 2, 3, 4, 5, 6, -11, -12, -13, -14, -15]
    List = [9, -8, 2, 1, -2]
    Operaciones(List)

if __name__ == '__main__':
    main()
