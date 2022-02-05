import random, time, copy
WIDTH = 60
HEIGHT = 20

nextCells = [] # Create a list for the new cells
for x in range(WIDTH):
    column = [] # Create a new column
    for y in range(HEIGHT):
        if random.randint(0,1)==0:
            column.append('#') # Add a living cell
        else:
            column.append('') # Add a dead cell
    nextCells.append(column) # nextCells is a list of column lists

while True: #Main program loop
    print('\n\n\n\n\n') # Seperate each step with new lines
    currentCells = copy.deepcopy(nextCells)

    # Print current cells onscreen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y],end='') # Print the # or space
        print() # Print a new line at the end of the row

    # Calculate next steps cells based on current steps
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # get current coordinates
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 2) % HEIGHT

            # Count living neighbors
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors =+ 1 #top-left neighbor is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1
            
            # Set cell based on Conway Game of Life Rules
            if currentCells[x][y]=='#' and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors alive
                nextCells[x][y]='#'
            elif currentCells[x][y]=='' and numNeighbors ==3:
                # Dead cells come alive w 3 living neighbors
                nextCells[x][y]='#'
            else: # everything else dies or stays dead
                nextCells[x][y]=''

            time.sleep(1) # 1 second pause to reduce flickering
