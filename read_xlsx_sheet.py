import pandas as pd 
import numpy as np 
# read excel in data frame 
df = pd.read_excel('4shusshi.xlsx') 
 
# convert a data frame to a Numpy 2D array 
np.asarray(df) 