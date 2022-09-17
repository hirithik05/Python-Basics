''' 1 1 1
    2 2 2
    3 3 3
'''
n = int(input("Enter number of row :"))
a = 1
for i in range(n):
     for j in range(n):
          print(a,end = " ")
     print()
     a = a + 14