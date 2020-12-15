#for loopcwithout flag and using forelse :
a = int(input("Enter a number: "))
i = 2
for x in range(i,a):
    if a%x == 0:
        print ("Your number is NOT a prime number!")
        break
    else:
        i += 1
else:
    print ("Your number is a prime number!")
    

