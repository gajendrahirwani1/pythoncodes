number = ["3","4","5","6"]
# for i in range(len(number)):                  #this is normal function
#     number[i] = int(number[i])
# number[2] = number[2] + 3
# print(number[2])
#=======================================Map function=====================================

# a map operation applies a function to each element in the sequence like list,tuple...
#    and returns a new sequence containing result..........

number = list(map(int, number))                 #this is to use to change type of items
print(number)

number[2] = number[2] +3
print(number[2])

#ex 2

def sq(a):
    return a*a
num = [1,2,3,4,5]
square = list(map(sq,num))                     #map function
print(square)

#ex3

num = [2,4,6,8]
print("this is output of ex3: ")
square1 = list(map(lambda x:x*x,num))          #lambda function
print(square1)


#ex 4
def square(a):
    return a*a
def cube(a):
    return a*a*a
func = [square,cube]
print("this is output of ex4: ")
for i in range(5):
    ans = list(map(lambda x:x(i),func))
    print(ans)



#=====================================filter operation=====================================================
#filter operation applies function to all the element of the sequence , the function return true is returned..
lst1 = [1,2,3,4,6,8,9,4,65,7,22]
def is_great(num):
    return num>5
great_5 = list(filter(is_great,lst1))
print("this is output of filter function: ")
print(great_5)


#=====================================reduce operation==================================================
# a reduce operation perform a rolling computation to sequential pairs of value in a sequence
# and returns the result
from functools import reduce       #to use reduce function ... this line is compulsory.!!!!!
lst2 = [1,2,3,4]
# num2 = 0
# print("this is output of normal function: ")
# for i in lst2:                   # this is normal function
#     num2 = num2 + i
# print(num2)
print("this is output of reduce function: ")
num3 = reduce(lambda x,y:x+y,lst2)    # this function returns 1+2+3+4=ans
print(num3)




# if we use map(),filter(),reduce() function in the program,,,,, we don't need to use for loop or
# if statement to control the flow
