# inheritance --- purane program ko copy krke usme kuchh naya code add krna
class Employee():
    no_of_leave = 7
    def __init__(self, aname, arole, asalary):          #this is called constructor
        self.name = aname
        self.role = arole
        self.salary = asalary

    def printdetail(self):
        return f"The name is {self.name} and role is {self.role}, his salary is {self.salary}"
    @classmethod
    def change_leave(cls,new_leave):
        cls.no_of_leave = new_leave

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))   # *arg function
    @staticmethod
    def printgood(string):
        print("this is good " + string)

class programmer(Employee):                 #this is an ex of single inheritance
    no_of_holiday = 56
    def __init__(self, aname, arole, asalary, languages):
        self.name = aname
        self.role = arole
        self.salary = asalary
        self.languages = languages

    def printprog(self):
        return f"the programmer's name is {self.name}, his salary is {self.salary},and role is {self.role}. the languages are {self.languages}"

harry = Employee("harry","student",13000)
rohan = Employee("rohan","actor",20000)
karan = Employee.from_dash("karan-teacher-12090")

shubham = programmer("shubham","programmer",13333,["python","cpp"])

print(shubham.no_of_holiday)
print(shubham.languages)


#====================sigle inheritance =================
class parent():
    def first(self):
        print("parent function")

class child(parent):
    def second(self):
        print("child function")
object1 = child()
object1.first()
object1.second()
