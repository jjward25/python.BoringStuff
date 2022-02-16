## \d any numeric digit from 0 to 9
## \D Any character that is not a numeric digit from 0 to 9
## \w Any letter, numeric digit, or the underscore character
## \W Any character that is not a letter, numeric digit, or the underscore character
## \s Any space, tab, or newline character (matching "space" type characters)
## \S Any character that is not a space, tab or newline
## [0-5] will only match the digits 0-5; easier than writing (0|1|2|3|4|5)

import re
from turtle import begin_fill
xmasRegex = re.compile(r'\d+\s\w+')  ## matches text with one or more numeric digits followed by a whitespace character, folowed by one or more letter/digit/underscore characters, then cuts it at the comma character bc it's not searching for that
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo)

## You can make your own character class with square brackets
## There is no shorthand that only matches letters, but you can use the [a-zA-Z] class
vowelRegex = re.compile(r'[aeiouAEIOU]')  ## matches any vowel lower caser or upper case
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)
 ## [a-zA-Z0-9] would match all letters and digits
 ## the special symbols aren't special in the square brackets, they're taken literally
 ## [0-5.] will match digits 0,1,2,3,4,5 and the '.' character.. you don't need to escape it with [0-5\.]

## Placing a ^ just inside the opening bracket will make it a negative character class (matches everything not in the class)
consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)


## You can start a regex with the ^ to indicate the match must occur at the start of the searched text
## Ending with a $ indicates the string must end with this regex pattern
## using them both together indicates the entire string should match the regex exactly, the match shouldn't be based on a subset of data
beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search('Hello World!')
mo2 = beginsWithHello.search('He said Hello World!')
print(mo)
print(mo2)

endsWithNumber = re.compile(r'\d$')
mo = endsWithNumber.search('Your number is 42')
mo2 = endsWithNumber.search('Your number is forty two.')
print(mo)
print(mo2)

wholeStringIsNum = re.compile(r'^\d+$')
mo = wholeStringIsNum.search('1234567890')
mo2 = wholeStringIsNum.search('Text123')
print(mo)
print(mo2)

## The . character is the Wildcard character and will matching anything except newline
atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)
## the . character only matches one character so flat is only returned as 'lat'

## You can match everything with .*
## ie: If you want to match 'First Name:' followed by anything
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))
print(mo.group())
## The .* is greedy and will always try to match as much text as possible.
## To match in a non-greedy way use .*?
nonGreedyRegex = re.compile(r'<.*?>')
mo = nonGreedyRegex.search('<To serve> for dinner.>')
print(mo)
print(mo.group())
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve> for dinner.>')
print(mo)
print(mo.group())
## Both are basically saying "Match an opening angle bracket followed by a closing angle bracket" but one will take the first closer and the other will take the last >


## Matching newlines with the . character, which typically matches everything but newlines
noNewlineRegex = re.compile('.*')
mo = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(mo)
newlineRegex = re.compile('.*',re.DOTALL)
mo = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(mo)  ## re.DOTALL as a second argument makes the . character match ALL characters


## to make string searches case insensitive, pass the re.IGNORECASE or re.I as a second argument to re.compile()
robocop = re.compile(r'robocop',re.I)
mo = robocop.search('RoboCop protects the innocent')
print(mo.group())

## You can find text and substitute it with new text.  
## The first argument is the string to replace any matches, the se
namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.sub('CENSORED','Agent Alice gave the secret documents to Agent Bob.')
print(mo)

## You can use the matched text in the substitution if needed
agentNamesRegex = re.compile(r'Agent (\w)\w*') ## looks for Agent [Name], but groups out the first letter of the agent's name
mo = agentNamesRegex.sub(r'\1****','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(mo)


## for complex regex expressions, you can enable Verbose mode so you can leave notes inside
## re.VERBOSE ignores whitespace and comments in regex expressions
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4} (\s*(ext|x|ext.)\s*d{2,5})?)')

phoneRegex = re.compile(r'''
((\d{3}|\(\d{3}\))? # area code
(\s|-|\.)? # seperator
\d{3} # first 3 digits
(\s|-|\.) #separator
\d{4} #last 4 digits
 (\s*(ext|x|ext.)\s*d{2,5})? #extension
 )''',re.VERBOSE)


## If you want to use multiple second arguments, you have to use the pipe | character
someRegexValue = re.compile('foo',re.IGNORECASE|re.DOTALL|re.VERBOSE)

