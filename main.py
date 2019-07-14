import csv
# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 対象のファイルパスを選択
file_path = 'files/data.csv'

## Pandasを使用して読み込む場合
# df = pd.read_csv(file_path)
# print(df)
# print(df['date'])

## 普通にCSVを読み込む場合

with open(file_path, 'r') as f:
    # ファイルを読み込む
    reader = csv.reader(f)
    # ヘッダ行を除く
    header = next(reader)

    # print(header)
    # リスト型に辞書型を格納する
    sum_list = []
    date_list = []
    for row  in reader:
        # sum_dict = {}
        # 合計を算出する
        sum = int(row[1]) + int(row[2]) + int(row[3]) + int(row[4])
        # sum_dict[row[0]] = sum
        # sum_list.append(sum_dict)
        sum_list.append(sum)
        date_list.append(int(row[0]))

        
# 辞書型に想定どおりに入っていることを確認
# print(sum_list)

sum_ary = np.array(sum_list)
date_ary = np.array(date_list)

plt.plot(date_ary, sum_ary)
plt.show()