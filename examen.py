def numfalta(L,e):
    Lc = [0,1,2,3,4,5,6,7,8,9]
    s = 0
    res = 0
    List = L
    if len(List) < 9:
        if List != Lc:
            for i in range(e):
                Lc.remove(List[i])
            print("Los elementos que faltan ",Lc)
    else:
        if len(List) == 10:
            print("No falta ninguno")
        else:
            for i in range(e):
                s += int(List[i])
                res = -1 * (s - 45)
                # 45 = 0+1+2+3+4+5+6+7+8+9
            print("El numero que falta es: " + str(res))

def main():
    L = []
    print("Cantidad de elementos: ")
    e = int(input())

    for i in range(e):
       L.append(int((input("Dame tu elemento: "))))

    numfalta(L,e)

if __name__ == '__main__':
    main()
