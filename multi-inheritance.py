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
