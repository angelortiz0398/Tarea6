'''
LinearBusq.py; busca un elemento en un arreglo de numeros aleatorios
'''
import random

def busca(lis,e):
    for i in range(len(lis)):
        if lis[i] == e:
            return i
    return -1

def main():
    lista = [random.randint(0,100) for _ in range(10000)]
    print(busca(lista,7))
    print(busca(lista,99))
    print(busca(lista,101)) 
    print(busca(lista,44))

if __name__ == '__main__':
    main()
