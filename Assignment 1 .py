#!/usr/bin/env python
# coding: utf-8

#     Adult Body Mass Index Calculator
Wt = int(input("Enter your weight(in Kg): "))
Ht = float(input("Enter your Height(in meters): "))
BMI = Wt/Ht
print("Body Mass Index (BMI): ",BMI)



#     Ride Cost Calculator
Travel = float(input("Enter distance traveled: "))
Cost_D = float(input("Enter Cost of Diesel per litre: "))
Avg_Fuel = int(input("Enter your vehicle Fuel Average(in km/litre): "))
Fuel_used = Travel / Avg_Fuel
Total_cost = Cost_D * Fuel_used
print("Total cost of driving per day to office: INR",Total_cost)




