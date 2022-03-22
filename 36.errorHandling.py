##### Raise your own exceptions in code in try/except statements to catch potential bugs
def boxPrint(symbol, width, height):
    if len(symbol)!=1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Heigh must be greater than 2.')



##### You can also print the standard traceback errors that the system gives you
import traceback
try: 
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt','w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt')


##### USE Assertions to place logic that should hold true or trigger a bug
ages = [26,57,92,54,22,17,15,80,47,73]
ages.sort()
ages
assert ages[0]<=ages[-1] ## assert that the first age is <= the last age
## if this is true, nothing happens, otherwise everything stops
## assertions are for programmers and should be used to test code in development, they should be working when pushed to prod


##### You can import the logging module to display log messages on your screen as your program runs, and to make a record of custom messages that you write
## logging can be a better alternative to typing a bunch of print statements bc they can all be disabled globally with "logging.disable(logging.CRITICAL)"
## import logging
## logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')

## to log to a file
## logging.basicConfig(filename='myProgramLog.txt',level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
