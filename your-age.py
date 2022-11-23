#practice problem 1


print("Please select what do you want:")
print("1. Year when you become 100 years old")
print("2. Your age on given year")
select = int(input())
while(True):
    if select == 1:
        age = int(input("Enter your age: "))
        if age>0 and age<100:
            # afterAge =  2200 - (78 + age)
            afterAge = (2022 - age) + 100
            print(f"You become 100 years old in {afterAge}")
        elif age>= 100:
            print("You are already 100 years old")

    elif select == 2:
        Byear = int(input("Enter your birth year: "))
        year = int(input("Enter the year that you want your age on that year: "))
        if Byear >1000:
             year1 = year - Byear
             print(f"Your age on {year} is {year1}")
             break
        else:
            print("Please enter a valid Birth year")

    else:
        print("Please enter a valid key")
        break
