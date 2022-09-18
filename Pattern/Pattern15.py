''' A
    B C 
    D E F
    G H I J
'''
n = int(input("Total number of rows :"))
alpha = ord("A")
for i in range(1,n+1):
     for j in range(i):
          print(chr(alpha),end = " ")
          alpha = alpha + 1
     print()
