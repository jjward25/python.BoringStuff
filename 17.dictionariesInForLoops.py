# Dictionaries don't work like lists but you can create list-like items for for loops

spam = {
    'color':'red',
    'age':42
    }

for k in spam.keys(): 
    print(k)

for v in spam.values(): 
    print(v)

for i in spam.items():
    print(i)

for k,v in spam.items():
    print(k + ' is ' + str(v))

# To create a true list
list(spam.keys())

# To check for keys and values
# for keys
'color' in spam
'color' in spam.keys()
# for values
42 in spam.values()


## The Get method takes two parameters, the key you want the valie for, and a default value if the key doesn't exist
picnicItems = {
    'apples': 5,
    'cups': 2
}
print(picnicItems.get('cups',0)) # Prints 2 because cups exists
print(picnicItems.get('eggs',0)) # Prints 0 because eggs doesn't

# setDefault adds a key:value pair if it doesn't exist, otherwise it returns the value of that existing key
picnicItems.setdefault('apples',6)
picnicItems.setdefault('oranges',4)
print(picnicItems)

# TO create an object that counts various values as it goes
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1
print(count)

# You can import pprint to to prettyprint an object
import pprint
pprint.pprint(count)