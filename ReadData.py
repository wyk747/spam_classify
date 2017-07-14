import xlrd
import thulac
import re

class ReadData(object):

    def readData(self, trainNumber, testNumber):
        data = xlrd.open_workbook('spam.xls')
        table = data.sheets()[0]
        nrows = table.nrows
        dataList = []
        for i in range(nrows):
           d = table.row_values(i)
           dataList.append(d)

        return dataList[trainNumber:], dataList[:testNumber]

def replace(line):
    regex = re.compile("[^\\u4e00-\u9fa5a-zA-z0-9]")
    return regex.sub("", line)

text = '您好！我是航城南门兴达置业的小熊，买卖房子流程不清楚的可以咨询我，祝您及您的家人万福安康！万福安康！万福安康！重要的事情说三遍！'
text.strip().replace("\\pP|\\pS", "")
print(replace(text))
thu = thulac.thulac(filt=True, seg_only=True)
result = thu.cut(text)
print(result)



