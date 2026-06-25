#Take input form the user

principle = float(input("Enter the principle amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))

#Display the input to the user

print("principle : ",principle)
print("rate : ",rate)
print("time : ",time)

#Display output to the user

print("The simple interest is : ", (principle*rate*time)/100)
