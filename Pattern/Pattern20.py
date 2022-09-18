''' ****
     ***
      **
       *
'''
n = int(input("Total number of rows :"))
for i in range(n):
     #print space
     for j in range(i):
          print(" ",end = " ")
     #print Star
     for k in range(n-i):
          print("*",end = " ")
     print()
     
