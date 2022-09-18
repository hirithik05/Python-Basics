#print fibonacci series 0 1 1 2 3 5 8 13 [n= n-1+n-2]
a = 0
b = 1
n = int(input("Enter number of terms:"))
print(a,b,end = " ")
for i in range(1,n-1):
    next_number = a + b
    print(next_number,end = " ")
    a = b
    b = next_number