import pyperclip
import re

## Checking for Dates
dates = pyperclip.paste()
dateList = []
#print(dates)
dateRegex = re.compile(r'(\d\d)(\/)(\d\d)(\/)(\d\d\d\d)')
print(dateRegex.findall(dates))

for date in dateRegex.findall(dates):
    #print(date)
    if int(date[0]) < 31:
        if int(date[2]) <= 12:
            if int(date[4]) <2999:
                newDate = '/'.join([date[0],date[2],date[4]])
                dateList.append(newDate)
print(dateList)
