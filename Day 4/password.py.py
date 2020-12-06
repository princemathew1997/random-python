password=8850
access=False
p=int(input("Enter The Password: "))
if p==password:
    print("Welcome To The room")
    access=True
elif p<=password+5 and p>=password-5:
    print("Contact Admin And Rest Ur Password")
else:
    print("Unauthorised Acess")
if access==True:
    print("Access Granted")
else:
    print("Access Denied")