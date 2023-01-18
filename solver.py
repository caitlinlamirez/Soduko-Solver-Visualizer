# Written by Caitlin Lamirez
# 12/19/2022

import curses 
from curses import wrapper 
import time
import boards
import random

board = random.choice(boards.boards_list)


def solve(bo, stdscr):
    # Find empty space
    find = find_empty(bo)

    # if we solved the board
    if not find: 
        return True 
    # otherwise, get row and col of empty space
    else:
        row, col = find 


    # loop through values 1-9
    for guess in range (1,10):

        #  If the guess is valid, we add them
        if valid(bo, guess, (row, col)):
            # Add current guess to the board and assume it is in correct position
            bo[row][col] = guess

            # Print out new board
            stdscr.refresh()
            stdscr.clear()
            print_board(bo, stdscr)
            time.sleep(0.01)
            stdscr.refresh()


            # Recursively call on new board to check for next guess with the next column
            if solve(bo, stdscr): 
                return True 

        # otherwise, our guess was wrong so we must reset it to 0
        bo[row][col] = 0 

    return False



def valid(bo, guess, pos):
    # Check row
    for i in range(len(bo[0])):
        # Check each element in the row to see if its the same number we just added in
        if bo[pos[0]][i] == guess and pos[1] != i:
              return False

    # Check column 
    for i in range (len(bo)):
        if bo[i][pos[1]] == guess and pos[0] != i:
            return False

    # Check the starting x & y values for the smaller boxes on the board
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y*3 +3):
        for j in range(box_x * 3, box_x*3 +3):
            # check to see if it is the same number we just added in
            if bo[i][j] == guess and (i, j) != pos:
                return False

    return True


def print_board(bo, stdscr):
    # Title
    stdscr.addstr("         SODUKO SOLVER\n", curses.A_BOLD)
    stdscr.addstr("-------------------------------\n", curses.A_BOLD)

    # Colors 
    BLUE = curses.color_pair(1)

    # For each row
    for r in range(len(bo)):
        # Add vertical separator
        stdscr.addstr("|")

        # For each element
        for c in range(len(bo[0])):
            # val --> the current value
            val = (bo[r][c]) 

            if val == 0:
                stdscr.addstr(" " + str(val) + " ")
            else:
                stdscr.addstr(" " + str(val) + " ", BLUE | curses.A_BOLD)

            # Add vertical separator
            if c == 2 or c == 5:
                stdscr.addstr("|")
        # Add vertical separator
        stdscr.addstr("|\n", )

        # Add horizontal separator
        if r == 2 or r == 5:
            stdscr.addstr("-------------------------------\n")
    # Add horizontal separator
    stdscr.addstr("-------------------------------\n")




def find_empty(bo):

    # for each row
    for r in range(len(bo)):
        # for each column
        for c in range(len(bo[0])):
            if bo[r][c] == 0:
                return (r,c)
    
    # if no more cells are empty
    return None 


def main(stdscr):
    # Colors
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # Store green color pair
    GREEN = curses.color_pair(2)

    # Print original
    stdscr.clear()
    print_board(board, stdscr)

    # Solve puzzle
    solve(board, stdscr)

    # Display success message
    stdscr.addstr("--> PUZZLE SOLVED!", GREEN)


    stdscr.getch()

# WRAPPER
wrapper(main)
   