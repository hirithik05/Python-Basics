num = int(input("Enter the number :"))
count = 1
for i in range(2,num):
    if num==2:
        count = 1
    elif (num%i == 0):
        count = 0
        break
if ( count == 1):
    print("Prime")
else:
    print("Not prime")