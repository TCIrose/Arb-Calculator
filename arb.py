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
        savebutton = tk.Button(self.master, text = "save", command = self.Calc3way)
        savebutton.pack()

        #Adding the stake entries and  labels 

        #stakes variables
        self.staketotal = tk.StringVar()
        
        #total stake entry
        totalstake = tk.Label(self.master, text = "Total Stake")
        totalstake.pack()
        tstake = tk.Entry(self.master, textvariable = self.staketotal)
        tstake.pack()

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
        
        #button to get stakes
        stakesButton = tk.Button(self.master, text = "calculate", command = self.Calc3wayStakes)
        stakesButton.pack()

        #Outcomes entries(disabled)
        self.o1 =tk.StringVar()
        self.ox =tk.StringVar()
        self.o2 =tk.StringVar()

        outcomesLabel = tk.Label(self.master, text = "Outcomes")
        outcomesLabel.pack()

        one = tk.Label(self.master, text = "1")
        one.pack()
        self.outcome1 = tk.Entry(self.master, textvariable = self.o1)
        self.outcome1.pack()

        draw = tk.Label(self.master, text = "X")
        draw.pack()
        self.outcomex = tk.Entry(self.master, textvariable = self.ox)
        self.outcomex.pack()
        
        two = tk.Label(self.master, text = "2")
        two.pack()
        self.outcome2 = tk.Entry(self.master, textvariable = self.o2)
        self.outcome2.pack()

        #button to get outcomes
        outcomesButton = tk.Button(self.master, text = "calculate", command = self.getOutcomes)
        outcomesButton.pack()

        #profit entry(disabled)
        self.prof = tk.StringVar()
        profi = tk.Entry(self.master, textvariable = self.prof)
        profi.pack()

        #button to show profit
        profitButton = tk.Button(self.master, text = "Calulate Profit", command = self.getProfit)
        profitButton.pack()


    def Calc3way(self):
        """
        Method to calculate the percentage of a 3 way arb
        """
        o1 = float(self.odds1.get())
        o2 = float(self.odds2.get())
        o3 = float(self.odds3.get())
        
        #Individual Arbitrage calculation
        o1A = (1/o1)*100
        o1X = (1/o2)*100
        o1B = (1/o3)*100
        totalArb = round((o1A + o1X + o1B),2)
        
        #profit entry(disabled)
        profitEntry = tk.Label(self.master, text = totalArb)
        profitEntry.pack()
        print(totalArb)
        


    def Calc3wayStakes(self):
        """
        Method to calculate stake to be placed for each outcome
        """
        #Just the total stake input for now
        o1 = float(self.odds1.get())
        o2 = float(self.odds2.get())
        o3 = float(self.odds3.get())
        
        #Individual Arbitrage calculation
        o1A = (1/o1)*100
        o1X = (1/o2)*100
        o1B = (1/o3)*100
        totalArb = round((o1A + o1X + o1B),2)

        #get total stake
        Tstake = float(self.staketotal.get())
        
        #calculate stakes for each outcome
        stakeA = round(((Tstake*o1A)/totalArb),2)
        stakeX = round(((Tstake*o1X)/totalArb),2)
        stakeB = round(((Tstake*o1B)/totalArb),2)

        #configure labels to show stakes
        self.hstake.configure(text = stakeA)

        self.dstake.configure(text = stakeX)
        
        self.astake.configure(text = stakeB)

        print(f"{stakeA} {stakeX} {stakeB}")
        print(stakeA+stakeB+stakeX)
        

    def getOutcomes(self):
        ot1 = float(self.o1.get())
        otx = float(self.ox.get())
        ot2 = float(self.o2.get())
        print(f"{ot1} {otx} {ot2}")

    def getProfit(self):
        p = float(self.prof.get())
        print(p)



