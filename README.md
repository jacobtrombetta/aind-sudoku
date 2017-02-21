# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: Finding naked twins on the sudoku board allows the algorithm to impose extra constrains on the space.  The constraints imposed on the rows, columns, and units in the normal elimination and search algorithms only take boxes with singular entries into account.  Finding a naked twin allows us to make additional constraints on entries in their related peer group. 

If a row has two separate entries with the same two values, they are considered naked twins. This means the two values can only exist in the two entries.  For example, using 'A-I' to denote rows and '1-9' to denote columns, if boxes C1 and E1 both contain [2,6], if [2] eventually goes into C1, [6] must go into E1.  This is also true for the opposite case. With the naked twin constraint on entries C1 and E1, the values [2,6] can be eliminated from the rest of the entries in the top row: A1, B1, D1, F1, G1, H1, and I1.  This logic can be applied if the naked twins appear in a peer column or peer unit as well.
    

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: The diagonal sudoku case forces the player to adhere to the same '1-9' ordering rule used for columns, rows, and units, on the two main diagonals.  This rule adds six additional constraint possibilities for seventeen different entries.  So approximately 21% of the entiries have additional constrains for the elimination algorithm to propagate across the board.  This is very good news for the elimination algorithm because a singular entry in one of the diagonal boxes will impose its constraints further than in the non-diagonal sudoku case.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.
# aind-sudoku
