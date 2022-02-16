import pyperclip
import re

text = pyperclip.paste()
phoneNumberList =[]
emailList = []
allMatches = []

phoneNumRegEx = re.compile(r'''
((\d{3}|\(\d{3}\))? # area code
(\s|-|\.)? # seperator
(\d{3}) # first 3 digits
(\s|-|\.) #separator
(\d{4}) #last 4 digits
(\s*(ext|x|ext.)\s*(d{2,5}))? #extension
)''',re.VERBOSE)

print(phoneNumRegEx.findall(text))
for groups in phoneNumRegEx.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    print(phoneNum)
    if groups[8] != '':
        phoneNum += 'X' + groups[8]
    phoneNumberList.append(phoneNum)
    allMatches.append(phoneNum)
print(phoneNumberList)

emailRegEx = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # username
    @
    [a-zA-Z0-9.-]+ # domain
    (\.[a-zA-Z]{2,4}) #dot something
)''',re.VERBOSE)

print(emailRegEx.findall(text))

for groups in emailRegEx.findall(text):
    emailList.append(groups[0]) ## Group 0 always matches the entire regular expression
    allMatches.append(groups[0])
print(emailList)

# copyresults to clipboard
if len(allMatches) > 0:
    pyperclip.copy('\n'.join(allMatches))
    print('Copied to Clipboard: ')
    print('\n'.join(allMatches))
else:
    print('No phone numbers or e-mails found.')