import os

def dateien(pfad):
    x = os.listdir(pfad)
    for datei in x:
        print(os.path.join(pfad, datei))
        if os.path.isdir( os.path.join(pfad, datei) ):
            dateien(os.path.join(pfad, datei))

#dateien('a')

def potenz_rekursiv(x, y, n=0):
    if n == 0:
        n = x

    if y > 1:
        n = potenz_rekursiv(x, y-1, n*x)
    return n

p = potenz_rekursiv(2, 3)

def potenz_schleife(x, y):
    n = x
    for i in range(y-1):
        n = n * x
    return n

p = potenz_schleife(2, 3)
print(p)

