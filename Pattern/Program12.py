''' A B C
    D E F
    G H I
'''
n = int(input("Enter number of row :"))
alpha = ord("A")

for i in range(n):
     for j in range(n):
          print(chr(alpha),end = " ")
          alpha = alpha + 1
     print()
