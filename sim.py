# beginer
st1=input("Enter the 1st String: ")
st2=input("Enter the 2nd String: ")
c=list(st1)
d=list(st2)
for x in range(len(c)-1):
	flag=0
	for y in range(x+1,len(c)):
		if (c[x]==c[y]):
			c[y]='*'
			flag=1
	if flag==1:
		c[x]='*'
	elif(flag==0) and c[x]!='*':
		c[x]='#'
for x in range(len(d)-1):
	flag=0
	for y in range(x+1,len(d)):
		if d[x]==d[y]:
			d[y]='*'
			flag=1
	if flag==1:
		d[x]='*'
	elif(flag==0) and d[x]!='*':
		d[x]='#'
if(c[len(c)-1]!='*'):
	c[len(c)-1]='#'
if(d[len(c)-1]!='*'):
	d[len(d)-1]='#'
ans1=''
ans2=''
for x in a:
	ans1=ans1+x
for x in b:
	ans2=ans2+x
if(ans1==ans2):
	print("The strings are isomorphic")
else:
	print("The strings are not isomorphic")
