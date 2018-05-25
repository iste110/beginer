# beginer
ip=input("Enter your Roman:")
st=list(ip)
a=[]
for x in st:
	if x=="V" or x=="v":
		a.append(5)
	elif x=="I" or x=='i':
		a.append(1)
	elif x=="X" or x=='x':
		a.append(10)
	elif x=="L" or x=='l':
		a.append(50)
	elif x=="C" or x=='c':
		a.append(100)
	elif x=="D" or x=='d':
		a.append(500)
	elif x=="M" or x=='m':
		a.append(1000)
 
z=a.index(max(a))
ans=max(a)
if z==0:
	for x in range(1,len(a)):
		ans=ans+a[x]
else:
	for x in range(len(a)-1):
		ans=ans-a[x]
print(ans)
