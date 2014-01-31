import math

def recursive(i, r, d, n):
    print "r = "+str(r)+"; d = "+str(d)
    if r==n or d==n:
        i+=1
        return i
    else:
        i = recursive(i, r+1, d, n)
        i = recursive(i, r, d+1, n)
        return i

n = int(raw_input("n = "))
print recursive(0, 0, 0, n)
