import os
import pandas as pd

directory = "archive"

filename = "0"
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        # print(f)
        read = pd.read_csv(f, index_col='Date', parse_dates=True)
        col1 = []
        col2 = []

        col1 = read.loc[:, "Close"]
        col2 = read.loc[:, "Last"]
        col3 = read.loc[:, "High"]
        col4 = read.loc[:, "Low"]
        x = len(col1)
        col3 = [0] * x

        for i in range(0, x):

            col3[i] = abs(
                ((col1[i] / col2[i])) / ((col3[i] - col4[i]) / col1[i]))
        s = pd.Series(col3)
        read['sharpe'] = s.values
        # read.insert(15, "Nerornwsf", col3, True)
        f = os.path.join("directory", filename)
        read.to_csv(f'{f}')
        print(read)
        # for pp in read:
        #     print(pp['Last'])