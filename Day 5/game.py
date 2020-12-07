import random
a = int(input("Enter the lower bound :"))
b = int(input("Enter the upper bound :"))
k = random.randint(a, b)
print("You Have Only 9 chance To Guess :")
limit = 9
count = 0
x=a
y=b
running = True
while running:
    while count<=limit:
       
        c=int(input("New number :"))
        if k==c:
            print("You won")
            running = False
            break
        elif c<=x:
            print("Poor entry too small")
        elif c < k-5:
            print(c,"Too small")
            x=int(c)
        elif c>=y:
            print("poor entry too large")
        elif c > k+5:
            print("Too large",c)
            y=int(c)
        else:
            print("You are near keep Trying")
        count += 1
    choice = input("Do u want to continue? (y/n)")
    count = 0
    if choice != "y":
        running = False
        

