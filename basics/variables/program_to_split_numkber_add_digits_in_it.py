number = input("Enter the number\n")
print(type(number))

print(number.isdigit())
print(number.isnumeric())
if(number.isdigit()):
    sum = 0

    try:
        for each_digit in number:
            sum += int(each_digit)
        print(sum)
    except:
        print("Error occured while processig request.")
else:
    print("enterted value is not number")