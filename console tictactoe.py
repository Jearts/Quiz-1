board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6: print("-----------")

def check_win(p):
    win_cond = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == p for a, b, c in win_cond)

turn = "X"
for _ in range(9):
    print_board()
    try:
        move = int(input(f"yooo player one {turn}, will enter their attack >:D choose 1-9/type ")) - 1
        if board[move] == " ":
            board[move] = turn
            if check_win(turn):
                print_board()
                print(f"Player {turn} won the game! niceeee")
                break
            turn = "O" if turn == "X" else "X"
        else:
            print("yooo this spot is taken, try again.")
    except (ValueError, IndexError):
        print("read the instructions clearly, alright? try again.")
else:
    print_board()
    print("yoo, its a draw? try another round hehe.")
