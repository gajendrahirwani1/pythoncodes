class library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}


    def displayBooks(self):
        print(f"we have following books in our library: {self.name}")
        for books in self.booklist:
            print(books)

    def lendBooks(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("lender-book databasehas been updated.You can take the book now.")
        else:
            print(f"book is already being used by {self.lendDict[book]}")

    def addBook(self,book):
        self.booklist.append(book)
        print("book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)
        print("done")

if __name__ == '__main__':
    My_Dict = library(['python','c++','java','sql','javascript','c'],"Gajendra")
    while(True):
        print(f"welcome to the {My_Dict.name} library. Enter your choice to continue: ")
        print("1. Display books")
        print("2. Lend a books")
        print("3. Add a books")
        print("4. Return a books")
        user_ch = input()
        if user_ch not in ['1','2','3','4']:
            print("Please enter a valid option ")
            continue

        else:
            user_ch = int(user_ch)

        if user_ch == 1:
            My_Dict.displayBooks()

        elif user_ch == 2:
            book = input("Enter the name of the book you want to lend: ")
            user = input("Enter your name: ")
            My_Dict.lendBooks(user, book)

        elif user_ch == 3:
            book = input("Enter the name of the book you want to add: ")
            My_Dict.addBook(book)

        elif user_ch == 4:
            book = input("Enter the name of the book you want to return: ")
            My_Dict.returnBook(book)

        else:
            print("Not a valid option.Please select valid option ")

        print("Press q to quit and c to continue: ")
        user_ch2 = ''
        while(user_ch2!= 'c' and user_ch2!= 'q'):
            user_ch2 = input()
            if user_ch2 == 'q':
                exit()
            elif user_ch2 == 'c':
                continue
                
                
                
 #===========================================================================================================================================


#===============================================================================================================

#other way    



class library:
    def display(self, name):
        print("welcome to "+name ,end=" ")

    def lend(self, list):
        print("which book do you want ? ")
        a = input()
        print("what is your name? ")
        name = input()
        f = open("books.txt","a")
        f.write("\n(a)"+ name +"\n")
        print(f"{a} is now with you {name}")
        return f"{list.remove(a)}"

    def add(self, list):
        print("write the book name you want to add: ")
        a = input()
        print("what is your name? ")
        name = input()
        print("successfully added")
        return list.append(a)

    def ret(self,list):
        print("what do you want to return: " )
        a = input()
        print("your name: ")
        name = input()
        print("done")
        return list.append(a)

mylib = library()
mainlist = ["maths","physic","ramayana","mahabharat","chemistry","hindi","english"]
mylib.display("My library")
print(mainlist)
while True:
    print("what do you want to do: (display , add , lend or return ) ")
    do = input()
    if do == "lend":
        mylib.lend(mainlist)
    elif do == "add":
        mylib.add(mainlist)
    elif do =="return":
        mylib.ret(mainlist)
    elif do == "display":
        print(mainlist)
    else:
        print("please enter correct key...!!!")




