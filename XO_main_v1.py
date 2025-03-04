# الفانكشن ديه بتعمل اللوحه الفاضيه عشان نلعب عليه
# كل خانه بتكون رقم من 1 ل 9 علشان اللعيبه يختارو بسهوله

def create_board():
    return [[str(i + j * 3 + 1) for i in range(3)] for j in range(3)]

# الفانكشن ديه بتطبع اللوحه بشكل منظم عشان نعرف نلعب

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("----------")
    print()

# ديه الفانكشن اللي بتاخد اسم اللعيب ورمزو
# وبتتاكد انه رمز مميز ومش متاخد من التاني

def get_player_info(player_num, taken_symbols):
    name = input(f"Player {player_num}, enter your name: ")
    while True:
        symbol = input(f"{name}, choose your symbol (any letter): ").upper()
        if len(symbol) == 1 and symbol.isalpha() and symbol not in taken_symbols:
            taken_symbols.add(symbol)
            return name, symbol
        print("Invalid symbol! Choose a uniqe letter.")

# الفانكشن ديه بتشوف اذا كان حد كسب ولا لا

def check_winner(board, symbol):
    win_patterns = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return any(all(cell == symbol for cell in pattern) for pattern in win_patterns)

# الفانكشن ديه بتشوف لو اللوحه اتملت ومفيش فايز

def is_draw(board):
    return all(cell.isalpha() for row in board for cell in row)

# الفانكشن ديه بتاخد الحركه من اللعيب وتتاكد انها صحيحه

def get_move(board, player_name, player_symbol):
    while True:
        try:
            move = input(f"{player_name}, enter your move (1-9) or 'q' to quit: ")
            if move.lower() == 'q':
                print("Game exited")
                exit()
            move = int(move) - 1
            row, col = divmod(move, 3)
            if board[row][col].isdigit():
                board[row][col] = player_symbol
                return
            print("This spot is already taken!")
        except (ValueError, IndexError):
            print("Invalid move! Choose a number between 1 and 9.")

# الفانكشن الاساسيه اللي بتدير الجيم كلها

def play_game():
    while True:
        board = create_board()
        print("Welcome to X-O Game!")
        taken_symbols = set()
        name1, symbol1 = get_player_info(1, taken_symbols)
        name2, symbol2 = get_player_info(2, taken_symbols)
        players = [(name1, symbol1), (name2, symbol2)]
        turn = 0
        while True:
            print_board(board)
            name, symbol = players[turn]
            get_move(board, name, symbol)
            if check_winner(board, symbol):
                print_board(board)
                print(f"🎉 {name} wins! 🎉")
                break
            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            turn = 1 - turn
        
        again = input("Do you want to play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

# تشغيل اللعبه
if __name__ == "__main__":
    play_game()
