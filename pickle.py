import pickle   #preserve krke rakhna
# cars = ["tata","bmw","audi","mercedes"]
# file = "mycars.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()

file = "mycars.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
