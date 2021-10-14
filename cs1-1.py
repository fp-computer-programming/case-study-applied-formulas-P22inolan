# Author: IBN (AMDG) 10/14/2021

x1 = int(input("What is your first x coordinate?"))
x2 = int(input("What is your second x coordinate?"))
y1 = int(input("What is your first x coordinate?"))
y2 = int(input("What is your second x coordinate?"))

formula = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
print("The distance between the points is: " + str(formula))
