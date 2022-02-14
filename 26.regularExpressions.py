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