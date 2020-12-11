#palindrom
a=int(input("Enter a number"))
rev=0
c=a
while a>0:
     b=a%10
     rev=rev*10+b
     a=a//10
if c==rev :
    print("The given number is palindrome")
else:
    print("The given number is not palindrome")
