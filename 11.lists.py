# lists contain multiple values in one variable.  Lists can contain other lists
# list items can be accessed by their index number 
# you can also start from the end by using a negative index... [-1] pulls the last item in the list

spam = ['cat','rat','bat']
print(spam[0])

# Using slice you can pull several values from a list.  A slice looks like an integer but with a range separated by a colon
# Slices start at 0 like indexes, but end one beyond the normal index list (3 instead of 2 for this list).  It returns >= to the first index number and < the second.

print(spam[1:3])

# You can get the length of a list (# of list items)
print(len(spam))

# You can re-assign a specific value by using the index
spam[0] = 'gnat'
print(spam)

# You can add or duplicate values within strings as well
can = ['dog','frog']
combo = can + spam
print(combo)
print(can * 3)

# To remove a value use del
del combo[4]
print(combo)

# For loop with a list
for i in combo[1:2]:
    print(i)

# Check for a value with in and 'not in'
print('dog' in spam)
print('dog' in combo)

# Multiple Assignment (also known as tuple unpacking)
# You have to use the same amount of variable as list items, then you can auto assign list items to variables in one line
cat = ['fat','gray','loud']
size, color, disposition = cat
print(size) ## returns fat

# Working with lists
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames)+1) + ' (Or enter nothing to stop):')
    name = input()
    if name =="":
        break
    catNames = catNames + [name]
print('The cat names are:')
for name in catNames:
    print('' +name)


## When you assign a new variable as a copy of a list, they both still share the same values.  Updating one will update both.
spam = [0,1,2,3,4,5]
cheese = spam
cheese[1] = 'Hello!'
print(spam)

## Use copy() to create a true duplicate that can be edited without affecting the original (like if a function uses a list)
## If the list you need to copy contains lists, use copy.deepcopy() to copy underlying lists too
import copy
jerry = copy.copy(spam)

