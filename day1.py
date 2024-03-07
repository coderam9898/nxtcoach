# python basics
print("Hello, World!")

#datatypes
# str
# int
# float
# list
# tuple
# range
# dict
# set
# boolean

age = 18      # age is of type int
name = "John" # name is now of type str
result = True
print(name)
print(type(age) , type(name),type(result))
# ascii
# newname = int(name)
# print(newname)
# type casting 
age  = "18"
print(age , type(age))

newage = int(age)

print(newage , type(newage))

def add():
    a = int(input("enter you first number:"))
    d = input(" enter second  number : ")

    b = 2
    c = a+int(d)
    return c

def formula(m,c):
    # (a+b)^2 = a^2 + 2ab + b^2
    # e = mc^2
    a = int(m)
    b = int(c)
    e = a*b**2
    return e


# operators
# arithmatic operators
# asignment operators
# comparision operators (==)
# logical operators (and , or ,not)
# identity operator ( is  , is not)
# membership operators ( in , not in)
# Python Bitwise Operators ( & , | , ^ ,~)




res = formula(2.16,"300000")
print(res , " this is result")


x = 2
print(x)


a = "mandip"

if a is "mandip": # ==
    print("good")
else:
    print("bad")
