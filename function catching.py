# # # # import time
# # # # import functools
# # # # @functools.lru_cache(maxsize=3)
# # # # def some_work(n):
# # # #     #some task taking n second
# # # #     time.sleep(n)
# # # #     return n
# # # #
# # # # if __name__ == '__main__':
# # # #     print("now running some work")
# # # #     some_work(3)
# # # #     print("done....calling again")
# # # #     some_work(3)
# # # #     print("called again")
# # #
# # # #=======================================================================================================
 #  for exercise


# # # import time
# # # from functools import lru_cache
# # # @lru_cache(maxsize=int(input("how many value do want to cache: ")))
# # # def work(n):
# # #     time.sleep(3)
# # #     return n
# # #
# # # if __name__=='__main__':
# # #     print("running work")
# # #     work(2)
# # #     print("running work")
# # #     work(2)
# # #     print("running work")
# # #     work(3)
# # #     print("run again")
# # #     work(4)
# # #     print("run again and again")
# #
# # import time
# # from functools import lru_cache
# #
# # n = int(input("how many values do you want to store: "))
# # @lru_cache(maxsize=n)
# # def fibo(x):
# #     time.sleep(x)
# #     return x
# #
# # if __name__ == '__main__':
# #     print("calling 1st time ")
# #     fibo(3)
# #     print("calling 2nd time ")
# #     fibo(5)
# #     print("calling 3rd time ")
# #     fibo(5)
# #     print("calling 4th time ")
# #     fibo(5)
#
# #exercise2
# import time
# from functools import lru_cache
# @lru_cache(maxsize=5)
# def fact(n):
#     fac = 1
#     for i in range(1,n):
#         fac = fac*(i+1)
#     time.sleep(2)
#     return fac
# print(fact(5))
# print("once done with call ")
# num = int(input("enter number: "))
# print(fact(num))

#exercise 3
from functools import lru_cache
n = int(input("enter the number to find it's fibo: "))

@lru_cache(maxsize=n)
def fibo(num):
    if num < 2:
        return 1
    else:
        return fibo(num-1)+fibo(num-2)

print(fibo(n))
