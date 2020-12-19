#number to words
import time
start_time = time.time()
o = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
t = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
h = ["", "One Hundred", "Two Hundred", "Three Hundred", "Four Hundred", "Five Hundred", "Six Hundred",
    "Seven Hundred", "Eight Hundred", "Nine Hundred"]
e = ["", "Eleven","Twelve","Thirteen","Fourteen","fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]

num = input("Enter the number: ")

text = []

rev_num = num[::-1]

i = 0

last_two = num[-2:]

first_no = 0    

if(len(num) == 3):
    first_no = num[:1]


if(10 < int(last_two) < 20):
    last_one = last_two[-1:]
    text.append(e[int(last_one)]) 

    if first_no != 0:
        text.append(h[int(first_no)])

    print(" ".join(text[::-1])) 


else:
    for digit in rev_num:
        if   i == 0:
            text.append(o[int(digit)])
        elif i == 1:
            text.append(t[int(digit)])
        elif i == 2:
            text.append(h[int(digit)])
        else:
            break
        i += 1

    print(" ".join(text[::-1]))
    end_time = time.time()
    print(f" The exection time is:{ end_time-start_time}")

