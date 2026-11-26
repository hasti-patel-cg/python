
# def divide(c,d,/,*,a=10,b):
#     return a/b,c+d

# print(divide(12,12,b=2))

# def divide(c,d=12,/,*,a=10,b):
#     return a/b,c+d

# print(divide(12,13,b=2))

# def add(*args):
#     print(args)
#     print(type(args))

# add(10, 20, 30)

# def add(a,b,*args):
#     print(a,b,args)
#     print(type(args))

# add(a=10, b=20, 30)

# def add(*args):
#     print(args)
#     print(type(args))

# add()

# def add(*args,**kargs):
#     print(kargs,args)
#     print(type(kargs))

# add(12,34,56,a=10, b=20, c=30)

add=0;
def addition(n):
    global add;
    add+=n;

    if n==10:
        return add;

    return addition(n+1);

print(addition(1))


