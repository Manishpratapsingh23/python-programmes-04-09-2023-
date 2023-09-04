#sum of digits of entered number
n=int(input("enter number: "))
s=0
r=1
t=n
while n!=0:
 r=n%10
 s=s+r
 n=int(n/10)
 
print("sum of digits of ",t," is ",s)




#output
#enter number: 123
#sum of digits of  123  is  6


#enter number: 546
#sum of digits of  546  is  15
