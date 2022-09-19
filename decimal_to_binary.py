n = int(input("Enter a value :"))
ans = ""
while ( n!=0 ):
    rem = n % 2
    ans = ans + str(rem)
    n = n // 2
print("Binary : ",int((ans)[::-1]))