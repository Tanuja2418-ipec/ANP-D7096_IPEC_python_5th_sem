#taking input from the formula 
principle = float(input("Enter the principle amount(in rs.)"))

if principle < 0:
    print (" principle amount can not be negative.")

rate = float(input("Enter the rate of interest(in %)"))

if rate < 0:
   print (" rate of interest can not be negative ")   

time = int(input("Enter the time(in years)"))


if time<0:
    print("time can not be negative")

    

#displaying output to the user

print("the compound interest is ", principle*(1+(rate/100))**time)    