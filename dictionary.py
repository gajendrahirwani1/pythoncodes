#dictionary is a collection of key-value pair {key:value}

d1 = {}
print(type(d1))

d2 = {"harry":22,"aman":23,"arun":24}
print(d2)
print(d2["harry"])

d2["ankit"] = 25    # to add some key:value pair
print(d2)

del d2["aman"]      # to delete any key:value pair
print(d2)

d3 = d2.copy()         # swallow copy
del d3["harry"]
print(d2)

print(d2.get("harry"))   #value of harry
d2.update({"leena":27})  # add leena in dict
print(d2)

print(d2.keys())       #print all keys in dict


# dict are mutable , so we can perform add , delete, modify operations
#dict cannot be sliced using []
#concatenation - not working
#comparison    - not working
#merging       - not working
#conversion    - working
#cloning       - working
#identity      - working
#emptiness     - working
#aliasing      - working
#searching     - working
#reverse       - working
# any other basic opeeations are working
