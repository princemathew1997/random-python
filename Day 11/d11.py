#for loop
a=input("Enter a number")
rev=0
for i in a:
     a=int(a)
     b=a%10
     rev=rev*10+b
     a=a//10
print("Reverse of the number is",rev)
