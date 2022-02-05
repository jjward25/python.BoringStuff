#You define a function and then call it.  You can use parameters.  In this case hello() is the function and name is the parameter.
def hello(name):
    print ('Hello ' + name)

#hello('Alice')

# magic 8 ball -- create a function getAnswer w a parameter answerNumber.  Then create a variable that gives you a random int from 1-9
# and pass that random int as the answerNumber parameter
# !! you use the retun keyword, otherwise python adds return None to the end of any function without a return statement.  
# spam = print('Hello!')
# spam == None will evaluate to True
import random

def getAnswer(answerNumber):
    if answerNumber==1:
        return 'It is certain'
    elif answerNumber==2:
        return 'It is decidedly so'
    elif answerNumber==3:
        return 'Yes'
    elif answerNumber==4:
        return 'Reply hazy try again'
    elif answerNumber==5:
        return 'Ask again later'
    elif answerNumber==6:
        return 'Concentrate and ask again'
    elif answerNumber==7:
        return 'My answer is no'
    elif answerNumber==8:
        return 'Outlook not so good'
    elif answerNumber==9:
        return 'Very doubtful'
    
r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)

## you can disable the newline that gets added after every print line
print('Hello', end='')
print('World')

