a = int(input("Enter The Lower Bound: "))
b = int(input("Enter The Upper Bound: "))
i= 2
while a<= b:
    flag=0
    while i <= a:
        a%i==0
        flag=1
        break
    else:
        i+=1
else:
    print(i)