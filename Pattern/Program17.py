''' D
    C D
    B C D
    A B C D
'''
n = int(input("Total number of rows :"))
for i in range(1,n+1):
     alpha = ord("A")+n-i
     for j in range(i):
          print(chr(alpha),end= " ")
          alpha = alpha +1
     i = i + 1
     print()
