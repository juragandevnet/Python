import pandas as pd
import openpyxl

Rule1 = ["6","IDJKTWR06","10.0.0.6","SERVER1","8.8.8.6","TCP","443"]
Rule2 = ["7","IDJKTWR07","10.0.0.7","SERVER2","8.8.8.7","UDP","80"]
Rule3 = ["8","IDJKTWR08","10.0.0.8","SERVER3","8.8.8.8","UDP","514"]
Rule4 = ["9","IDJKTWR09","10.0.0.9","SERVER4","8.8.8.9","TCP","443"]
Rule5 = ["10","IDJKTWR10","10.0.0.10","SERVER5","8.8.8.10","TCP","443"]

df = pd.DataFrame([Rule1,Rule2,Rule3,Rule4,Rule5],columns=['No','SourceHost','SourceIP','DestinationHost','DestinationIP','Protocol','Port'])
df.to_excel('BackupFirewallRules.xlsx',index=False)