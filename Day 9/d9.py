#for loop
a = int(input("Enter a number: "))
i = 2
flag = 0
for x in range(i,a):
    if a%x == 0:
        flag = 1
        break
    else:
        i += 1
if flag == 0:
    print ("Your number is a prime number!")
else:
    print ("Your number is NOT a prime number!")

