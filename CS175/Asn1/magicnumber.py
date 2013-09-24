# magicnumber.py
# Reads a file containing a matrix of numbers, determines whether it
# is a magic square, and prints the numbers and the result.
#
# Copyright 2011, Mark Tupala.
# All rights reserved.
#
# Created: Mark Tupala (tupala@ualberta.ca)

import sys

class Matrix(object):
    def __init__(self, rows):
        self.rows = rows
        self.num_rows = len(rows)
        self.num_cols = len(rows[0])
        self.conv_to_ints()
        # The target is defined as the sum of the first row. If any
        # row, column, or diagonal doesn't match, it's not a magic square
        self.target = sum(self.rows[0])
    
    # Turns strings into ints
    def conv_to_ints(self):
        for row in range(self.num_rows):
            for col in range(len(self.rows[row])):
                self.rows[row][col] = int(self.rows[row][col])
    
    # Utilizes short circuit evaluation (i.e. as soon as one check fails 
    # the rest are not evaluated) to check if it is a perfect square
    def check_perfect_square(self):
        if self.is_square() and self.check_rows() and self.check_cols() and \
        self.check_diagonal1() and self.check_diagonal2():
            self.is_magic = True
        else: self.is_magic = False

    # Checks to see if the rows all have the same length and are equal to the
    # number of rows as well (i.e. whether it is actually a square)
    def is_square(self):
        if self.num_rows != self.num_cols: return False
        for row in self.rows:
            if len(row) != self.num_cols: return False
        return True

    def check_rows(self):
        for row in self.rows:
            if sum(row) != self.target:
                return False
        return True

    def check_cols(self):
        for col in range(self.num_cols):
            tally = 0
            for row in self.rows:
                tally += row[col]
            if tally != self.target:
                return False
        return True

    # Checks the diagonal from top-left to bottom-right
    def check_diagonal1(self):
        tally = sum([self.rows[ii][ii] for ii in range(self.num_rows)])
        if tally != self.target: return False
        else: return True

    # Checks the diagonal from top-right to bottom-left
    def check_diagonal2(self):
        col = self.num_cols - 1
        tally = 0
        for row in range(self.num_rows):
            tally += self.rows[row][col]
            col -= 1
        if tally != self.target: return False
        else: return True

if __name__ == "__main__":
    # Get the file name, open it, read it into a list of strings, then close
    file_name = sys.argv[1]
    infile = open(file_name, 'r')
    lines = infile.readlines()
    infile.close()
    
    # Create matrix with rows data, and check if it is a perfect square
    rows = [line.split() for line in lines]
    matrix = Matrix(rows)
    matrix.check_perfect_square()

    # Print output
    for line in lines:
        print(line, end='')

    if not matrix.is_magic:
        print('The input matrix is not a magic square.')
    else:
        print('The input matrix is a magic square ' +
            'and has a magic number of ' + str(matrix.target) + '.')

