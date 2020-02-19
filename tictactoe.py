# Tic tac toe!
#define print board
def print_board(board):
    #define variables
    d=1
    f=0
    #setup board
    print("- 0 1 2")
    for r in board:
        for c in r:
            if d % 3 == 0:
                if c == 0:
                    print(".")
                elif c == 1:
                    print("X")
                else:
                    print("O")
            elif d % 3== 1:
               if c == 0:
                    print(f,".",end="|")
               elif c==1:
                    print(f,"X",end="|")
               else:
                    print(f,"O",end="|")
            else:
                 if c==0:
                     print(".",end="|")
                 elif c==1:
                     print("X",end="|")
                 else:
                     print("O",end="|")
            
            d +=1
        if d !=10:
            print("  -----")
        f +=1
                    
#define is valid
def is_valid(r, c, board):
    if (r<0 or r>2)or(c<0 or c>2):
        return False
    if board[r][c] == 0:
        return True
    return False

def is_winner(board):
    for i in range (0,3):
        #vertical and horizontal first
        if board[0][i] == board[1][i] == board[2][i] !=0:
            return True
        if board[i][0] == board[i][1] == board[i][2] !=0:
            return True
    #check for diagonal last
    if board[0][0] == board[1][1] == board[2][2] !=0:
            return True 
    if board[0][2] == board[1][1] == board[2][0] !=0:
            return True
    return False
#put em all togetha
def main():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    current = 1
    for i in range(9):
        print_board(board)
        if is_winner(board) == True:
            if current == 1:
                print("O has won")
            else:
                print("X has won")
            break
        if current == 1:
            print("X's turn")
        else:
            print("O's turn")

        r = int(input("Give Row:"))
        c = int(input("Give Column:"))
        while not is_valid(r, c, board):
            r = int(input("Give Row:"))
            c = int(input("Give Column:"))

        board[r][c] = current
        if current == 1:
            current = 2
        else:
            current = 1

#call main
main()
