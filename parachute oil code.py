import pandas as pd
from scipy import stats
data  = pd.read_excel("C:/Users/VICKY R R/Desktop/parachute oil data.xlsx")
data.Male.describe()
data.Male.describe()
stats.ttest_ind(data.Male,data.Female )
