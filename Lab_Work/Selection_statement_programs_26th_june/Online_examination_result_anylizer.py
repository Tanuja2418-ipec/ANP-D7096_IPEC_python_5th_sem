"""--------------------------online Examination Result Analyzer---------------------------------- 
Problem Statement A student appears in 5 subjects.
 Rules: 
 • Minimum 40 marks in every subject to pass.  
 • Distinction → Average ≥ 75  
 • First Division→ Average ≥ 60  
 • Second Division → Average ≥ 50  
 • Pass  → Average ≥ 40  
 • Fail if any subject score < 40  
 
 Sample Input 
 Hindi : 85 
 English : 78 
 Mathematics : 82 
 Science : 75 
 Computer : 90 
 
 Sample Output 
 Average Marks: 82.0 
 Result: PASS Classification: Distinction """


#-------------------------------coding section--------------------------------

#take inputs from the user
hindi = float(input("Enter the marks of Hindi: "))
english = float(input("Enter the marks of English: "))
mathametics = float(input("Enter the marks of mathametics: "))
science = float(input("Enter the marks of science: "))
computer = float(input("Enter the marks of computer: "))

average = (hindi+english+mathametics+science+computer)/5



#displaying the input to the user 
print("Hindi : ", hindi)
print("English : ", english)
print("Mathametics : ", mathametics)
print("Science : ", science)
print("Computer : ", computer)

print("Average : ", average)


#checking the pass classification
if average >= 75:
    print("PASS Classification: Distinction")
elif average >= 60:
    print("PASS Classification: First Division")
elif average >= 50:
    print("PASS Classification: Second Division")
elif average >= 40:
    print("PASS Classification: Pass")
else:
    print("Fail")
    