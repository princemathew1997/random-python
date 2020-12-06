a=int(input("Enter a number"))
rev=0
while a>0:
     b=a%10
     rev=rev*10+b
     a=a//10
print("Reverse of the number is",rev)
