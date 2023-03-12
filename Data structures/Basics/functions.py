for i in range(6):
    print(i)


# If you do not know the number of arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("maya", "sanjana", "golu", "prince")


# If you do not know the number of keyword arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?
def my_function2(**kid):
    print(type(kid))
    print("His last name is " + kid["lname"])


my_function2(fname="govind", lname="kumar", fullname="govind kumar")

"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
"""

dosum = lambda a, b, c: a + b + c
print(dosum(1, 2, 3))


# !Examples
def myfunc(n):
    return lambda a: a * n


def myfunc1(n):
    return lambda a: a * n


mydoubler = myfunc1(2)
print(mydoubler(11))


def hello():
    print("Hello world!")

def good_morning():
    print("Good morning!")


