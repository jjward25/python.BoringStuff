print('My name is')
for i in range(5):
    print('Jimmy five times (' + str(i) + ')')

# the variables are running from 0 through 4 (the first 5 ints)

total = 0
for num in range(101):
    total = total + num
print(total)

# doing it with a while loop
print ('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i=i+1

#for loops can count down with the range function as well
for i in range (5,-1,-1):
    print(i)