''' A B C
    A B C
    A B C
'''
n = int(input("Enter number of row :"))
alpha = ord("A")

for i in range(n):
     for j in range(n):
          print(chr(alpha+j),end = " ")
     print()
