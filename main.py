import csv
import pandas as pd

file_path = 'files/data.csv'

## 普通にCSVを読み込む場合

# with open(file_path, 'r') as f:
#     reader = csv.reader(f)
#     header = next(reader)

#     print(header)

#     for row  in reader:
#         print(row)


## Pandasを使用して読み込む場合(こっちが良い)
df = pd.read_csv(file_path)
print(df)
print(df['date'])
