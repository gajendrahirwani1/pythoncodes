#container is an entity which contains multiple data item.
# It is also known as a collection of a compound data type
# lists are mutable , it can change

animals = ["lion","tiger","zebra","elephant"]
num = [1,2,4,3,7,6,5]
lst = []                            #empty list
lst1 = ["sanjay",15,16.66]          #list can contain dissimilar types
print(animals)
print(num[2])
num.sort()                          # sorting in ascending order
print(num)
#num.reverse()                       # sorting in reverse order
print(num)


#slicing
print(num[1:5])              # [start:end]
# extended slicing
print(num[0:5:2])            #[start:end: ]
print(num[::-1])             #reversed


print(len(num))
print(max(num))
print(min(num))
print(sum(num))
print(any(num))
print(all(num))

num.append(7)    #add something at end
print(num)

num.insert(2,99) #insert something in the list
print(num)

num.remove(2)   #remove 2nd position number
print(num)

num.pop()      #removes last position number
print(num)

