def adding(x,y):
    return (x+y)

def subtracting(x,y):
    return(x-y)

def multiply(x,y):
    return(x*y)

print(adding(2,4),multiply(2,4), subtracting(2,4))

def add1(*args):
    return(sum(args))

ls=[1,23,4,5]
print(ls)
print(add1(ls[0-3]))

def add2(*ls):
    print(ls)
    return(sum(ls))

ls1 = [1,2,3,4,5,6,8,9,10]
print(add2(*ls1))