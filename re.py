# beginer
import re

sat = r'^[a-zA-Z ]+$'

s = input()

if bool(re.match(sat, s)):
    new = ""
    #new += s[0].upper()
    flag = True
    for i in s:
        if i == " ":
            flag = True
            new += i
        elif flag:
            new += i.upper()
            flag = False
        else:
            new += i
    print(new)
else:
    print("Invalid")
