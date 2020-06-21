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
        bookmaker = tk.Label(self.master, text = "Odds")
        bookmaker.pack()
        self.odds1 = tk.StringVar()
        self.odds2 = tk.StringVar()
        self.odds3 = tk.StringVar()

        #home team win odds
        one = tk.Label(self.master, text = "1")
        one.pack()
        firstentry = tk.Entry(self.master, textvariable = self.odds1)
        firstentry.pack()
        
        #draw odds
        draw = tk.Label(self.master, text = "X")
        draw.pack()
        secondentry = tk.Entry(self.master, textvariable = self.odds2)
        secondentry.pack()

        #away team wins odds
        two = tk.Label(self.master, text = "2")
        two.pack()
        thirdentry = tk.Entry(self.master, textvariable = self.odds3)
        thirdentry.pack()
        savebutton = tk.Button(self.master, text = "save", command = self.saveodds)
        savebutton.pack()

        #Adding the stake entries and  labels 
        stakes = tk.Label(self.master, text = "Stake")
        stakes.pack()

        #stakes variables
        stakeone = tk.StringVar()
        stakedraw = tk.StringVar()
        staketwo = tk.StringVar()

        #home team stake
        one = tk.Label(self.master, text = "1")
        one.pack()
        hstake = tk.Entry(self.master, textvariable = stakeone)
        hstake.pack()

        #draw stake
        draw = tk.Label(self.master, text = "X")
        draw.pack()
        dstake = tk.Entry(self.master, textvariable = stakedraw)
        dstake.pack()

        #away team stake
        two = tk.Label(self.master, text = "2")
        two.pack()
        astake = tk.Entry(self.master, textvariable = staketwo)
        astake.pack()
        
        #button to get stakes
        stakesButton = tk.Button(self.master, text = "calculate", command = self.getStakes)
        stakesButton.pack()

    def saveodds(self):
        o1 = float(self.odds1.get())
        o2 = float(self.odds2.get())
        o3 = float(self.odds3.get())
        print(f"{o1}  {o2}  {o3}")

    def getStakes(self):
        pass



