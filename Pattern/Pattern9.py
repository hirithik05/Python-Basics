''' 1
    2 1
    3 2 1
    4 3 2 1
'''
n = int(input("Enter number of row :"))
for i in range(1,n+1):
     for j in range(i):
          print(i-j,end=" ")
     print()
