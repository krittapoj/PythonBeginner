x = lambda a , b : a + b

print(x(5, 5))

#-------------------------------------------------
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(3)

print(mydoubler(10))