from tkinter import *
from tkinter import messagebox


board = [[" " for _ in range(3)] for _ in range(3)]  # 3x3 game board
FirstPlayer = "X"
player1_name = ""
player1_symbol = ""
player2_name = ""
player2_symbol = ""


def submit():
    global player1_name, player1_symbol, player2_name, player2_symbol

    player1_name = entry.get()
    player1_symbol = entry1.get().upper()
    player2_name = entry2.get()
    player2_symbol = entry3.get().upper()


    if len(player1_symbol) != 1 or not player1_symbol.isalpha():
        messagebox.showerror("Error", "Player 1 symbol must be a single letter.")
        return
    if len(player2_symbol) != 1 or not player2_symbol.isalpha():
        messagebox.showerror("Error", "Player 2 symbol must be a single letter.")
        return
    if player1_symbol == player2_symbol:
        messagebox.showerror("Error", "Players must have unique symbols.")
        return
    if player1_symbol.upper() not in ["X", "O"]:
        messagebox.showerror("Error", "Symbol must be X or O")
        return
    if player2_symbol.upper() not in ["X", "O"]:
        messagebox.showerror("Error", "Symbol must be X or O")
        return

    form_frame.pack_forget()
    game_frame.pack()
    update_turn_label()


def next_turn(row, col):
    global FirstPlayer


    if board[row][col] == " ":
        board[row][col] = FirstPlayer  # Update the board
        game_btns[row][col].config(text=FirstPlayer, fg="blue" if FirstPlayer == player1_symbol else "red")  # Update the button text


        if check_winner(FirstPlayer):
            winner_name = player1_name if FirstPlayer == player1_symbol else player2_name
            messagebox.showinfo("Game Over", f"🎉 {winner_name} wins! 🎉")
            reset_game()

        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:

            FirstPlayer = player2_symbol if FirstPlayer == player1_symbol else player1_symbol
            update_turn_label()


def check_winner(symbol):

    for row in board:
        if all(cell == symbol for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True

    if all(board[i][i] == symbol for i in range(3)):  # Top-left to bottom-right
        return True
    if all(board[i][2 - i] == symbol for i in range(3)):  # Top-right to bottom-left
        return True
    return False


def is_draw():
    return all(cell != " " for row in board for cell in row)


def reset_game():
    global board, current_player
    board = [[" " for _ in range(3)] for _ in range(3)]  # Reset the board
    current_player = player1_symbol  # Reset to starting player
    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text=" ", fg="black")  # Clear all buttons
            update_turn_label()
def update_turn_label():
    current_player_name = player1_name if FirstPlayer == player1_symbol else player2_name
    turn_label.config(text=f"{current_player_name}'s turn ({FirstPlayer})")


window = Tk()
window.title("X-O Game")
window.geometry("500x500")
window.configure(bg="#c5edd9")


form_frame = Frame(window, bg="#c5edd9")
form_frame.pack(pady=50)

titleLabel = Label(form_frame, text="X/O Game", font=("Comic Sans MS", 27,), bg="#c5edd9")
titleLabel.grid(row=0, column=0, columnspan=2, pady=10)
# Labels and Entry widgets for Player 1
Label(form_frame, text="Player 1 Name:", font=("Georgia", 12), bg="#f0f0f0").grid(row=2, column=0, sticky="w", pady=5)
entry = Entry(form_frame, width=20, font=("Georgia", 12))
entry.grid(row=2, column=1, pady=5,sticky="w")

Label(form_frame, text="Player 1 Symbol:", font=("Georgia", 12), bg="#f0f0f0").grid(row=3, column=0, sticky="w", pady=5)
entry1 = Entry(form_frame, width=20, font=("Georgia", 12))
entry1.grid(row=3, column=1, pady=5)


Label(form_frame, text="Player 2 Name:", font=("Georgia", 12), bg="#f0f0f0").grid(row=4, column=0, sticky="w", pady=5)
entry2 = Entry(form_frame, width=20, font=("Georgia", 12))
entry2.grid(row=4, column=1, pady=5)

Label(form_frame, text="Player 2 Symbol:", font=("Georgia", 12), bg="#f0f0f0").grid(row=5, column=0, sticky="w", pady=5)
entry3 = Entry(form_frame, width=20, font=("Georgia", 12))
entry3.grid(row=5, column=1, pady=5)


submit_button = Button(form_frame, text="Start Game", font=("Arial", 14), bg="#4CAF50", fg="white", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=20)


game_frame = Frame(window, bg="#c5edd9")
resetButton=Button(game_frame,command=reset_game, text="Reset Game", font=("Arial", 14),bg="#4CAF50", fg="white")
resetButton.grid(row=5)


game_btns = [[0,0,0], [0,0,0], [0,0,0]]
for row in range(3):
    for col in range(3):
        game_btns[row][col] = Button(game_frame, text="", font=("Arial", 24), width=5, height=2,
                                     bg="#ffffff", fg="black", command=lambda row=row, col=col: next_turn(row, col))
        game_btns[row][col].grid(row=row, column=col, padx=5, pady=5)
turn_label = Label(game_frame, text="", font=("Verdana", 20), bg="#c5edd9")
turn_label.grid(row=3, column=0, columnspan=3, pady=10)

window.mainloop()