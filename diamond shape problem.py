# diamond shape problem is a confusion between multiple inheritance=================
class A:
    def met(self):
        print("this is method of A")

class B(A):
    def met(self):
        print("this is method of B")

class C(A):
    def met(self):
        print("this is method of C")

class D(B ,C):
    def met(self):
        print("this is method of D")

a = A()
b = B()
c = C()
d = D()
d.met()
