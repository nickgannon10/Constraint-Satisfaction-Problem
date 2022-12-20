initial_board = [
    [6,0,8,7,0,2,1,0,0],
    [4,0,0,0,1,0,0,0,2],
    [0,2,5,4,0,0,0,0,0], 
    [7,0,1,0,8,0,4,0,5],
    [0,8,0,0,0,0,0,7,0],
    [5,0,9,0,6,0,3,0,1], 
    [0,0,0,0,0,6,7,5,0], 
    [2,0,0,0,9,0,0,0,8], 
    [0,0,6,8,0,5,2,0,3]
]

#initializes environment and aesthetics 
def board(initial_board): 
    for i in range(len(initial_board)): 
        #place horizontal line every 3 lines 
        if i % 3 == 0 : 
            print("----------------------------") 
        #place a vertical line every three line
        for j in range(len(initial_board[0])):
            if j % 3 == 0 : 
                print ("|", end = " ")
            if j == 8: 
                print(initial_board[i][j])
            else: 
                print(str(initial_board[i][j]) + " ", end = " ")

#establish row and column coorinate system
def zeros(initial_board): 
    for i in range(len(initial_board)): 
        for j in range(len(initial_board[0])): 
            if initial_board[i][j] == 0: 
                return (i, j)
    return None

#determine if inserted number contradicts sodoku rules 
#each row, column, and 3x3 box can't have a repeated number
def legit(initial_board, number, position):
    #check row 
    for i in range(9): 
        if initial_board[position[0]][i] == number: 
            if position[1] != i: 
                return False  
    #check column
    for i in range(9): 
        if initial_board[i][position[1]] == number:
            if position[0] != i: 
                return False 
    #check 3x3 Box 
    #deal with whole numbers 
    row_beginning = position[0] - position[0] % 3
    col_beginning = position[1] - position[1] % 3
    for row in range(3):
        for col in range(3):
            if row != position[0] and col != position[1]:
                if initial_board[row_beginning + row][col_beginning + col] == number:
                    return False
    return True

def domain_vals():
    return [1,2,3,4,5,6,7,8,9]

def backtrack(initial_board):
    #test for completion, check is represented by coordinates 
    check = zeros(initial_board)
    #return true if no zeroes
    if not check:
        return True
    #discern coordinates of the zero
    else: 
        x, y = check 
    #loop through values 1-9
    for i in domain_vals():
        if legit(initial_board, i, (x, y)): 
            #if valid add num into the board
            initial_board[x][y] = i
            #recursivley call solve on updated board
            if backtrack(initial_board):
                return True 
            #THIS IS THE BACKTRACKING
            #recursion has returned failure
            #so current value may not be the problem  
            #reset the value back to empty 
            initial_board[x][y] = 0
    #if False, then every possible variable breaks the constaints 
    #if backtack alg returns falls then board is not possible  
    return False

advanced_board = [
    [0,7,0,0,4,2,0,0,0],
    [0,0,0,0,0,8,6,1,0],
    [3,9,0,0,0,0,0,0,7], 
    [0,0,0,0,0,4,0,0,9],
    [0,0,3,0,0,0,7,0,0],
    [5,0,0,1,0,0,0,0,0],
    [8,0,0,0,0,0,0,7,6],
    [0,5,4,8,0,0,0,0,0],
    [0,0,0,6,1,0,0,5,0]
]


print("Initial Board - Easy Board")
board(initial_board)
backtrack(initial_board)
print("Completed Board - Easy Board")
print(backtrack(initial_board)) #returns false when board is impossible 
board(initial_board)

print("Initial Board - Advanced Board")
board(advanced_board)
backtrack(advanced_board)
print("Completed Board - Advanced Board")
print(backtrack(advanced_board)) #returns false when board is impossible 
board(advanced_board)

