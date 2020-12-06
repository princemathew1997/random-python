n=input("Enter a number")
sum=0
count=len(n)
z=int(n)
q=z
while z>0 : 
    r=z%10
    sum=sum+r**count
    z=z//10
if sum==q:
    print("The given number is amstrong")
else:
    print("The given number is not an amstrong number")
