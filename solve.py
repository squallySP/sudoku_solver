# -*- coding: utf-8 -*-

import time
import re

class sudoku:
    def __init__(self):
        self.grid = [
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]
            ]
        self.step_num = 0
        self.time_sec = 0
        
    def get_input_file(self, file):
        with open(file, 'rb') as f:
            i = 0
            for line in f.readlines():
                if line[0] != '|':
                    continue
                j = 0
                for char in line:
                    if re.match('\d', char):
                        self.grid[i][j] = int(char)
                        j += 1
                    if j >= 9:
                        break
                i += 1
                if i >= 9:
                    break
            
    def process(self):
        def check_line(grid, i, j):
            for index in range(9):
                if index == j:
                    continue
                if grid[i][index] == grid[i][j]:
                    return False
            return True
            
        def check_column(grid, i, j):
            for index in range(9):
                if index == i:
                    continue
                if grid[index][j] == grid[i][j]:
                    return False
            return True

        def check_cube(grid, i, j):
            m = i / 3
            n = j / 3
            for x in range(m*3, m*3+3):
                for y in range(n*3, n*3+3):
                    if x == i and y == j:
                        continue
                    if grid[x][y] == grid[i][j]:
                        return False
            return True

        def clone_grid(grid):
            new_grid = []
            for line in grid:
                new_grid.append(line[:])
            return new_grid
            
        def guess(grid, i, j):
            self.step_num += 1
            if i >=8 and j >= 9:
                return grid  # DONE
            if j >= 9:
                i = i + 1
                j = j % 9
            if grid[i][j] != 0:
                return guess(grid, i, j + 1)
            for x in range(1, 10):
                new_grid = clone_grid(grid)
                new_grid[i][j] = x
                if check_line(new_grid, i, j) and check_column(new_grid, i, j) and check_cube(new_grid, i, j):
                    new_new_grid = guess(new_grid, i, j + 1)
                    if new_new_grid:
                        return new_new_grid
                    else:
                        continue
            return None
                
        time_start = time.time()
        self.grid = guess(self.grid, 0, 0)
        self.time_sec = time.time() - time_start
        
    def output(self):
        if not self.grid:
            print "Error with input, please check your question file."
        for i in range(9):
            if i % 3 == 0:
                print "+-------+-------+-------+"
            for j in range(9):
                if j % 3 == 0:
                    print "|",
                print "%d" % self.grid[i][j] ,
            print "|"
            
        print "+-------+-------+-------+"
        
    def show_solve_info(self):
        print "Guess  Count:", self.step_num
        print "Second Count:", self.time_sec

    
if __name__ == "__main__":
    test = sudoku()
    test.get_input_file("question.txt")
    print "The question:"
    test.output()
    test.process()
    print "\nThe answer:"
    test.output()
    test.show_solve_info()