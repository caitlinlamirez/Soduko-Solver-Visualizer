# Sudoku Solver with Backtracking Algorithm
This project is a Python implementation of the backtracking algorithm to solve Sudoku puzzles using the curses module. The backtracking algorithm is a common technique that works by incrementally building a solution one step at a time, and "backtracking" when a dead end is reached.

## How to Use 
To run the Sudoku solver, you will need to have Python installed on your machine. Then, you can clone this repository, navigate to the project directory, and run the solver.py file. To add additional boards, you can navigate to the boards.py file and create additional boards. 

## How it Works

The backtracking algorithm used in this project is a recursive function that starts with a randomly generated board from the boards.py file and tries to fill in each empty cell with a number from 1 to 9 that satisfies the Sudoku constraints. If a number cannot be placed in a cell, the algorithm backtracks to the previous cell and tries a different number until a solution is found.

The curses module is used to display the current state of the board and the backtracking algorithm as it progresses. The interface is updated in real-time as the algorithm tries different values for each cell, providing a visual representation of how the backtracking algorithm works.
