# It's commmon to use range() and len() together to iterate through a list
supplies = ['pen','pencil','eraser','notebook']
for i in range(len(supplies)):
    print ('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# The enumerate function also returns the index and item
for index, item in enumerate(supplies):
    print ('Index ' + str(index) + ' in supplies is: ' + item)

# You can make a random selection from a list with random.choice()
import random
random.choice(supplies)

# Or re-order with random.shuffle()
random.shuffle(supplies)

# += is the same as using a variable twice
spam = 42
spam = spam + 1 # is the same as
spam += 1

# You can find the index by searching for the exact list item.  # If there are duplicates, the location of the first instance is returned
supplies.index('pen')

# Add values with .append()
supplies.append('moose')
print(supplies)

# Use insert to add something at a specific index
# Note you don't use supplies = supplies.insert() or append() -- their return values are 0, so you just run the command and it modifies the list in place.
supplies.insert(1,'goose')
print(supplies)

# Sort lists of numbers or strings with sort().  You cannot sort a list that has both. 
# Don't save the variable value here either, it modifies the list in place
# By default, sort puts lower case strings behind upper case strings.  So the first a work comes after the last Z word.  Use list.sort(key=str.lower) to avoid this (it doesn't actually change the lsit values)
numbers = [1,5,32,-7,14]
numbers.sort()
print(numbers)
numbers.sort(reverse=True) #this sorts in reverse order

# Remove the first instance of a value with .remove()
numbers.remove(1)
print(numbers)

supplies.reverse() #reverses the list order
