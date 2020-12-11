num = int(input('How many numbers: '))
sum = 0
i = 0
while i<num:
    a = input("Enter The Number: ")
    if a == 'q':
        break
    else:
        sum = sum + int(a)
        i += 1
avg = sum/i
print(avg)
