name=''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')


while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

# The / is a line continuation command, so if you have a long line of code that you want to break into two lines, just put a / at the end of the first line