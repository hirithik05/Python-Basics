''' A
    B C
    C D E
'''
n = int(input("Total number of rows :"))
alpha = ord("A")
for i in range(1,n+1):
     for j in range(i):
          print(chr(alpha+i+j-1),end = " ")
     i = i + 1
     print()
