
import pandas as pd
import sys
filename = sys.argv[1]
fname,sfix=filename.split(".")

def parsingtheExportedXlsxFile(self, excelFilePath, sheetName=filrname):
    excelDf = pd.read_excel(excelFilePath, sheet_name= sheetName)
    sliceIndex = 20
    for index, row in excelDf.iterrows():
        if row[0] == "Well":
            sliceIndex = index 
            break                
    df.to_csv(fname+".csv")
