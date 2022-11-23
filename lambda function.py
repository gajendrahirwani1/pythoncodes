#using lambda with map
lst1 = [5,10,15,20]
m = map(lambda n:n*n,lst1)
print(list(m))


#using lambda with filter
lst2 = [5,10,15,20]
f = filter(lambda n:n%2==0,lst2)
print(list(f))

#using lambda with reduce
from functools import reduce
lst3 = [1,2,3,4,5]
s = reduce(lambda x,y:x+y,lst3)
p = reduce(lambda x,y:x*y,lst3)
print(s)
print(p)


#if required map(),filter(),reduce() can be used together
def fun(n):
    return n>1000
lst = [10,20,30,40,50]
l = filter(fun,map(lambda x:x*x,lst))
print(list(l))
#============================================================================

#function that receives an argument and returns its cube
print((lambda n:n*n*n)(3))


#function that receives 3 arguments and returns average of them
print((lambda x,y,z:(x+y+z)/3)(10,20,30))


#function that receives a string , strips any whitespace and return the uppercase version of the string
print((lambda s:s.lstrip().rstrip().upper())(' Ngp '))





#The lambda can also be assigned to a variable and then invoked
p = lambda n:n*n*n
q = lambda x,y,z:(x+y+z)/3
r = lambda s:s.lstrip().rstrip().upper()
print(p(3))
print(q(10,20,30))
print(r(' ngp '))

#container type can also be passed to a lambda function
lst1 = [1,2,3,4,5]
lst2 = [10,20,30,40,50]
print((lambda l:sum(l)/len(l))(lst1))
print((lambda l:sum(l)/len(l))(lst2))

