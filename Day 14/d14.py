#to get last char of even words
a = "Betty  Bought a Butter The Butter Was Bitter So Betty Bought a  Better Butter Which Was Not Bitter"
c = a.split()
b = {i: c.count(i) for i in c }
print(b)

