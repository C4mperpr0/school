c = 0
for i in range(1000, 9999):
    noe = 1
    n = str(i)
    for char in n:
        if char in "06789":
            noe = 0
    c += noe
print(c)
