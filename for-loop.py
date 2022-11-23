list = [["me",2],["aman",4],["naman",5],["numan",6]]
dict = dict(list)
for item, number in dict.items():
    print(item,"and number is ",number)


for item in dict :                          # for key only
    print(item)
