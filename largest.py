# beginer
h=int(input())
a=[]
for x in range(0,h):
    b=input()
    a.append(b)
for i in range(0,h):
    for j in range(i+1,h):
        if(a[i]<a[j]):
            t=a[i]
            a[i]=a[j]
            a[j]=t
for i in range(0,h):
    print(a[i],end='')
