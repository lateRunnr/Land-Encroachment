#PROBLEM: given a 2D array, return the size (in units) of the largest
#contiguous 0-bounded shape.


# should return 4
grid1 = [[1, 1, 1, 1, 1],
         [1, 1, 0, 0, 1],
         [1, 1, 1, 0, 1],
         [1, 0, 0, 1, 1],
         [1, 0, 0, 1, 1]]

# should return 0
grid2 = [[1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1]]

# should return 1
grid3 = [[1, 1, 1, 1, 1],
         [1, 0, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1]]

# should return 3
grid4 = [[1, 1, 1, 1, 1],
         [0, 1, 0, 0, 1],
         [0, 1, 1, 1, 1],
         [0, 1, 1, 1, 1],
         [1, 1, 1, 1, 1]]

# should return 3
grid5 = [[1, 1, 1, 1, 1],
         [0, 1, 0, 0, 1],
         [0, 1, 0, 1, 1],
         [0, 1, 1, 1, 1],
         [1, 1, 0, 0, 0]]

grids = [grid1, grid2, grid3, grid4, grid5]

def checkMaxFlow(grid,row,column,visited):

    count=1
    count_right=0
    count_left=0
    count_up=0
    count_down=0

    ## Zero to the right
    if column+1 < len(grid[row]):          ## Handling index out of bound exception
        if grid[row][column+1]==0:
           if (row,column+1) not in visited:
               row_column=(row,column+1)
               visited.add(row_column)     ## Adding visited row_column major to the visited set
               count_right=checkMaxFlow(grid,row,column+1,visited)

       
    ## Zero to the left
    if column-1 >= 0:                    ## Handling index out of bound exception
        if grid[row][column-1]==0:
            if (row,column-1) not in visited:
               row_column=(row,column-1)
               visited.add(row_column)    ## Adding visited row_column major to the visited set
               count_left=checkMaxFlow(grid,row,column-1,visited)
    
    ## Zero Up
    if row-1 >= 0:                      ## Handling index out of bound exception
        if grid[row-1][column]==0:
            if (row-1,column) not in visited:
               row_column=(row-1,column)
               visited.add(row_column)    ## Adding visited row_column major to the visited set
               count_up=checkMaxFlow(grid,row-1,column,visited)
            
    ##Zero Down
    if row+1 < len(grid):                 ## Handling index out of bound exception
        if grid[row+1][column]==0:
            if(row+1,column) not in visited:
              row_column=(row+1,column)
              visited.add(row_column)    ## Adding visited row_column major to the visited set
              count_down=checkMaxFlow(grid,row+1,column,visited)
    
    ## Adding all zero elements from right, left , up and down 
    return (count_right+count_left+count_up+count_down+1)
    
    

def largest_bounded_shape(grid):
    # WRITE CODE HERE
    
    ## Base Condition - Starting Zero
    maxCount=0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == 0:
               visited=set()
               row_column=(row,column)
               visited.add(row_column)   ## Adding visited row_column major to the visited set
               count=checkMaxFlow(grid,row,column,visited)
               if count > maxCount:      ## Checking Max flow/Count
                  maxCount=count
        
    return maxCount

for index, grid in enumerate(grids):
    print 'Largest 0-bounded shape for grid ' + str(index) + ' = ' + str(largest_bounded_shape(grid))