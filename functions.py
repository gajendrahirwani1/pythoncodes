#built-in function
a = 3
b = 2
c = sum((a , b))            #len(),max(),min(),....etc
print(c)

#user-define function
def fun1(a,b):
    print("you are in function", a + b)
fun1(1,2)
def fun2(a,b):
    """This is a function which will calculate average of two numbers"""
    print("average of a and b")
    average = (a + b)/2
    return average
v = fun2(2,4)
print(v)
print(fun2.__doc__)   #docstring
