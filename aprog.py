def sumOfAP( a, d,n) :
    sum = 0
    i = 0
    while i < n :
        sum = sum + a
        a = a + d
        i = i + 1
    return sum
    
# Driver function
n = int(input("enter the n "))
a = int(input("enter the a "))
d = int(input("enter the d "))
print (sumOfAP(a, d, n))
