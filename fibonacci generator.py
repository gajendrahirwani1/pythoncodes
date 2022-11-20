def fibo(n):
    for i in range(n):
        yield i

        if n == 0:
            return 0
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fibo(n - 1) + fibo(n - 2)


def fibo(n):
    for i in range(n):
        yield i


g = fibo(1)
print(g.__next__())
print(g.__next__())


def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibogen(n-1) + fibogen(n-2)
def fibogen(n):
 i = 1
 while i<=n:
     yield fibo(i)
     i += 1

num = int(input("enter your number: "))
g = fibogen(num)
for i in g:
    print(i)
