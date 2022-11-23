# using super

class A:
    classvar1 = "i am a class variable in class A"
    def __init__(self):                     #constructor
        self.var1 = "i am inside class A's constructor"
        self.classvar1 = "instnce var in class A"
        self.special = "special"

class B(A):
    classvar1 = "i am in class B"
    def __init__(self):
        super().__init__()
        self.var1 = "i am inside B's constructor"
        self.classvar1 = "instance var in class B"

a = A()                     # this is called instance
b = B()
print(b.special, b.var1 , b.classvar1)
