# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 13:53:39 2021

@author: gperr
"""
print("for a line (y=mx+b) enter numbers in the format: m b ")
print("and python Returns the value of x when y=0")
print("you can find the intercept for multiple functions in the format: m b m2 b2 m3 b3 ..mn bn")
input_number = input().split()
#print("[m, b]")
#print(input_number)

n=int(len(input_number))

if n%2 == 0 :ArithmeticError 
    
else :
    print("Error: missing values in input")
count = 0
paircount = 0
while (count < n):
    m = input_number[0+int(count)]
    b = input_number[1+int(count)]
    count= count + 2
    paircount = paircount + 1
    x = -float(b)/float(m)
    
    print(paircount)
    
    print("y=0 : x="),print(x)