"""-----------------------Internet Speed Rating-----------------------------  
Problem Statement An Internet Service Provider categorizes connection quality based on download speed. 
• Less than 25 Mbps → Slow  
• 25–99 Mbps → Good  
• 100 Mbps or above → Excellent  

Write a Python program to display the connection quality. 

Sample Input 120 
Sample Output Excellent Connection"""


#--------------------------Coding Section-----------------------------------    

#taking the input from the user
download_speed = float(input("Enter the download speed in Mbps: "))

#Validating the download speed
if download_speed < 0:
    exit("Invalid download speed. Please enter a positive value.")

#Categorizing the connection quality
if download_speed < 25:
    print("Slow Connection")
elif 25 <= download_speed < 100:
    print("Good Connection")
else:
    print("Excellent Connection")


#-----------------------------Output Section-----------------------------------

""" 
Sample input: 120
Sample output: Excellent Connection

Sample input: 50
Sample output: Good Connection

Sample input: 10
Sample output: Slow Connection"""