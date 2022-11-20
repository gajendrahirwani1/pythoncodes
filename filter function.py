#filter function

def fun(n):
    if n % 5 ==0:
        return True
    else:
        return False
lst1 = ['A','X','Y','3','M','4']
f1 = filter(str.isalpha,lst1)
print(list(f1))
lst2 = [5,10,18,27]
f2 = filter(fun,lst2)
print(list(f2))
