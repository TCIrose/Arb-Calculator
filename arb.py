import tkinter as tk

class Arb:
    """
    Class that initializes tkninter root
    """
    def __init__(self, master):
        #root window
        self.master = master

        #odds variables
        self.odds1 = tk.StringVar()
        self.odds2 = tk.StringVar()
        self.odds3 = tk.StringVar()


        #widgets
        #labels
        title = tk.Label(self.master, text = "ARBITRAGE CALCULATOR")
        title.pack()
        bookmaker = tk.Label(self.master, text = "Odds")
        bookmaker.pack()
        
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
        
        #Adding the stake entry and  labels 
        #stakes variables
        self.staketotal = tk.StringVar()
        
        #total stake entry
        totalstake = tk.Label(self.master, text = "Total Stake")
        totalstake.pack()
        tstake = tk.Entry(self.master, textvariable = self.staketotal)
        tstake.pack()

        #button to get outcomes
        savebutton = tk.Button(self.master, text = "save", command = self.Calc3way)
        savebutton.pack()

        stakes = tk.Label(self.master, text = "Stakes")
        stakes.pack()

        #home team stake
        one = tk.Label(self.master, text = "1")
        one.pack()
        self.hstake = tk.Label(self.master, text = 0.00)
        self.hstake.pack()

        #draw stake
        draw = tk.Label(self.master, text = "X")
        draw.pack()
        self.dstake = tk.Label(self.master, text = 0.00)
        self.dstake.pack()

        #away team stake
        two = tk.Label(self.master, text = "2")
        two.pack()
        self.astake = tk.Label(self.master, text = 0.00)
        self.astake.pack()

        #Outcomes labels
        outcomesLabel = tk.Label(self.master, text = "Outcomes")
        outcomesLabel.pack()

        one = tk.Label(self.master, text = "1")
        one.pack()
        self.outcome1 = tk.Label(self.master, text = 0.00)
        self.outcome1.pack()

        draw = tk.Label(self.master, text = "X")
        draw.pack()
        self.outcomex = tk.Label(self.master, text = 0.00)
        self.outcomex.pack()
        
        two = tk.Label(self.master, text = "2")
        two.pack()
        self.outcome2 = tk.Label(self.master, text = 0.00)
        self.outcome2.pack()

        #profit labels
        one = tk.Label(self.master, text = "1")
        one.pack()
        self.prof1 = tk.Label(self.master, text = 0.00)
        self.prof1.pack()
        draw = tk.Label(self.master, text = "X")
        draw.pack()
        self.prof2 = tk.Label(self.master, text = 0.00)
        self.prof2.pack()
        two = tk.Label(self.master, text = "3")
        two.pack()
        self.prof3 = tk.Label(self.master, text = 0.00)
        self.prof3.pack()


    def Calc3way(self):
        """
        Method to: 
        1. Calculate the percentage of a 3 way arb
        2. Calculate stake to be placed for each outcome
    
        """
        
        #Just the total stake input for now
        o1 = float(self.odds1.get())
        o2 = float(self.odds2.get())
        o3 = float(self.odds3.get())
        
        #Individual Arbitrage calculation
        o1A = (1/o1)*100
        o1X = (1/o2)*100
        o1B = (1/o3)*100

        #total arbitrage
        totalArb = round((o1A + o1X + o1B),2)
        arbperc = round((100 - totalArb), 2)
        print(totalArb)

        #profit label
        profitArb = tk.Label(self.master, text = f"{arbperc}%")
        profitArb.pack()
        print(arbperc)
        
        #get total stake
        Tstake = float(self.staketotal.get())
        
        #calculate stakes for each outcome
        stakeA = round(((Tstake*o1A)/totalArb),2)
        stakeX = round(((Tstake*o1X)/totalArb),2)
        stakeB = round(((Tstake*o1B)/totalArb),2)

        #Calculate each possible outcome
        outcA = round((stakeA*o1), 2)
        outcX = round((stakeX*o2),2)
        outcB = round((stakeB*o3),2)

        
        #profit per outcome
        pA = round((outcA - Tstake),2)
        pX = round((outcX - Tstake),2)
        pB = round((outcB - Tstake),2)


        #configure labels to show stakes
        self.hstake.configure(text = stakeA)
        self.dstake.configure(text = stakeX)        
        self.astake.configure(text = stakeB)

        #configure labels to show potential outcomes
        self.outcome1.configure(text = outcA)
        self.outcomex.configure(text = outcX)
        self.outcome2.configure(text = outcB)

        #configure labels to show profit per outcome
        self.prof1.configure(text = pA)        
        self.prof2.configure(text = pX)
        self.prof3.configure(text = pB)

    


