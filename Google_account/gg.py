# install
# pip install ipenpyxl
import openpyxl
# get value
def get_value(fileName, cellName):
  wbk = openpyxl.load_workbook(fileName)
  Sheet1 = wbk['Sheet1']
  wbk.close()
  return Sheet1[cellName].value
  
# update value
def update_value(fileName, cellName, newValue ):
  wbk = openpyxl.load_workbook(fileName)
  Sheet1 = wbk['Sheet1']
  Sheet1[cellName].value = newValue
  wbk.close()
  wbk.save(fileName)
fileName = '   '
cellName = '    '
