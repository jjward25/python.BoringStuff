## Count the number of items with the same key in nested objects

allGuests = {
    'Alice':{'apples':5,'pretzels':12},
    'Bob':{'ham sandwiches':3,'apples':2},
    'Carol':{'cups':3,'apple pies':1}
}

def totalBrought(guests,item):
    numBrought = 0
    for k,v in guests.items():
        numBrought = numBrought + v.get(item,0)
    return numBrought

print('Number of items bought:')
print(' - Apples: ' + str(totalBrought(allGuests,'apples')))

## Looping through an object to show videogame inventory
stuff = {'rope':1,'torch':6,'gold coin': 42,'dagger':1}
def ownedStuff(stuff):
    for k,v in stuff.items():
        print(str(v) + ' ' + k)
print(ownedStuff(stuff))