#to get last char of even words
a = "Betty  Bought a Butter The Butter Was Bitter So Betty Bought a  Better Butter Which Was Not Bitter"
b = [ i[-1] for i in a.split() if len(i)%2==0]
print(b)
