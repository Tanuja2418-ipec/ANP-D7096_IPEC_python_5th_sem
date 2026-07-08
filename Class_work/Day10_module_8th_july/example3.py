#importing module
from numeric_calculation import calculate_addition, calculate_remainder

#----------------------------------------------------------------

a = 20
b = 5
print("Sum of ",a,"and ",b,"is: ",calculate_addition(a,b))
print("----------------------------------------------------")

#----------------------------------------------------------------

x= 15
y= 3
print("Difference of ",a,"and ",b,"is: ",calculate_difference(a,b))
print("----------------------------------------------------")


#----------------------------------------------------------------


#---------------------------output section---------------------------


"""
Sum of  20 and  5 is:  25
----------------------------------------------------
Traceback (most recent call last):
  File "D:\ANP-D7096_IPEC_python-5th_sem\Class_work\Day10_module_8th_july\example3.py", line 15,in <module>
    print("Difference of ",a,"and ",b,"is: ",calculate_difference(a,b))
                                             ^^^^^^^^^^^^^^^^^^^^
NameError: name 'calculate_difference' is not defined
"""


