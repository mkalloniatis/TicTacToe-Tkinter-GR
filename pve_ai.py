import tkinter as tk
import tictactoe_menu
from tkinter import messagebox
import algorithm


playerO = []
playerX = []
buttons = {}
color_w = []
turn = 0
val = 0



class Buttons():
    def __init__(self, col, row, num):
        self.col = col
        self.row = row
        self.num = num
        self.button = tk.Button(Board.frame, text = "", bg = "#FECEAB", command= self.button_action, relief="ridge")
        self.button.grid(row =self.row, column = self.col, padx=3 , pady= 3, sticky="nsew")     

    def button_action(self):
        global val
        self.button.config(state="disabled")
        if turn % 2 == 0:
            self.button.config(text="O", font=('Courier New', 70, 'bold'))
            playerO.append(self.num)
        else:
            self.button.config(text="X", font=('Courier New', 70, 'bold'))
            playerX.append(self.num)
        move.check_win(playerO, playerX)
        if move.win == True:
            move.have_win()
        else:
            board.set_round()
            board.update_window()
            if turn % 2 == 0:
                if val == "no":
                    move.ai_turn()
            else: 
                if val == "yes":
                    move.ai_turn()


class Move():
    def __init__(self):
        self.win_combos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        self.win = False
        self.result =""
        self.ai_choice = 0
    
    def check_win(self, O, X):
        global color_w, turn
        if turn < 10:
            for comb in self.win_combos:
                if self.win !=True: color_w = []
                for num in comb:
                    if turn % 2 == 0 and self.win == False:
                        if num in O:
                            color_w.append(num)
                            if len(color_w) == 3:
                                self.win = True
                                self.result = "'O'"
                                break
                        else: break
                    elif self.win == False:
                        if num in X:
                            color_w.append(num)
                            if len(color_w) == 3: 
                                self.win = True
                                self.result = "'X'"
                        else: break
        else: self.result = "-"
        return self.result
        
    def have_win(self):
        for i in color_w :
                buttons[i].button.config(bg = "#99B898")
        for i in range(1,10):
            buttons[i].button.config(state = "disabled")
        board.update_window()

    def ai_turn(self):
        global playerO, playerX, val, turn
        if self.win ==False:
            self.ai_choice = algorithm.best_move(playerO,playerX, val, turn)
            buttons[self.ai_choice].button_action()
        

class Board():
    buttons = {}
    turn = 0
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("           Tic Tac Toe ")
        self.window.configure(bg = "#2A363B")
        self.playertext = ""
        self.set_round()
        self.label = tk.Label(self.window, text = self.playertext,font=('Courier New', 30, 'bold'), bg = "#2A363B", fg = "#FECEAB")
        self.optionsframe = tk.Frame(self.window, bg = "#2A363B")
        self.restart_button = tk.Button(self.optionsframe, text = "Παίξε ξανά",height = 3, width = 15,font=('Courier New', 15, 'bold'), bg = "#FFFFC1", command=self.restart) 
        self.menu_button = tk.Button(self.optionsframe, text = "Menu",height = 3, width = 15,font=('Courier New', 15, 'bold'), bg = "#FFFFC1", command=self.menu) 
        Board.frame = tk.Frame(self.window, bg = "#000000")  
        self.create_window()  


    def create_window(self):
        self.label.pack()
        Board.frame.pack(expand=True,padx=100, pady=20)
        self.optionsframe.pack(expand=True)
        self.restart_button.pack(padx = 10, pady = 10, side="left")
        self.menu_button.pack(padx = 10, pady = 10, side="left")
        for row in range(3):
            Board.frame.rowconfigure(row, weight=1, minsize= 200)
            Board.frame.columnconfigure(row, weight=1, minsize= 200)
            for col in range(3):
                butt_num = 2*row +row + col + 1
                buttons[butt_num] = Buttons(col, row, butt_num)

    def update_window(self):
        if move.win == False:
            if turn < 10:
                self.label.config(text = self.playertext )
            else:
                self.label.config(text="Ισοπαλία!")
                move.win = True
                for i in range(1,10):
                    buttons[i].button.config(state = "disabled", bg ="#E84A5F")

        elif move.win == True:
            self.label.config(text="Νίκησε ο {} !!!".format(move.result))

    def set_round(self):
        global turn
        if turn % 2 == 0:
            self.playertext = "Η σειρά του 'X'"
            turn +=1
        else: 
            self.playertext = "Η σειρά του 'O'"
            turn +=1

    def set_algo(self):
        global val
        val = messagebox.askquestion("Πληροφορίες", "Θες να ξεκινήσω εγώ;")
        if val == "yes":
            move.ai_turn()


    def main(self):
        self.window.mainloop()

    def restart(self):
        self.window.destroy()
        main()

    def menu(self):
        self.window.destroy()
        tictactoe_menu.main()
    

#---------------------------------------------------------------------------

def main():
    global board, move,playerO,playerX,buttons,color_w, turn
    playerO = []
    playerX = []
    buttons = {}
    color_w = []
    turn = 0
    board = Board()
    board.create_window()
    move = Move()
    board.set_algo()
    board.main()



if __name__ == "__main__":
    global board, move
    board = Board()
    move = Move()
    board.set_algo()
    board.main()
