# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 12:35:00 2026

@author: aidan
"""
#Straight line: y1 = -0.5 x + 4.0, 
#Parabola: y2 = -0.29 x 2 - x + 12.5
#More Complicated function: y3 = 1.0 + 10*(x + 1.0)*exp(-x2)
#y1: 40.0
#y2: 100.83
#y3: 27.72

import numpy as np
import matplotlib.pyplot as plt

def y1(x): 
    return -0.5*x + 4.0
def y2(x):
    return -0.29*x**2 - x + 12.5
def y3(x):
    return 1.0 + 10*(x + 1.0)*np.exp(-x**2)
#all of these are def functions that i made to make it easier to call the equations.
#Midpoint rule. very simple calc 2: x = (b - a)/n.
#AREA UNDER THE CURVE +60 points RAHHHHH
def midpoint(f,a,b,n): #calling a and b here allows this assignment to go above -5.0 and 5.0 if someone wants to use it :)
    dx = (b - a)/n #rectangle width calculation
    x = np.arange(a + dx/2, b, dx) #starts at midpoint, ends at b, steps by dx as its the amount intervals should increase by.
    return np.sum(f(x)*dx) #same thing as f(x)dx
"""z = midpoint(y1,-5.0,5.0,40)
print(z) #it works!"""

#now the percent difference section
#Input Section of code, so I get that +10 from input section :P
a = -5.0
b = 5.0
print("Area under the Curve:")
print(f"   Interval of the area under the curve is [{a},{b}]")
n = int(input("     Enter number of rectangles n: "))
dx = (b - a) / n
print(f"        dx = (b - a)/n, the dx is: {dx}")
#kind of messy but gets the job done.

#I List all the areas here.
A1 = midpoint(y1, a, b, n)
A2 = midpoint(y2, a, b, n)
A3 = midpoint(y3, a, b, n)

#Percent difference
def percent_diff(approx, actual):
    return abs(approx - actual) / actual * 100.0
pd1 = percent_diff(A1, 40.0)
pd2 = percent_diff(A2, 100.83)
pd3 = percent_diff(A3, 27.72)

print("\nResults:")
print("\ny1 area =", A1, "percent diff =", pd1)
print("\ny2 area =", A2, "percent diff =", pd2)
print("\ny3 area =", A3, "percent diff =", pd3)

#The Trend Figure: THIS TOOK ME SO LONG A LOT OF GOOGLING TO GET THIS TO WORK GAHHH

dx_list = [] 
pd1_list = []
pd2_list = []
pd3_list = []

for n in range(1, 1001): #I did all this on my own.

    dx = (b - a) / n

    A1 = midpoint(y1, a, b, n)
    A2 = midpoint(y2, a, b, n)
    A3 = midpoint(y3, a, b, n)

    pd1 = percent_diff(A1, 40.0) 
    pd2 = percent_diff(A2, 100.83)
    pd3 = percent_diff(A3, 27.72)

    dx_list.append(dx)
    pd1_list.append(pd1) 
    pd2_list.append(pd2)
    pd3_list.append(pd3)

#did the rest.
plt.ylim(0,100)
plt.plot(dx_list, pd1_list, label= "y1") #y1 does not show up because there is 0.0 percent difference.
plt.plot(dx_list, pd2_list, label= "y2") #y2
plt.plot(dx_list, pd3_list, label= "y3") #y3 
plt.xlabel("dx")
plt.ylabel("Percent Difference (%)")
plt.title("Percent Difference Trend")
plt.legend()
plt.show()
plt.savefig("example_figure.png")
#Hope you like! PLEASE give me details on areas where I can improve because this one was a bit more messy. 
#Coding seems like a very useful tool and I would like to learn more.
#SO PLEASE I WOULD LOVE TO HEAR OTHER WAYS I COULD'VE DONE THIS LAB.