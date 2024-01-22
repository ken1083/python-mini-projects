import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")

        self.current_player = "X"
        self.board = [""] * 9

        for i in range(9):
            btn = tk.Button(self.window, text="", width=10, height=5,
                            command=lambda i=i: self.on_button_click(i))
            btn.grid(row=i // 3, column=i % 3)

        self.status_label = tk.Label(self.window, text="Player X's turn", font=("Helvetica", 12))
        self.status_label.grid(row=3, columnspan=3)

    def on_button_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.check_winner()
            self.update_button_text(index)
            self.switch_player()

    def update_button_text(self, index):
        button = self.window.grid_slaves(row=index // 3, column=index % 3)[0]
        button.config(text=self.current_player, state=tk.DISABLED)

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()

        if "" not in self.board:
            messagebox.showinfo("Game Over", "It's a tie!")
            self.reset_game()

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"

        for i in range(9):
            button = self.window.grid_slaves(row=i // 3, column=i % 3)[0]
            button.config(text="", state=tk.NORMAL)

        self.status_label.config(text="Player X's turn")

    def run(self):
        self.window.mainloop()

# 创建并运行游戏
game = TicTacToe()
game.run()
