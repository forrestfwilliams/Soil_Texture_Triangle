# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 10:44:17 2020

@author: 4rest
"""
import matplotlib
import matplotlib.pyplot as plt
import ternary

matplotlib.rcParams['figure.dpi'] = 200
matplotlib.rcParams['figure.figsize'] = (3.5, 3.5)

## Boundary and Gridlines
scale = 100
figure, tax = ternary.figure(scale=scale)
# figure.set_size_inches(6, 6)

# Draw Boundary and Gridlines
tax.boundary(linewidth=1.5)
#tax.gridlines(color="black", multiple=10, linewidth=0.25)

# Set Axis labels and Title
fontsize = 10
axisfont = 6
labelfont = 6
#tax.set_title("Texture Triangle\n", fontsize=fontsize)
tax.left_axis_label("Clay %", fontsize=fontsize, offset=0.14)
tax.right_axis_label("Silt %", fontsize=fontsize, offset=0.14)
tax.bottom_axis_label("Sand %", fontsize=fontsize, offset=0.10)

# Set ticks
tax.ticks(axis='lbr', linewidth=1, clockwise=True, multiple=10, fontsize=axisfont, offset=0.03)

#Line list
lines = [[[ 0,55,45], [28,27,45]],
         [[15,40,45], [60,40, 0]],
         [[40,60, 0], [40,40,20]],
         [[40,40,20], [53,27,23]],
         [[28,27,45], [73,27, 0]],
         [[50,27,23], [50, 0,50]],
         [[80,12, 6], [88,12, 0]],
         [[80,12, 6], [80, 0,20]],
         [[40, 8,52], [50, 8,42]],
         [[40, 8,52], [28,20,52]],
         [[28,20,52], [28,27,45]],
         [[28,20,52], [ 0,20,80]],
         [[ 0,15,85], [30, 0,70]],
         [[ 0,10,90], [14, 0,86]],
         [[ 0,35,65], [20,35,45]]]
for points in lines:
    tax.line(points[0], points[1], linewidth=0.5, color='black',solid_capstyle='round')

# Soil texture name
# (silt,clay,sand)
labels = [{'text':'clay', 'position':[17,60]},
    {'text':'silty\nclay', 'position':[46,42]},
    {'text':'silty clay\nloam', 'position':[51,30]},
    {'text':'sandy\nclay', 'position':[3,38]},
    {'text':'clay loam', 'position':[25,33]},
    {'text':'sandy clay\nloam', 'position':[7,24]},
    {'text':'loam', 'position':[37,17]},
    {'text':'silt loam', 'position':[60,13]},
    {'text':'silt', 'position':[85,5]},
    {'text':'sandy loam', 'position':[13,10]},
    {'text':'loamy sand', 'position':[5,1], 'rotation':-30},
    {'text':'sand', 'position':[2,1], 'rotation':-30}]
for label in labels:
    tax.annotate(**label, fontsize=labelfont)

# Remove default Matplotlib Axes
tax.clear_matplotlib_ticks()
tax.get_axes().axis('off')

ternary.plt.show()

