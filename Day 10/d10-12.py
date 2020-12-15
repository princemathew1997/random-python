#string palindrome
a = input("Enter a String: ")
b = a[::-1]
if a==b:
    print("The given string is palindrome")
else:
    print("The given sting is not palindrome")