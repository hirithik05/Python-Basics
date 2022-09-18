''' A B C
    B C D
    C D E
'''
n = int(input("Total number of rows :"))
alpha = ord("A")
for i in range(1,n+1):
     for j in range(1,n+1):
          print(chr(alpha+i+j-2),end= " ")
     i = i + 1
     print()
          
