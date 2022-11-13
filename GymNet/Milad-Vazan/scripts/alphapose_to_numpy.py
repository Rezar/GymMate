import os
import pandas as pd
dataset = pd.read_csv('1.csv')
for index, row in dataset.iterrows():
    dirname = row["folder_add"]
    dn = row["name"]
    p= f"{dirname}"
    pn=f"{dn}"
    df = pd.read_json(p)
    A=[]
    for i in range (len(df.keypoints)):
        A.append(df.keypoints[i])
    arr = np.array(A)
    np.save(pn, arr)
