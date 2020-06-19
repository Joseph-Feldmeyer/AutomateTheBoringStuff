###################################################################
#File Name: 04_conway.py
#Author: Joseph Feldmeyer
#Email: joseph.k.feldmeyer@gmail.com
#Creation Date: 19-06-2020

#Description: Create a program that shows "Conway's Game of Life" 

###################################################################


import random, time, copy

# Global vars
WIDTH = 90 
HEIGHT = 55


# Create a list of list for the cells 
nextCells = []
for x in range(WIDTH): 
    column = []     # Create a new column 
    for y in range(HEIGHT): 
        if random.randint(0,1) == 0: 
            column.append('#')  # Add a living cell 
        else: 
            column.append(' ')  # Add a dead cell 
    nextCells.append(column)    # nextCells is a list of column lists 


# Main program loop 
while True: 
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n')     # Separate each step with new lines 
    currentCells = copy.deepcopy(nextCells) 

    # Print currentCells on the screen: 
    for y in range(HEIGHT): 
        for x in range(WIDTH): 
            print(currentCells[x][y], end='')   # Print the '#' or ' '
        print()     # Print a new line at the end of the row 
    
    # Calculate the next step's cells based on current step's cells: 
    for x in range(WIDTH): 
        for y in range(HEIGHT): 
            # Get neighboring coordinates: 
            # `% WIDTH` ensures left Coord is always between 0 and WIDTH-1
            leftCoord = (x-1) % WIDTH
            rightCoord = (x+1) % WIDTH
            aboveCoord = (y-1) % HEIGHT
            belowCoord = (y+1) % HEIGHT 

            # Count the number of living neighbors 
            numNeighbors = 0 
            
            if currentCells[leftCoord][aboveCoord] == '#': 
                numNeighbors += 1   # Top-left 
            if currentCells[x][aboveCoord] == '#': 
                numNeighbors += 1   # Top
            if currentCells[rightCoord][aboveCoord] == '#': 
                numNeighbors += 1   # Top-right 
            if currentCells[leftCoord][y] == '#': 
                numNeighbors += 1   # Left
            if currentCells[rightCoord][y] == '#': 
                numNeighbors += 1   # Right
            if currentCells[leftCoord][belowCoord] == '#': 
                numNeighbors += 1   # Bottom-left 
            if currentCells[x][belowCoord] == '#': 
                numNeighbors += 1   # Bottom 
            if currentCells[rightCoord][belowCoord] == '#': 
                numNeighbors += 1   # Bottom-right

            # Set cell based on Conway's Game of Life rules: 
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3): 
                # Living cells with 2 or 3 neighbors become alive: 
                nextCells[x][y] = '#' 
            elif currentCells[x][y] == ' ' and numNeighbors == 3: 
                # Dead cells with 3 neightbors become alive: 
                nextCells[x][y] = '#' 
            else: 
                # Everything else dies or stays dead: 
                nextCells[x][y] = ' ' 
        
    time.sleep(0.03)   # Add pause 

