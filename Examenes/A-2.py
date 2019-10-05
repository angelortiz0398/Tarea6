def divisiblePor(Lis, num):
    for i in range(len(Lis)):
        if Lis[i] % num == 0 and Lis[i] > 0:
            print(Lis[i],end=" ")

def main():
    lists = [9, 12, 3, 0, 1, 4]
    divisiblePor(lists, 3)

if __name__ == '__main__':
    main()
