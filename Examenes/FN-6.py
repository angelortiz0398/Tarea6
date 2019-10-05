def sumDif(lis):
    suma = 0
    for i in range(len(lis)-1):
        if i == len(lis):
            return suma
        else:
            suma += lis[i] - lis[i + 1]
    return suma
def main():
    print(sumDif([10, 2, 1]))
    print(sumDif([11, 10, 5]))
    print(sumDif([4, 3, 2, 1]))

if __name__ == '__main__':
    main()
