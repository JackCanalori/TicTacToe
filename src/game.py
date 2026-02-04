import tkinter as tk


import Bot

game_board = [["","",""],
              ["","",""],
              ["","",""]]



def handle_click(event):
    row = event.y // CELL
    col = event.x // CELL
    print(row, ", ",col)


def player_X():
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    title.pack_forget()
    choice.pack_forget()
    canvas.pack(anchor="center", pady = 100)
    # Vertical lines
    canvas.create_line(CELL, 0, CELL, SIZE, width=2, fill="red")
    canvas.create_line(2 * CELL, 0, 2 * CELL, SIZE, width=2, fill="red")

    # Horizontal lines
    canvas.create_line(0, CELL, SIZE, CELL, width=2)
    canvas.create_line(0, 2 * CELL, SIZE, 2 * CELL, width=2)






def display_rules():
    print("Rules: \n"
          "X plays first\n"
          "First to connect 3 in a row horizontally, vertically or diagonal wins\n"
          "If the board is filled without a win the game is a draw")



def start_game():
    start_button.pack_forget()
    rules.pack_forget()
    title.pack(pady = 20)
    choice.pack()
    button1.pack(pady = 5)
    button2.pack(pady = 5)
    button3.pack(pady = 5)




# Create the main window
root = tk.Tk()
root.title("Button Replacement Demo")
root.geometry("900x600")
start_button = tk.Button(root, text="Start Game", command=start_game, width= 15)
start_button.pack(pady=10, anchor="center")
rules = tk.Button(root, text="See Rules", command=display_rules, width= 15)
rules.pack(pady=10, anchor="center")
button_frame = tk.Frame(root)
button_frame.place(relx=0.5, rely=0.5, anchor="center")
button1 = tk.Button(button_frame, command = player_X, text="X", width=15, height = 5)
button1.pack_forget()
button2 = tk.Button(button_frame, text="Y", width=15, height = 5)
button2.pack_forget()
button3 = tk.Button(button_frame, text="Random", width=15, height = 5)
button3.pack_forget()
choice = tk.Label(root, text="Pick your Letter")
choice.pack_forget()
title = tk.Label(root, text="Welcome to Tic Tac Toe")
title.pack_forget()
canvas = tk.Canvas(root, width=300, height=300)
canvas.bind("<Button-1>", handle_click)
SIZE = 300
CELL = SIZE // 3
root.mainloop()