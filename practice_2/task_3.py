# -*- coding: utf-8 -*-
"""
Write a program to calculate the body mass index (BMI) of a person. The user must enter their height and weight, after which you use one of the formulas below to determine the index.
BMI = weight/height**2 
"""
weight = int(input("Enter your weight in kg: "))
height = int(input("Enter yout height in cm: "))
BMI = weight/(height*height)*10000
#multiplying by 10000 for the correct metric
print("Your BMI is: ",BMI)


