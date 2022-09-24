n = int(input("Enter a value :"))
dec = 0
a = 0
while (n!=0):
     digit = n % 10
     if(digit == 1):
          dec = dec + pow(2,a)
     n = n // 10
     a = a + 1
print(dec)
     
