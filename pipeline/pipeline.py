import sys
import pandas as pd

month = int(sys.argv[1]) # first argument is month num

df = pd.DataFrame({"day": [1, 2], "num_passengers": [3, 4]})
df['month'] = month
print(df.head())

df.to_parquet(f"output_{month}.parquet")
print(f"hi pipeline, month={month}")