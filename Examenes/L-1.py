def dibTriangulo():
    for i in range(1,11):
        k = 1
        for j in range(i):
            print(k, end=' ')
            k += 2
        print()
def main():
    dibTriangulo()

if __name__ == '__main__':
    main()
