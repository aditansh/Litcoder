import sys
rows = 9
cols = 9

def validSudoku(board):
    #row check
    for row in range(rows):
        numbers = set()
        for col in range(cols):
            if board[row][col] != '.' and board[row][col] in numbers:
                return False
            numbers.add(board[row][col])
    
    #col check
    for col in range(cols):
        numbers = set()
        for row in range(rows):
            if board[row][col] != '.' and board[row][col] in numbers:
                return False
            numbers.add(board[row][col])
    
    #box check
    for row in range(0, rows, 3):
        for col in range(0, cols, 3):
            numbers = set()
            for r in range(row, row+3):
                for c in range(col, col+3):
                    if board[r][c] != '.' and board[r][c] in numbers:
                        return False
                    numbers.add(board[r][c])
    
    return True

board = [["." for col in range(cols)] for row in range(rows)]
x = int(input())
inputVal = [input() for i in range(x)]
inputVal = ''.join(inputVal)

for index in range(81):
    board[index//9][index%9] = inputVal[index]

if(validSudoku(board)):
    print("YES")
else:
    print("NO")