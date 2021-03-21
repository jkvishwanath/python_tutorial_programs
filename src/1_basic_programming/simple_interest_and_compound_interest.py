#Simple interest program
principle = int(input("enter principle amount"))
interest = int(input("enter interest rate"))
term = int(input("enter term"))

simple_interst = (principle*interest*term)/100
print("simple interst is {0} ".format(simple_interst))



#Compound interest program

#A = P(1 + R/100) power t  -> Compound Interest = A – P
#A is amount , P is principle amount , R is the rate and T is the time span


Amount = principle * pow((1+interest/100), term)
compound_interest  = Amount - principle

print("compound interest is {0} ".format(compound_interest))
