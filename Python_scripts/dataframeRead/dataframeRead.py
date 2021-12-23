
import pandas as pd

def parsingtheExportedXlsxFile(self, excelFilePath, sheetName='Results'):
    excelDf = pd.read_excel(excelFilePath, sheet_name= sheetName)
    sliceIndex = 23
    for index, row in excelDf.iterrows():
        if row[0] == "Well":
            sliceIndex = index 
            break                
    
    tempDf = excelDf[sliceIndex:]      
    headers = tempDf.iloc[0]
    edsExportedFileDF = pd.DataFrame(tempDf.values[1:], columns=headers)  # creating a dataframes
    
    return edsExportedFileDF

