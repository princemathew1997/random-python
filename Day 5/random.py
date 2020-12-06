import random
a = int(input("Enter the lower bound :"))
b = int(input("Enter the upper bound :"))
k = random.randint(a, b)
print("You Have Only 15 chance To Guess :")
limit = 9
count = 0
running = True
while running:

    while count<=limit:
        c=int(input("New number :"))
        if k==c:
            print("You won")
            running = False
            break
        if c < k-5:
            print("Too small")
        elif c > k+5:
            print("Too large")
        else:
            print("You are near keep Trying")
        count += 1
    choice = input("U Fail. Do u want to continue? (y/n)")
    count = 0
    if choice != "y":
        running = False
        

