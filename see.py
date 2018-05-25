# beginer
p=list(input())
for i in range(0,len(p)-1,2):
    p[i],p[i+1]=p[i+1],p[i]
print("".join(str(x) for x in p))
