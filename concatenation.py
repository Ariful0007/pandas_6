import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import  style
style.use("fivethirtyeight")

df1=pd.DataFrame({"HPI":[80,90,60,70],"Int_rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},
                 index=[2001,2002,2003,2004])
df2=pd.DataFrame({"HPI":[80,90,60,70],"Int_rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},
           index=[2005,2006,2007,2008])

con_cat=pd.concat([df1,df2])
#con_cat.plot()
#df2.plot()
#plt.show()
print(con_cat)
