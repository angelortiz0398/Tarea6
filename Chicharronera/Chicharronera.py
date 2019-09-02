"""
* Chicharronera.py
* Solution for x1, x2
* When I. Term = 0
"""


def Abs(num):
    return num * -1 if num < 0 else num

def CuadraticE(a,b,c):
    
    if((b**2 - 4*a*c) <= 0):
        d = (b**2 - 4*a*c)**(1/2)
        e = 2*a
        x1 = (b + d)/e
        x2 = (b - d)/e
        return x1, x2 
        
    else:
        det = b**2 - 4*a*c
        d = (abs(det))**(1/2)
        e = 2*a 
        x1 = str((b + d)/e) + "i"
        x2 = str((b - d)/e) + "i"
        return x1,x2
        
print(CuadraticE(1,2,1))
print(CuadraticE(1,0,1))
