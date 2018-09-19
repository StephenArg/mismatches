import os

os.chdir("/Users/BasicallySteve/Desktop")

with open("lineS.txt", "r") as f:
    for letter in f:
        s=""
        s += letter

with open("lineT.txt","r") as f2:
    for letter in f2:
        t=""
        t +=letter

length = len(s)
que_number = 0
number = 0


print(s)
print(t)

while que_number < length:
    if s[que_number] == t[que_number]:
        que_number +=1
    else:
        number += 1
        que_number += 1


print("There are " + str(number) + " mismatches.")
