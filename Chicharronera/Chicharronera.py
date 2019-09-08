"""
* Chicharronera.py
* Solution for x1, x2
* When I. Term = 0
"""
import math

def Abs(num):
    return num * -1 if num < 0 else num

def CuadraticE(a,b,c):
    div = 2 * float(a)
    disc = b * b - (4 * a * c)
    if disc < 0:
        x1 = str(-b / div) + " + " + str(math.sqrt(dis * -1) / div) + "i"
        x2 = str(-b / div) + " - " + str(math.sqrt(dis * -1) / div) + "i"
        return [x1, x2]
    else:
        x1 = (- b + math.sqrt(dis)) / div
        x2 = (- b - math.sqrt(dis)) / div
        return [x1, x2]

        
print(CuadraticE(1,2,1))
print(CuadraticE(1,0,1))
