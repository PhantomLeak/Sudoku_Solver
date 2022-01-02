
def solve(board):
    find = find_empty(board)
    if not find: #if it cannot find empty
        return True
    else:
        row, col = find #set the rows and columns to find_empty

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board): #if board is solved
                return True
            board[row][col] = 0
    return False
    
def valid(board, num, pos):
    #checks the rows 
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i: #if board position 0 equals position 1 and position 1 does not equal i
            return False
        
        #checks the columns
        for i in range(len(board)):
            if board[i][pos[1]] == num and pos[0] != i: #if board position i position 1 is equal to num and board position 0 doe not equal i
                return False
        
        #Checks boxes
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if board[i][j] == num and (i,j) != pos:
                    return False

        return True

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
    for j in range(len(board[0])):
        if j % 3 == 0 and i != 0:
            print(" | ", end="")

        if j == 8:
            print(board[i][j])
        else:
            print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return(i,j) # this is the row (i) and column(j)
    return None

