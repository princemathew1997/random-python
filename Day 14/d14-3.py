string = "Betty  Bought a Butter the Butter Was Bitter So Betty Bought a  Better Butter Which Was Not Bitter"
max = 0
for i in string:
    print(i,max)
    if string.count(i) > max:
        max = string.count(i)
print (max)