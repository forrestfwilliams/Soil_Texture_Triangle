# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 15:04:09 2020

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

# Draw Boundary and Gridlines
tax.boundary(linewidth=2.0)
tax.gridlines(color="black", multiple=10)

fontsize = 10
#tax.set_title("Texture Triangle\n", fontsize=fontsize)
tax.left_axis_label("Clay %", fontsize=fontsize, offset=0.14)
tax.right_axis_label("Silt %", fontsize=fontsize, offset=0.14)
tax.bottom_axis_label("Sand %", fontsize=fontsize, offset=0.07)

# Set ticks
tax.ticks(axis='lbr', linewidth=0.1)

# Remove default Matplotlib Axes
tax.clear_matplotlib_ticks()
tax.get_axes().axis('off')

ternary.plt.show()