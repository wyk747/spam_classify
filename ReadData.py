import xlrd
import thulac
import re

class ReadData(object):

    def __init__(self):
        self.thu = thulac.thulac(filt=True)

    def readData(self):
        table, nrows = self.readRowNum()
        dataList = []
        for i in range(nrows):
           d = table.row_values(i)
           filteUseless = self.replace(d[1])
           #cutedWords = self.cut(filteUseless)
           #d.append(cutedWords)
           dataList.append(d)
        return dataList

    def readFile(self):
        data = xlrd.open_workbook('spam.xls')
        return data

    def readRowNum(self):
        data = self.readFile()
        table = data.sheets()[0]
        nrows = table.nrows
        return table, nrows

    def replace(self, line):
        regex = re.compile("[^\\u4e00-\u9fa5a-zA-z0-9]")
        return regex.sub("", line)

    def cut(self, text):
        result = self.thu.cut(text)
        return result

    def dealData(self, trNumber, teNumber):
        dataSet = []
        data = self.readData()
        



trainData, testData = ReadData().readData(100, 100)
print(trainData)
