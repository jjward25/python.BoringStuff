# using a backslash lets you use an otherwise illegal character.  You can also use double quotes for a string to enable use of single quotes inside
spam = 'Say hi to Bob\'s mother.'  # \t is tab, \n is newline
print(spam)
# Raw strings ignore escape characters and print backslashes
print(r"That is Carol\'s cat")

# You can make multi-line strings with triple quotes ''' '''
print('''Dear Alice,
Line 2
Line 3''')

# You can use indexes and slices on strings
spam = "Hello, world!"
print(spam[0])  # returns H
print(spam[0:5])
print(spam[:4])

# In and Not In  also work
print('Hello' in 'Hello World')

# To avoid long concatenate strings, you can use string interpolation
name = 'Al'
age = 4000
#print('My name is %s. I am %s years old.' (name,age))

# .lower() and .upper() to lower case or capitalize 

# isX methods -- useful for valdiating user inputs

name.isalpha() # true if the name string consists only of letters and isn't blank
name.isupper() # true if it's an upper case string
name.isalnum() # true if alphanumeric string
name.isdecimal() # true if string is only numeric characters
name.isspace() # true if string is only spaces, tabs and newlines
name.istitle() # true if string consists only of words that begin with uppercase letters followed by all lower case


# Password validation
while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')

# string.startswith() and string.endswith() do exactly what you think they do
# join and split 
','.join(['cats,rats,bats'])
' '.join(['cats,rats,bats'])
'My name is Simon'.split() # returns a list of words, split by default at the spaces (or tabs or newlines)
'MyABCnameABCisABCSimon'.split('ABC') #returns the string without the ABCs

# .partition() creates a tuple with the before, the separator, and the after as values.  It only separates at the first occurrence of the separator though
'Hello World!'.partition('w') 
'Hello'.rjust(20," ")
'Hello'.center(20,'=')

# rstrip() and lstrip() remove characters 
# for spam='   Hello    ' ,  spam.strip()='Hello' and spam.lstrip()='Hello     '

# you can copy strings to your clipboard
import pyperclip
pyperclip.copy('Hello world!')
# if you copy something else to the clipboard from another program, python will print that
pyperclip.paste()
