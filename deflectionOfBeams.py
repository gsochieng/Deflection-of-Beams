""" In this program we will determine the Modulus of Elasticity of Steel and Ensure that the clamping of a fixed beam works.  To determine Young's Modulus(E1):
    1. Input the beam's cross-section and length.  
    2. Determine its Second Moment of Area.
    3. Plot a graph of loading(w grams) Vs. Deflection (d, millimetres)
    4. Determine the slope of the graph.
    5. Use the derived deflectioin equaton to determine the modulus of Elasticity.
To ensure integrity of clamping of the fixed beam:
    1. Input the data
    2. Plot a graph of loading vs deflection
    3. Determine the slope of the graph
    4. Use the derived equation of delection of fixed beam with central point loading to determine the Young's Modulus.
    5. If the Young's Modulus obtained is equal to the initial one; then the clamping is effective.
"""
import math as m;
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal

print()
print("Beam geometric properties: ")
b = 25.36
h = 2.48
l = 846
print()
#Determination of the secondmoment of area
secondMomArea = (b *(h)**3)/12
print("The second moment of area a beam with a breadth %fmm and thickness %fmm is %fmm^4" %(b, h, secondMomArea))
#Determination of Young's Modulus
#SIMPLY SUPPORTED BEAM WITH CENTRAL POINT LOADING
load = [100, 200, 300, 400, 600, 800]
deflection = [0.65, 1.95, 3.31, 4.64, 7.92, 10.42]

#fitting the data in a straight curve
slope1, intercept= np.polyfit(deflection, load, 1)
#plotting the data as is 
plt.plot(deflection, load, 'o')
#graph labels
plt.title('Graph of Load(grams) Vs. Deflection(mm) for a Centrally Point Loaded Simply Supported Beam', fontsize=14)
plt.xlabel('Deflection(mm)', fontsize=12)
plt.ylabel('Load(g)', fontsize=12)
#plotting the straight line of best fit
loadFunction1 = np.poly1d(np.polyfit(deflection, load, 1))
plt.plot(deflection, loadFunction1(deflection))
#slope
print()
print("The slope is of simply supported graph is: ", end='')
print(slope1, end='g/mm\n')
#Calculation of Young's Modulus
eMod = ((l**3)/(48*secondMomArea))*slope1*9810
print("The Young's Modulus for a Simply Supported Steel Beam is: %dPa" %(Decimal(eMod)))
#plt.show()

#FIXED BEAM WITH CENTRAL POINT LOADING
#print("Fixed Beam with Central Point Loading")
loadFix = [100, 200, 300, 400, 600, 800, 1000]
defFix = [0.27, 0.53, 0.75, 1.02, 1.51, 1.99, 2.44]

#fitting the data in a straight curve
slope2, intercept = np.polyfit(defFix, loadFix, 1)
print("The slope of the fixed beam graph is: ", end='')
print(slope2, end='g/mm\n')

#plotting a line graph
plt.figure()
plt.plot(defFix, loadFix, 'o')
#graph labels
plt.title("Graph of Load(grams) Vs. Deflection(mm) for a Centrally Point Loaded Fixed Beam", fontsize=14)
plt.xlabel('Deflection(mm)', fontsize=12)
plt.ylabel('Load(g)', fontsize=12)
#plotting the straight line of best fit
loadFunction2 = np.poly1d(np.polyfit(defFix, loadFix, 1))
plt.plot(defFix, loadFunction2(defFix))
eMod2 = ((l**3)/(48*secondMomArea))*slope2*9810
print("The Young's Modulus for a Fixed Steel Beam is: %dPa" %(Decimal(eMod2)))
#showing the graphs
#plt.show()
#CONCLUSION
print()
print("CONCLUSION FROM THE EXPERIMENT")
if eMod != eMod2:
    print('The clamping is NOT effective!!!')
elif eMod == eMod2:
    print('The clamping is effective.')

plt.show()
