#  enumerate function

lst = ["bhindi","aaloo","chopsticks","chocolate"]

i = 1
for item in lst:
    if i%2 !=0:
        print(f"jarvis please buy {item}")       #normal function
    i +=1


# enumerate function
for index, item in enumerate(lst):
    if index %2 ==0:
        print(f"please buy {item}")
