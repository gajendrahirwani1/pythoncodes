"""
iterable - __iter__() or __getitem__()
iterator - __next__()
iteration- iterarte krne ke process ko iteration kahte haiiiiii
generators - ye ek tarah ke iterator hote hai jinko ham ek bar diverse kr skte hai...
"""

for i in range(10):         #normal iteration (on the fly)
    print(i)                #range is generator (jo ek bar bss use ho skta hai...)

#generator::::
def gen(n):
    for i in range(n):
        yield i     #yield on the fly value generate krega....

g = gen(12)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())

text = "Gajendra"
# for c in text:            # normal iteration
#     print(c)
#

ier = iter(text)           #this is generator  this is only for str....
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
