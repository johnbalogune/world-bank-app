import pandas as pd
from pandas_datareader import wb

df = wb.get_indicators()[['id','name']]
df = df[df.name == 'Proportion of seats held by women in national parliaments (%)']
print(df)
