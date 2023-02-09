import pandas as pd
from prettytable import PrettyTable

df = pd.read_excel('BackupFirewallRules.xlsx')
df = df.values.tolist()

table = PrettyTable(['No','SourceHost','SourceIP','DestinationHost','DestinationIP','Protocol','Port'])

for i in range(len(df)):
    table.add_row([df[i][0],df[i][1],df[i][2],df[i][3],df[i][4],df[i][5],df[i][6]])
print(table)

