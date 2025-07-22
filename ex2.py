import csv
import pandas as pd

df=pd.read_csv ('IntroToPy/mountains_db.tsv', delimiter='\t')
print (df.to_string ())