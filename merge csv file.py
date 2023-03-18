import glob 
csv_files = sorted(glob.glob("*.{}".format('csv')))
#print(csv_files)

import pandas as pd
df_csv_merge= pd.concat([pd.read_csv(file) for file in csv_files],ignore_index=True)
#print(df_csv_merge)
l=[]
for f in csv_files:
    l.append(pd.read_csv(f))

df_res=pd.concat(l,ignore_index=True)
print(df_res)
#print(df_res.head())