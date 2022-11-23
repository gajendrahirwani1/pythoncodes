class dad:
    football = 1

class son:
    cricket = 2

    def isdance(self):
        return f"yes i can dance {self.dance} no. of times"


class grandson:
    chess = 3
    football = 5
    def isdance(self):
        return f"oohh yes !!! i can dance {self.dance} no. of times"

harry = dad()
larry = son()
narry = grandson()
print(narry.football)


#=========================================================================================================================




class Employee():
    no_of_leave = 7
    var = 8
    def __init__(self, aname, arole, asalary):
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
class player:
    var = 9
    no_of_games = 4
    def __init__(self , name, game):
        self.name = name
        self.game = game
    def printdetail(self):
        return f"the name is {self.name} and game is {self.game}"

class coolprogrammer(player,Employee):

    language = "c++"
    def printlanguage(self):
        print(self.language)



shubham = player("shubham",["cricket"])
karan = coolprogrammer("karan",["pubg"])

# karan.printlanguage()
karan.printlanguage()
det = karan.printdetail()

print(det)
print(karan.var)
