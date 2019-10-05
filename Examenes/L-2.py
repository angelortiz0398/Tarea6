def dibTrianguloE(num):
    for i in range(num + 1):
        k = num - 1
        print(' '*(2*num-i)+"*"*(2*i-1)+' '*k,end=' ')
        k -= 1
        print()
def main():
    dibTrianguloE(6)

if __name__ == '__main__':
    main()