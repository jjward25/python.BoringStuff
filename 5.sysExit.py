import sys
# sys.exit() terminates the code

from urllib import response

while True:
    print('Type exit to exit.')
    response=input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')