from z3 import *
from scrapper import scrape_sudoku_entries

sudoko_grid = scrape_sudoku_entries('https://www.websudoku.com/')
print(sudoko_grid)

s = Solver()

grid = [
    [Int(f'entry{n}{m}') for m in range(9)]
    for n in range(9)
]


# we should have the grid s.t each row and column will have a proposition that is true exactly 9 times, this is checked below

for n in range(9):
    for m in range(9):
        s.add(grid[n][m]>=1)
        s.add(grid[n][m]<=9) 
        # adds the conjucntion that all entries must be 1 to 9
    s.add(Distinct(grid[n]))
    #checks if all the numbers are unique in each row (proposiiton that all numbers are different)
    
for m in range(9):
    s.add(Distinct([grid[n][m] for n in range(9)]))
    # does the same iterates over the column list
    
# now we need to make sure that the 3 by 3 grids are populated by 1 to 9:

for n in range(3):
    for m in range(3):
        s.add(Distinct([grid[3*n+i][3*m+j] for i in range(0,3) for j in range(0,3)]))
        
for i in range(9):
    for j in range(9):
        n = sudoko_grid[i][j]
        if n != '':
            s.add(grid[i][j]==int(n))
            

s.check()
m=s.model()
print(m)

# above solves the problem, now we need an implementation that take a game from a file/website and solves from it
