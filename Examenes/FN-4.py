def promedio(lis):
    p = 0
    for i in range(len(lis)):
        p += lis[i]
    return p

def prom(lis):
    p = 0
    for i in range(len(lis)):
        p += lis[i]
    return p / len(lis)


def main():
    Lis = []
    List = [[1, 2, 2, 2, 2, 1], [2, 1]]
    #List = [[10, 5], [6, 2, 2], [1]]
    #List = [[3, 4, 1, 3, 5, 1, 4], [21, 54, 33, 21, 77]]
    Lis = [prom(List[0]),prom(List[1])]
    print(promedio(Lis))



if __name__ == '__main__':
    main()
