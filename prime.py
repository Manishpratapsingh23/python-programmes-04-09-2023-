#number entered is prime or not
n=int(input("enter number: "))
c=0
if n==1:
 print("1 is not a prime number")
else:
  for i in range(2,(n+1)):
   if n%i==0:
      c=c+1
if c==1:
 print(n," is a prime number")
else:
 print(n," is a not prime number")
 

#output
#enter number: 7
#7  is a prime number


#enter number: 28
#28  is a not prime number
