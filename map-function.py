import math
def fun(n):
    return n*n
lst = [1,2,3,4]
m1 = map(math.radians,lst)
m2 = map(math.factorial,lst)
m3 = map(fun,lst)
print(list(m1))
print(list(m2))
print(list(m3))
