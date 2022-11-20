# json module

import json  #java script object notation
data = '{"var1":"harry","var2":"56"}'
print(data)

parsed = json.loads(data)
print(parsed)

data2 = {
    "channel":"coding",
    "cars":['audi','bmw','porche'],
    "bikes":('mt15',150),
    "isbad":False
}
jscomp = json.dumps(data2)
print(jscomp)
