
import pandas as pd
import glob, os

files = glob.glob('files/*.txt')
print (files)

df = pd.concat([pd.read_table(fp).assign(New=os.path.basename(fp)) for fp in files])
print (df)
