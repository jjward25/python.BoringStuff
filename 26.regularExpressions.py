import re

# Passing a string value representing your regular expression to re.compile will return a regex object
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# a regex objects search() method will return non if the pattern is not found in the string
# if the object is found, the search() method returns a Match object, which has a group() method to return the actual matched text
mo = phoneNumRegex.search('My number is 415-555-4242')
print('Phone number found: ' + mo.group())
# here the results of the regex search are stored in variable 'mo' and can be accessed with the group() method

# With parentheses, you can create regex groups within one regex object
# The first set of parenthesis in a regex string will be group 1, the second will be group 2.  You can pass the integer 1 or 2 to the group() method and grab different parts of the matched text
# Passing 0 or nothing will return the entire matched text

phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())

# Using the plural 'groups' you can return all groups separated within a tuple
# You can then assign these tuple values to variable
print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

## the . ^ * + ? {} [] \ | () characters all have special meaning in regexes, so if you're searching for those exact characters you must use a backslash to 'escape' them
phoneNumRegex = re.compile(r'(\(\d\d\d\))(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415)555-4242.')  ## note a space between the 415) and 555 makes this break
print(mo.group(1))
print(mo.group(2))

# The pipe key | can be used to match one of many expressions.  It only returns the first match
# You can use findall() to find all matching occurrences
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

## Here we want to find any instance of Batman, Batmobile, Batcopter or Batbat
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel.')
print(mo.group())
print(mo.group(1))  ## first matches text in the parenthesis group

# Using a ? let's you make an optional match, meaning it will return a match on the rest of the expression whether that ? part is there or not
# The ? flags the group that precedes it, so here 'wo' is optional in the match
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

## Looking for numbers that do or do not have area codes
## again the ? basically means check for one or zero of the group preceding the ?
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())
mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())

## the * matches 0 or more.  The group can be absent or repeated over and over
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowowoman')
print(mo3.group())

## + means match one or more
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1 == None)
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

## Specify reptitions with {} ha{3} will match HaHaHa but not HaHa
## You can also specify a range in the braces {1,3} will match Ha, HaHa, and HaHaHa
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo2 = haRegex.search('Ha')
print(mo2 == None)

## Greedy vs Non-Greedy strings.  Pythons regexes are greedy by default, meaning they will match the longest string possible
## non-greedy (also called lazy) have a ? after the {}
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHaHa')
print(mo1.group())
nonGreedyRegex = re.compile(r'(Ha){3,5}?')
mo2 = nonGreedyRegex.search('HaHaHaHaHaHa')
print(mo2.group())
## {,n} returns from 0 to n of the preceding group... {n,} returns n or more or the preceding group

## Search only returns the first match, findall() returns all matching strings in a list as long as there are no groups in the regular expression
## If there are groups in the regex then findall() will return a list of tuples
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())
mo1 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo1)

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo2 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo2)
