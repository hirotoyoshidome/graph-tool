import sys
import csv
import json
# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# matplotlibで出力
def show_sum(date_list, sum_list):
    # 変換する
    sum_ary = np.array(sum_list)
    date_ary = np.array(date_list)
    # プロットする
    plt.plot(date_ary, sum_ary)
    # 出力する
    plt.show()

# JSONで出力
def print_json(dict):
    print(json.dumps(dict, sort_keys=True, indent=4))


## main実行

# 引数リスト
# help, sum, json

args = sys.argv
flg = 0
# print(len(args)) args[0]には実行ファイル名が入るみたい
if len(args) == 1:
    print("引数を設定してください")
    print("[sum, json]")
    exit(1)

# 引数判定(help, sum, json)
# 第二引数以降は無視する
if "help" == args[1]:
    print("help")
    print("引数は[sum, json]いずれかで指定してください")
    exit(0)
elif "sum" == args[1]:
    print("sum")
    flg = 1
elif "json" == args[1]:
    print("json")
    flg = 2
else:
    print("引数エラーです")
    print("引数は[sum, json]いずれかで指定してください")
    print("困った場合はhelpをください")
    exit(0)

# 対象のファイルパスを選択
FILE_PATH = 'files/data.csv'

## Pandasを使用して読み込む場合
# df = pd.read_csv(FILE_PATH)
# print(df)
# print(df['date'])

## 普通にCSVを読み込む場合(withを使うと安全に読み込める)
with open(FILE_PATH, 'r') as f:
    # ファイルを読み込む
    reader = csv.reader(f)
    # ヘッダ行を除く
    header = next(reader)
    # 変数宣言
    sum_list = []
    date_list = []
    json_dict = {}
    for row  in reader:
        # 合計を算出する
        sum = int(row[1]) + int(row[2]) + int(row[3]) + int(row[4])
        sum_list.append(sum)
        date_list.append(int(row[0]))
        json_dict[row[0]] = sum

if flg == 1:
    show_sum(date_list, sum_list)
elif flg == 2:
    print_json(json_dict)
