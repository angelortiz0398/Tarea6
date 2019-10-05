def Prom(lis):
    suma = 0
    for i in range(len(lis)):
        suma += lis[i]
    return suma/6
def Promedios(a,b,c,d,e):
    conta = 0
    if a >= 6:
        conta += 1
    if b >= 6:
        conta += 1
    if c >= 6:
        conta += 1
    if d >= 6:
        conta += 1
    if e >= 6:
        conta += 1
    return (conta/5)*100

def main():
    #Lis = [[9, 8, 7, 5, 2, 10],[5, 5, 5, 5, 5, 5],[0, 1, 2],[4, 2, 4, 5, 7, 8],[1, 1, 1, 1]]
    Lis = [[6],[10, 10, 5, 10, 10, 10],[9, 8, 9, 8, 7, 6],[10],[6, 7, 8, 9, 9, 6]]
    print(str(Promedios(Prom(Lis[0]),Prom(Lis[1]),Prom(Lis[2]),Prom(Lis[3]),Prom(Lis[4])))+"%")
if __name__ == '__main__':
    main()
