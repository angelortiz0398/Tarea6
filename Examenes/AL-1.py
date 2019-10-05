def esPrimo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def primos(num1, num2):
    cont = 0
    print("Primos: ", end=' ')
    for i in range(num1, num2):
        if esPrimo(i) == True:
            cont += 1
            print(str(i) +",", end=" ")
    print("")
    print("Hay", cont, "numeros primos")

def main():
    print(primos(2, 100))

if __name__ == '__main__':
    main()
