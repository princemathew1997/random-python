a=int(input("enter a number"))
if a%2==0:
    print(a,"is divisible by 2")
    if a%5==0:
        print(a,"is divisible by 5")
    else:
        print(a,"is not divisible by 5")
else:
    print(a,"is not divisible by2")
