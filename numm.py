# beginer
import re

pat = r'^\d+$'

a = input()

if bool(re.match(pat, a)):
    a = int(a)
    flag = True
    ar = list(input().split())
    for i in ar:
        if not bool(re.match(pat, i)):
            print("Invalid")
            flag = False
            break
    if flag:
        ans = []
        for i in range(a):
            if i == int(ar[i]):
                ans.append(i)
        if len(ans) == 0:
            print(-1)
        else:
            print(*ans)
else:
    print("Invalid")
