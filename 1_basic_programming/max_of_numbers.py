
#max of numbers
num1=input("enter num1")
num2=input("enter num2")

if num1 > num2:
    print("{0} is  bigger number than {1}".format(num1,num2))
elif num1 < num2:
    print("{0} is  bigger number than {1}".format(num2, num1))
else:
    print("{0} is equal to  {1}".format(num2, num1))

max_num = max(num1,num2)
min_of_num = min(num1,num2)
print("using max function {0}".format(max_num))
print("using min function {0}".format(min_of_num))

