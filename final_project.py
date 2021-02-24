
#imports 
import pygame
import numpy as np
import math
from time import perf_counter

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LBLUE = (52, 225, 235)
TEAL = (52, 235, 229)
DBLUE = (67, 52, 235)
LIME = (167, 245, 66)


#input needed information
size = int(input("Enter the size of the grid: "))
density = float(input("Enter the obstacle density: "))
# This sets the margin between each cell
MARGIN = 1



# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 0
HEIGHT = 0
if size == 100:
    HEIGHT = 5
    WIDTH = 5
    WINDOW_SIZE = [620, 620]
    if(density == .10):
        obst = 1000
    elif(density == .20):
        obst = 2000
    elif(density == .30):
        obst = 3000
    #break
elif size == 200:
    HEIGHT = 2
    WIDTH = 2
    WINDOW_SIZE = [630, 630]
    if(density == .10):
        obst = 4000
    elif(density == .20):
        obst = 8000
    elif(density == .30):
        obst = 12000
    #break
elif size == 300:
    HEIGHT = 1
    WIDTH = 1
    WINDOW_SIZE = [630, 630]
    if(density == .10):
        obst = 9000
    elif(density == .20):
        obst = 18000
    elif(density == .30):
        obst = 21000
elif size == 50:
    HEIGHT = 11
    WIDTH = 11
    WINDOW_SIZE = [650, 650]
    if(density == .10):
        obst = 750

#create random arrays
randnumsx = np.random.randint(0,size,obst)
randnumsy = np.random.randint(0,size,obst)

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(size):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(size):
        grid[row].append(0)  # Append a cell

#use while loop to insert 3 into grid location based on random array
j = 0
while(j < obst):
    x = randnumsx[j]
    y = randnumsy[j]
    grid[x][y] = 3
    j = j + 1

# Initialize pygame
pygame.init()


# Set the HEIGHT and WIDTH of the screen
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Final Project")

 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#arrays needed
op = []
closed = []
closed1 = []
closed2 = []
closed3 = []
neighbors = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

def neigh(nBest,GOAL,w):
    x = 0
    current = nBest
    while x < len(neighbors):
        for i,j in neighbors:
            neighbor = current[0] + i, current[1] + j
            if neighbor[0]==size or neighbor[1] == size:
                #print("out of grid")
                x = x + 1
            elif grid[neighbor[0]][neighbor[1]] == 3:
                #print("obstacle")
                x = x + 1
            elif grid[neighbor[0]][neighbor[1]] == 1:
                #print("Start")
                x = x + 1
            elif neighbor in closed:
                #print("node visited")
                x = x + 1
            else:
                #total = f(current,GOAL,neighbor)
                g = (gdistance(current,neighbor))
                h = (hdistance(neighbor,GOAL))*(w)
                total = (g + h)
                comb = (total,neighbor)
                op.append(comb)
                #print(neighbor)
                #print(grid[neighbor[0]][neighbor[1]])
                x = x + 1

def gdistance(current, neighbor):
    Node1 = current
    xCord1 = Node1[1]
    yCord1 = Node1[0]
    Node2 = neighbor
    xCord2 = Node2[1]
    yCord2 = Node2[0]
    distance = math.sqrt((xCord1 - xCord2)** 2 + (yCord1 - yCord2) ** 2)
    return distance

def mov():
    new = op[0]
    node = new[1]
    closed.append(node)
    op.clear()

def hdistance(neighbor, GOAL):
    Node1 = neighbor
    xCord1 = Node1[1]
    yCord1 = Node1[0]
    GOAL = GOAL
    xCordg = GOAL[1]
    yCordg = GOAL[0]
    distance = math.sqrt((xCord1 - xCordg)** 2 + (yCord1 - yCordg) ** 2)
    return distance

def take_first(elem):
    return elem[0]

def printary():
    a = 0
    while a < len(closed1):
        node = closed1[a]
        x = node[0]
        y = node[1]
        grid[x][y] = 4
        a = a + 1

def printary1():
    a = 0
    while a < len(closed3):
        node = closed3[a]
        x = node[0]
        y = node[1]
        grid[x][y] = 6
        a = a + 1

def printary2():
    b = 0
    while a < len(closed2):
        node = closed3[b]
        x = node[0]
        y = node[1]
        grid[x][y] = 5
        b = b + 1


def moveAr(w):

    if w == 200:
        #print("Array closed 1 filled")
        x = 0
        while x < len(closed):
            move = closed[x]
            closed1.append(move)
            x = x + 1
        #print("closed1")
        #print(closed1)
        closed.clear()
        astar(100)
    elif w == 100:
        #print("Array closed 2 filled")
        k = 0
        while k < len(closed):
            move = closed[k]
            closed2.append(move)
            k = k + 1
        #print("closed2")
        #print(closed2)
        closed.clear()
        astar(1)
    elif w == 1:
        #print("Array closed 3 filled")
        t = 0
        while t < len(closed):
            move = closed[t]
            closed3.append(move)
            t = t + 1
        #print("closed3")
        #print(closed3)
        printary()
        printary1()
        t1_stop = perf_counter()
        time = (t1_stop - t1_start) 
        c = round(time,4)
        print(c)
        

def astar(w):
    
    #print("WWWWWWWWWWW")
    #print(w)
    closed.append(START)
    nBest = closed[ len(closed) - 1]
    while nBest != GOAL:
        nBest = closed[ len(closed) - 1]
        neigh(nBest,GOAL,w)
        op.sort(key=take_first)
        #print(op)
        mov()
        if nBest == GOAL:
            #print("IT WORKS!!!!!!XXXXX#######$$$$$$$$")
            moveAr(w)



#-------------------------------------------------------------------
# left vs left click
LEFT = 1
RIGHT = 3
def switch_env(argument):
    switcher = {
        1: astar

    }
    # Get the function from switcher dictionary
    func = switcher.get(argument)
    # Execute the function
    func(200)


# -------- Main Program Loop -----------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            START = (row,column)

            #These prints are to make sure the mose click and the START variable are the same
            #print("Start Variable = mouse Click: ")
            #print(START)
            #print("Click ", pos, "Grid coordinates: ", row, column)
            
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 2
            GOAL = (row,column)
            #These prints are to make sure the mose click and the GOAL variable are the same
            #print("GOAL Variable = mouse Click: ")
            #print(GOAL)
            #print("Click ", pos, "Grid coordinates: ", row, column)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                t1_start = perf_counter()
                switch_env(1)





        # Set the screen background
    screen.fill(BLACK)

        # Draw the grid
    for row in range(size):
        for column in range(size):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            elif grid[row][column] == 3:
                color = DBLUE
            elif grid[row][column] == 2:
                color = RED
            elif grid[row][column] == 4:
                color = LBLUE
            elif grid[row][column] == 5:
                color = LIME
            elif grid[row][column] == 6:
                color = LIME
            pygame.draw.rect(screen,color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH,HEIGHT])
    

        # Limit to 60 frames per second
    clock.tick(60)


        # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()




#this print is meant to show the full grid to help debug any future problems with logic
#print(grid)



# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()