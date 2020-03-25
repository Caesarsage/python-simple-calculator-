print("Welcome to a Simple Area Of A Circle Calculator")

#Collecting Details
radius = input("Please, input your radius:  ")
radius_interger = int(radius)
radius_unit = input("(cm ) or  (m): ")

#Formula and Constant
constant_pi = 22/7
area = constant_pi * radius_interger**2 

#Condictions
if radius_unit.lower() == "cm":
    print(f"The area of the circle is {area}{radius_unit}\N{SUPERSCRIPT TWO}")
else:
    print(f"The area of the circle is {area}{radius_unit}\N{SUPERSCRIPT TWO}")

#\N{SUPERSCRIPT} is Unicode formatting supported by python 3.3 and higher