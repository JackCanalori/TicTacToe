import tkinter as tk
import Bot

game_board = [["","",""],
              ["","",""],
              ["","",""]]




def display_rules():
    print("Rules: \n"
          "X plays first\n"
          "First to connect 3 in a row horizontally, vertically or diagonal wins\n"
          "If the board is filled without a win the game is a draw")



def start_game():
    start_button.pack_forget()
    rules.pack_forget()
    title = tk.Label(root, text="Welcome to Tic Tac Toe")
    title.pack(pady = 20)
    choice = tk.Label(root, text="Pick your Letter")
    choice.pack()

    # Create centered frame
    button_frame = tk.Frame(root)
    button_frame.place(relx=0.5, rely=0.5, anchor="center")

    # 3 stacked buttons
    button1 = tk.Button(button_frame, text="X", width=15, height = 5)
    button1.pack(pady=5)

    button2 = tk.Button(button_frame, text="Y", width=15, height = 5)
    button2.pack(pady=5)

    button3 = tk.Button(button_frame, text="Random", width=15, height = 5)
    button3.pack(pady=5)


# Create the main window
root = tk.Tk()
root.title("Button Replacement Demo")
root.geometry("900x600")

# Create the start button
start_button = tk.Button(root, text="Start Game", command=start_game, width= 15)
start_button.pack(pady=10, anchor="center")
rules = tk.Button(root, text="See Rules", command=display_rules(), width= 15)
rules.pack(pady=10, anchor="center")

root.mainloop()