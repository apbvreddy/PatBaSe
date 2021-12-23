import pandas as pd
import openpyxl

df= pd.read_excel('excel_sheets.xlsx', sheet_name='Results',
    header=23,usecols = "B,D,E,I,J,N:V")

df.to_csv('bvb.csv')
