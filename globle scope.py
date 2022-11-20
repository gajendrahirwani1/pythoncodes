l = 10   #this is globle scope
def fun1(n):
    l = 5           # this is local veriable , yaha globle read only hota hai
    m = 4           # local
    print(l,m)
    print(n,"i have printed")

fun1("This is me")
print(l)

l = 10   #this is globle scope
def fun1(n):
    global l       # yaha globle l ko read write kr skte hai....
    m = 4           # local
    print(l,m)
    print(n,"i have printed")

fun1("This is me")
print(l)


x = 88
def harry():
    x = 66
    def rohan():

        global x    #this globle veriable changes the first x value(88) to - x = 77
        x = 77
    print("before calling rohan()", x)
    rohan()
    print("after calling rohan()",x)
harry()
print(x)
