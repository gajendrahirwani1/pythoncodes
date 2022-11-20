def func1():
    print("subscribe now")
func2 = func1
del func1
func2()

# #function ke andar function

def funcret(num):
    if num == 0:
        return print
    if num==1:
        return sum
a = funcret(0)
print(a)
b = funcret(1)
print(b)
#

#function ko as an argument bhi le skte hai.....
#ex--
def executor(func):
    func("Gajendra")

executor(print)


#-----------------------------------------decorator---------------------------------------------------
def deco(func):
    def nowexe():
        print("executing first")
        func()
        print("then execute this - 3rd line")
    return nowexe
@deco                                   #this is decorator
def who_is_Gajendra():
    print("me")
who_is_Gajendra()
