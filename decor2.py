def calculator(func):
    print("Execute this First")
    def inner(a,b):
        print("value of a",a)
        print("value of b",b)
        return func(a,b)
    return inner

@calculator

def add(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

add(10,2)