# == - "value equality" - two objects have the same value
# is - "reference equality"- two references refer to the same object

#task
a = [1,2,3,4,"34"]
b = [1,2,3,4,"34"]
print(a is b)  #prints false
print(a == b)  #prints true
