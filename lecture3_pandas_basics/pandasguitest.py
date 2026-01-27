import numpy as np
import pandas as pd

# load the data
df = pd.read_csv("houses.csv")

# note: pandasgui might not work with MacOS (use dtale instead)
# for MacOS: check -> https://www.kdnuggets.com/2023/06/revolutionizing-data-analysis-pandasgui.html
# in pandasgui: right-click a column to select color by column

# let's also test pandasGUI
# pip install pandasGUI
from pandasgui import show

# uncomment this in order to run pandasGUI instead
show(df)

# run this file in console:
# python pandasguitest.py