# Author: IBN (AMDG) 10/14/2021

p_inv = float(input("What is your initial investment amount? "))
rate = float(input("What is the annual interest rate as a percent? "))
years = int(input("How many years is the investment in the account? "))

rate /= 100

future_value = p_inv * ((1 + (rate / 12)) ** (12 * years))
print("The future value of the investment after " + str(years) + " year(s) is: " + str(future_value))
