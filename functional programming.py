#example of assigning a function to a variable and calling the function using the variable
def func():
    print('hello')

f = func     #assignment of function to a variable
f()          #call to func()



def sum(x,y):
    print(x+y)
g = sum      #assignment of function to a variable
g(10,20)     #call to sum()



#example of passing a function as argument to a function
def sum(x,y,f):
    print(x+y)
    f()          #calling a function
def func():
    print('hello')
f = func         #assignment of function to a variable
sum(10,20,f)     #pass function as argument to a function
