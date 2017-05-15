# CSC 392 Assignment 2: Conway's Game of Life
# 
# Group: Jie He, Noah Davis, Marwan

import os     # Used for system calls
import time   # Used for system calls
import pandas # Used for dataframes and information processing
import numpy   # Used for generating random arrays

# From Dr. Hamel's CSC 392 website, slightly modified
def display_df(df):
    "clear the screen, display the contents of a dataframe, wait for 1sec"
    os.system('clear')
    rows = df.shape[0]
    cols = df.shape[1]
    for i in range(rows):
        for j in range(cols):
            # Modified to print live cells as black squares and dead cells as space
            if (df.iloc[i,j])==1:
                print(u"\u25A0",end=' ')
            else:
                print(" ",end=' ')
        print()
    time.sleep(1)

""" The update function is used to iterate a given dataframe once, such that each 
    cell in the frame follows the rules of Conway's Game of Life given a previous 
    state
"""
def update(Z):
    # We consider a neighbor for each extreme upper, lower, left, and right bound
    # to be the cell at its opposite extreme. That is, the leftmost center cell's 
    # neighbor is the rightmost center cell and vice versa.
    for i in range (size):
        #Check upper bundary
        if  i==0:
            upper=size-1
        else:
            upper=i-1
        #Check lower bundary
        if i==size-1:
            lower=0
        else:
            lower=i+1
        for j in range (size):
            #Check left bundary
            if  j==0:
                left=size-1
            else:
                left=j-1
            #Check right bundary
            if j==size-1:
                right=0
            else:
                right=j+1
            # Count neighbors so that the game rules can be applied
            N=(Z.iloc[upper,left]+Z.iloc[upper,j]+Z.iloc[upper,right]+
               Z.iloc[i,left]+Z.iloc[i,right]+
               Z.iloc[lower,left]+Z.iloc[lower,j]+Z.iloc[lower,right])
            
            #Apply rules to each cell for a given number of neighbors
            birth=(N==3) & (Z.iloc[i,j]==0)
            survive=((N==2)|(N==3))  &  (Z.iloc[i,j]==1)
            if birth | survive:
               Z.iloc[i,j]=1
            else:
               Z.iloc[i,j]=0

    # Return the new matrix
    return Z

""" The main program calls the user to input a size and iteration number then
    updates and displays the dataframe for each iteration.

    Warning: Large dataframe sizes may be very slow :(
"""

# Code input statically if you don't want console output
# Get user input for size
a=input("please input the board size: ")
size=int(a)
# Generate random list of 1's and 0's in the given size
Z=numpy.random.randint(2, size=(size, size))

# TESTING
# if used for testing then size must be 6
# Z=numpy.array([[0,0,0,0,0,0],
#               [0,0,0,1,0,0],
#               [0,1,0,1,0,0],
#               [0,0,1,1,0,0],
#               [0,1,0,0,1,0],
#               [0,0,0,0,0,0]])

# Again, code input statically if you don't want console output
# get user input for number of generations
b=input("please input the number of generations: ")
g=int(b)
# Iterate for number of desired iterations, display dataframe contents
# per iteration
for i in range(g):
    Z=pandas.DataFrame(Z)
    df = update(Z)
    display_df(df)

# end of file
