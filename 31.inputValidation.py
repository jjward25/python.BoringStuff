## Input validation typically means repeatedly asking the user for input until they enter valid text

while True:
    print('Enter your age:')
    age=input()
    try:
        age=int(age)
    except:
        print('Please user numeric digits.')
        continue
    if age <0:
        print('Please enter a positive number.')
        continue
    break
print(f'Your age is {age}.')

## This manual writing could cause you to miss some cases
## PyInputPlus contains functions for several kinds of data: numbers, dates, emauls, addresses, and more.  Bad inputs will be prompted for re-entry like the code above
#### PyInputPlus is not part of the Python standard library and must be installed with pip
import pyinputplus as pyip
#response = pyip.inputStr(prompt='Enter a string (can be basically anything, like the traditional input method):')
response2 = pyip.inputNum(prompt='Enter a number (returns an int or a float depending on if the number has a decimanl in it):')
#response3 = pyip.inputChoice(prompt='Enter one of the provided choices:')
#response4 = pyip.inputMenu(prompt='Select one of the numbered options')
#response5 = pyip.inputDatetime(prompt='Enter a date and time:')
#response6 = pyip.inputYesNo(prompt='Enter yes or no:')
#response7 = pyip.inputBool(prompt='Enter True or False:')
#response8 = pyip.inputEmail(prompt='Enter a valid email address:')
#response9 = pyip.inputFilepath(prompt='Enter a valid filepath (can check if the file exists):')
#response10 = pyip.inputPassword(prompt='Similar to traditional input method but displays *s as the user types to protect sensitive information')

## pyinputplus also has min, max, greaterThan and lessThan arguments
response = pyip.inputNum('Enter num:',min=4)
response = pyip.inputNum('Enter num:',greaterThan=4)

## You can set blank=True to accept a blank input
response = pyip.inputNum('Enter num:',max=4, blank=True) ## blank=True means blank entries are allowed
## You can use limit and timeout to set a limit to the number of attempts and the limit in terms of seconds to answer
## allowRegex and blockRegex will set contraints based on the regex you pass to it
## pyip.inputCustom() to use a predefined function as parameters



