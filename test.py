import pandas as pd


tab = pd.read_csv('https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv')
tab.to_csv("tocsv.csv")

