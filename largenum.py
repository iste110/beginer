i1 = float(input("Enter first number: "))
i2 = float(input("Enter second number: "))
i3 = float(input("Enter third number: "))
 
if (i1 > i2) and (i1 > i3):
   largest = i1
elif (i2 > i1) and (i2 > i3):
   largest = i2
else:
   largest = i3
 
print("The largest number is",largest)
