arr=[]
T1=[]
T2=[]
T3=[]
n=int(input('no of elements? \n'))
for x in range(0,n):
	num=int(input())
	arr.append(num)
for x in arr:
	if x not in t1:
		T1.append(x)
	else:
		T2.append(x)
for x in T1:
	if x not in t2:
		T3.append(x)
print (T3)
