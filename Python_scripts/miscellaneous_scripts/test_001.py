import pandas as pd
import openpyxl
#df = pd.read_excel('excel_sheets.xlsx', sheet_name = None)
#print(df)
#print(df.keys('Results','AmplificationData'))
#print(df.keys())
#print(df.values()) 
df= pd.read_excel('excel_sheets.xlsx', sheet_name='Results',
    header=23,usecols = "B,D,E,I,J,N:V")
#    skiprows = range(0,22),header=23,usecols = "B,D,E,I,J,R:V")
#df_s1[df_sheet_name1["Amp Status"].str.contains("Amp")==False]
#df_s2 = pd.read_excel('excel_sheets.xlsx', sheet_name='AmplificationData')
#print(df_sheet_name2)
#print(df[0:20])
#df.to_excel('bvb.xlsx')
df.to_csv('bvb.csv')
