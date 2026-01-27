import numpy as np
import pandas as pd

# load the data
df = pd.read_csv("houses.csv")
df

# let's also test pandasGUI
# pip install pandasGUI
from pandasgui import show

# uncomment this in order to run pandasGUI instead
show(df)

# run this file in console:
# python pandasguitest.py