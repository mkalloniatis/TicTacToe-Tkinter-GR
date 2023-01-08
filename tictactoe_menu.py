import tkinter as tk
import pvp
import pve_random
import pve_ai


class Menu():
    def __init__(self):
        self.window = tk.Tk()
        self.welcome = tk.Label(text="Καλωσόρισες στην τρίλιζα!", font=('Courier New', 30, 'bold'), bg = "#69698B", fg = "#FFFFC1")
        self.button_pvp = tk.Button(text="Παίξε εναντίον ενός άλλου παίκτη",height = 4, width = 40, command=self.run_pvp, font=('Courier New', 15, 'bold'), bg = "#FFFFC1")
        self.button_pve = tk.Button(text="Παίξε εναντίον του υπολογιστή(εύκολο)",height = 4, width = 40, command=self.run_pve,font=('Courier New', 15, 'bold'), bg = "#FFFFC1")
        self.button_pve2 = tk.Button(text="Παίξε εναντίον του υπολογιστή(δύσκολο)",height = 4, width = 40, command=self.run_pve2,font=('Courier New', 15, 'bold'), bg = "#FFFFC1")
        self.create_menu()

    def run_pvp(self):
        self.window.destroy()
        pvp.main()
    
    def run_pve(self):
        self.window.destroy()
        pve_random.main()

    def run_pve2(self):
        self.window.destroy()
        pve_ai.main()

    def create_menu(self):
        self.window.title("Τρίλιζα")
        self.window.geometry("800x800")
        self.window.configure(bg = "#69698B")
        self.welcome.pack(padx = 20, pady= 80)
        self.button_pvp.pack(padx = 20, pady= 40)
        self.button_pve.pack(padx = 20, pady= 40)
        self.button_pve2.pack(padx = 20, pady= 40)

    def main(self):
        self.window.mainloop()

#----------------------------------------------------------------

def main():
    board = Menu()
    board.main()
    
if __name__ == "__main__":
    board = Menu()
    board.main()
