''' A A A
    B B B
    C C C
'''
n = int(input("Enter number of row :"))
alpha = ord("A")

for i in range(n):
     for j in range(n):
          print(chr(alpha+i),end = " ")
     print()
