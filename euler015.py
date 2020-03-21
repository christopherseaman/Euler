#!/usr/bin/env python3

# Problem 15
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# The smart way to do this is to recognize that each path from the top left to the bottom right takes 40 steps with 20 down and 20 to the right
# That means there are 40 spaces to fit 20 downward steps in, or 40c20 combinations = 40! / (20! * (40-20)!)
# import gmpy2 as g
# print(g.comb(40, 20))
# > 137846528820

# Let do an inefficient solution using recursion as well
def walk(grid):
    if(grid[0] == 0 or grid[1] == 0):
        # reach an edge, only one way to go
        return 1
    else:
        right = grid.copy()
        right[0] -= 1
        down = grid.copy()
        down[1] -= 1
        return walk(down) + walk(right)

len = 20
square = [len, len]
print(walk(square))



# A smarter way by combining numbers of paths from each child node
# l=[]
# for i in range(21):
#        l.append([])
#        for j in range(21):
#               l[i].append(0)
              
# for i in range(21):
#        l[20][i]=1
#        l[i][20]=1
       
# for i in range(19,-1,-1):
#        for j in range(19,-1,-1):
#               l[i][j]=l[i+1][j]+l[i][j+1]
              
# print l[0][0]