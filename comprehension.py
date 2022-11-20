#==============================================list comprehension=====================================


lst = []
for i in range(50):                                 # this is normal program
    if i%2==0:
        lst.append(i)
lst = [i for i in range(50) if i%5==0]                # this is list comprehension
print(lst)

#====================================dictionary comprehension================================================


dict1 = {i:f"item {i}" for i in range(5)}               #this is dict comprehension
print(dict1)

to reverse key-value pair
dict1 = {i:f"Item {i}" for i in range(5)}
dict2 = {value:key for key,value in dict1.items()}
print(dict1,"\n",dict2)


#==================================set comprehension=========================================================
dresses = {dress for dress in ["dress1","dress2","dress2","dress1"]}
print(dresses)
print(type(dresses))                           #object itrespection







#===================================generator comprehension===========================================
evens = (i for i in range(50) if i%2==0)
print(type(evens))
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())

#or
for item in evens:
    print(item)

