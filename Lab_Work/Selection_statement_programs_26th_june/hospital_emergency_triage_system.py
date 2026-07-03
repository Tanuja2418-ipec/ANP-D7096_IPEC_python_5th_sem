"""-----------------------------Hospital Emergency Triage System---------------------------------------
 Problem Statement A hospital prioritizes patients based on: • Critical Condition  
                                                             • Age  
                                                             • Oxygen Level 
                                                      Rules: • Critical condition → Immediate Treatment  
                                                             • Oxygen below 90 → High Priority  
                                                             • Age above 65 → Medium Priority  
                                                             • Others → Normal Priority 
Sample Input Critical Condition (Y/N): N Age: 70 Oxygen Level: 94 
Sample Output Patient Priority: Medium Priority Reason: Senior Citizen """


#-------------------------------coding section--------------------------------

#take inputs from the user
critical_condition = input("Is the patient in critical condition? (Y/N): ")
age = int(input("Enter the age of the patient: "))
oxygen_level = int(input("Enter the oxygen level of the patient: "))

#displaying the input to the user
print("Critical Condition: ", critical_condition)
print("Age: ", age)
print("Oxygen Level: ", oxygen_level)

#checking the patient priority based on the conditions

if critical_condition.upper() == "Y":
    print("Patient Priority: Immediate Treatment")
    print("Reason: Critical Condition")

elif oxygen_level < 90:
    print("Patient Priority: High Priority")
    print("Reason: Oxygen Level below 90")

elif age > 65:
    print("Patient Priority: Medium Priority")
    print("Reason: Senior Citizen")

else:
    print("Patient Priority: Normal Priority")
    print("Reason: Stable Condition")


#---------------------------------------output section-------------------------------------

"""
Sample Input Critical Condition (Y/N): N Age: 70 Oxygen Level: 94
Sample Output Patient Priority: Medium Priority Reason: Senior Citizen

Sample Input Critical Condition (Y/N): Y Age: 50 Oxygen Level: 85
Sample Output Patient Priority: Immediate Treatment Reason: Critical Condition"""
