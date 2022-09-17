''' 1 2 3
    4 5 6
    7 8 9
'''
n = int(input("Enter number of row :"))
count = 1
for i in range(n):
     for j in range(n):
          print(count , end = " ")
          count = count + 1
     print()
