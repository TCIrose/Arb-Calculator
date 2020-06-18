import tkinter as tk

class Arb:
    """
    Class that initializes tkninter root
    """
    def __init__(self, master):
        #root window
        self.master = master

        #widgets
        #labels
        title = tk.Label(self.master, text = "ARBITRAGE CALCULATOR")
        title.pack()
        bookmaker = tk.Label(self.master, text = "Bookmakers Odds")
        bookmaker.pack()
        self.odds1 = tk.StringVar()
        self.odds2 = tk.StringVar()
        self.odds3 = tk.StringVar()
        firstentry = tk.Entry(self.master, textvariable = self.odds1)
        firstentry.pack()
        secondentry = tk.Entry(self.master, textvariable = self.odds2)
        secondentry.pack()
        thirdentry = tk.Entry(self.master, textvariable = self.odds3)
        thirdentry.pack()
        savebutton = tk.Button(self.master, text = "save", command = self.saveodds)
        savebutton.pack()
        
    def saveodds(self):
        o1 = float(self.odds1.get())
        o2 = float(self.odds2.get())
        o3 = float(self.odds3.get())
        print(f"{o1}  {o2}  {o3}")



