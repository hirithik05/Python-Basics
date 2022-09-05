# Take multiple inputs in one line
x , y = input("Enter two value seprated by space").split() #if you want to take inputs as string
print(x)
print(y)
print(type(x))

a , b = map(int,input("Enter two value:").split()) #if you want to take inputs as integer
print(a)
print(b)
print(type(a))

l = list(map(int,input("Enter the elements of list :").split())) #if you want to take inputs as in list/tuple
print(l)

#Note :- inside split() you can write seprater example= ,
