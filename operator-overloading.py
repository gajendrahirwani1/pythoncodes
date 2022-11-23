class employee:
    def __init__(self, aname , asalary, arole):    #this is dunder method
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetail(self):
        return f"The name is {self.name}, salary is {self.salary} and his role is {self.role}"

    def __add__(self, other):    #this is maping operator in function
        return  self.salary + other.salary
    def __repr__(self):
        return f"employee('{self.name}', {self.salary},'{self.role}')"
    def __str__(self):
        return f"the name is {self.name}, his salary is {self.salary},his role is {self.role}"

emp1 = employee("harry", 45,"programmer")
emp2 = employee("larry",40, "cleaner")
print(emp1 +emp2)
print(repr(emp1))
print(str(emp2))
