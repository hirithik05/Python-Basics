''' 1
    2 2
    3 3 3 
    4 4 4 4
'''
n = int(input("Enter number of row :"))
for i in range(1,n+1):
     for j in range(i):
          print(i,end= " ")
     print()
