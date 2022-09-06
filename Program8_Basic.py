#String method in Python
a = "hello world"
b = "HELLO"
c = ["1","2","3"]
print(a.capitalize()) #Convert first letter into upper case
print(b.lower())      #convert all letters into lower case
print(a.title())      #Convert every first letter of word into upper case
print(a.casefold())   #convert into lower case
print(a.upper())      #conver into upper case
print(a.count("hello"))   #count number of appearences
print(a.find("h"))     #return index of first apperences
print(a.replace("he","re"))  #change the string
print(a.swapcase())    #change lower case into uppercase and vice versa
print("#".join(c))     #used for iterable