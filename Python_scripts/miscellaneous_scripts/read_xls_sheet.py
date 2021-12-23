import glob
import openpyxl
from pathlib import Path

xlsx_file = 'excel_sheets.xlsx'
wb_obj = openpyxl.load_workbook(xlsx_file) 

# Read the active sheet:
sheet = wb_obj.AmplificationData
print(sheet)
