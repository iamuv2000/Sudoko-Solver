sudoko_board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


#Solving the board
def solve(board):
    
    found_element = find_empty(board) 
    if not found_element:
        return True
    else: 
        row, column = found_element

    for i in range(1,10):
        if valid(board,i,(row,column)):
            board[row][column] = i

            if solve(board):
                return True
            board[row][column] = 0
    return False
        

# To check whether insertion is valid
def valid(board,num,pos):
    
    #Checking the row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    
    #Checking the column
    for i in range(len(board[0])):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
        
    #Checking the square
    box_x = pos[1] // 3
    box_y = pos[0] // 3



    for i in range(box_y*3 , box_y*3 + 3):
        for j in range(box_x * 3 , box_x * 3 + 3):
            if board[i][j] == num and pos != (i,j):
                return False
    return True


# Print board
def print_board(board):
    for i in range(len(board)):
        if i%3==0 and i!=0:
            print('---------------------------')
        for j in range(len(board[i])):
            if j%3==0 and j!=0:
                print('|' , end = " ")
            print(board[i][j],  end = " ")
            if j == 8 :
                print('|')

# Find an empty element in the board
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i,j)
    return False


# Print unsolved board
print("Unsolved board --->")
print_board(sudoko_board)

#Solve board
solve(sudoko_board)

print('***************************')

#Print solved board
print("Solved board --->")
print_board(sudoko_board)
