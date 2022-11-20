#normal program
def fun_name_print(a,b,c,d):
    print(a,b,c,d)

fun_name_print("aman","naman","karan","dharam")

#args program--

def funargs(*args):
    print(type(args))
    print(args)

lst = ["suresh","mukesh","naresh","haresh"]
funargs(*lst)

def funargs(*args):             #for loop
    for item in args:
        print(item)
lst = ["suresh","mukesh","naresh","haresh"]
funargs(*lst)


def funargs(normal,*args):
    print(normal)
    for item in args:
        print(item)

lst = ["suresh","mukesh","naresh","haresh"]
normal = "this is normal arguments and the list is:"
funargs(normal,*lst)

#rule is - first normal, 2nd args then 3rd kwargs
#args and kwargs are optional

#kwargs-----
def funargs(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)

    print("\nNow i would like to introduce our heroes: ")
    for key,value in kwargs.items():
        print(f"{key} is a {value}")

lst = ["suresh","mukesh","naresh","haresh"]
normal = "this is normal arguments and the list is:"
kw = {"rohan":"cook","haresh ":"class monitor","naresh":"programmer"}
funargs(normal, *lst, **kw)
