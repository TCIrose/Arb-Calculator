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
        title.grid(row = 0, column = 2)
        bookmaker = tk.Label(self.master, text = "Odds")
        bookmaker.grid(row = 2, column = 0)
        
        #home team win odds
        one = tk.Label(self.master, text = "1")
        one.grid(row = 4, column = 0)
        firstentry = tk.Entry(self.master, textvariable = self.odds1)
        firstentry.grid(row = 6, column = 0)
        
        #draw odds
        draw = tk.Label(self.master, text = "X")
        draw.grid(row = 4, column = 2)
        secondentry = tk.Entry(self.master, textvariable = self.odds2)
        secondentry.grid(row = 6, column = 2)

        #away team wins odds
        two = tk.Label(self.master, text = "2")
        two.grid(row = 4, column = 3)
        thirdentry = tk.Entry(self.master, textvariable = self.odds3)
        thirdentry.grid(row = 6, column = 3)
        
        #Adding the stake entry and  labels 
        #stakes variables
        self.staketotal = tk.StringVar()
        
        #total stake entry
        totalstake = tk.Label(self.master, text = "Total Stake")
        totalstake.grid(row = 8, column = 0 )
        tstake = tk.Entry(self.master, textvariable = self.staketotal)
        tstake.grid(row = 8, column = 2)

        #button to get outcomes
        savebutton = tk.Button(self.master, text = "save", command = self.Calc3way)
        savebutton.grid(row = 10, column = 2)

        #total %profit label
        self.percprofitTag = tk.Label(self.master, text = "Arb percentage")
        self.percprofitTag.grid(row = 12, column = 2)
        self.percprofitArb = tk.Label(self.master, text = "0.00%")
        self.percprofitArb.grid(row = 14, column = 2)

        stakes = tk.Label(self.master, text = "Stakes")
        stakes.grid(row = 16, column = 2)

        #home team stake
        one = tk.Label(self.master, text = "1")
        one.grid(row = 18, column = 0)
        self.hstake = tk.Label(self.master, text = 0.00)
        self.hstake.grid(row = 20, column = 0)

        #draw stake
        draw = tk.Label(self.master, text = "X")
        draw.grid(row = 18, column = 2)
        self.dstake = tk.Label(self.master, text = 0.00)
        self.dstake.grid(row = 20, column = 2)

        #away team stake
        two = tk.Label(self.master, text = "2")
        two.grid(row = 18, column = 3)
        self.astake = tk.Label(self.master, text = 0.00)
        self.astake.grid(row = 20, column = 3)

        #Outcomes labels
        outcomesLabel = tk.Label(self.master, text = "Outcomes")
        outcomesLabel.grid(row = 22, column = 2)

        one = tk.Label(self.master, text = "1")
        one.grid(row = 24, column = 0)
        self.outcome1 = tk.Label(self.master, text = 0.00)
        self.outcome1.grid(row = 26, column = 0)

        draw = tk.Label(self.master, text = "X")
        draw.grid(row = 24, column = 2)
        self.outcomex = tk.Label(self.master, text = 0.00)
        self.outcomex.grid(row = 26, column = 2)
        
        two = tk.Label(self.master, text = "2")
        two.grid(row = 24, column = 3)
        self.outcome2 = tk.Label(self.master, text = 0.00)
        self.outcome2.grid(row = 26, column = 3)

        #profit labels
        proflabel = tk.Label(self.master, text = "Potential Profit")
        proflabel.grid(row = 30, column = 2)
        one = tk.Label(self.master, text = "1")
        one.grid(row = 32, column = 0)
        self.prof1 = tk.Label(self.master, text = 0.00)
        self.prof1.grid(row = 34, column = 0)
        draw = tk.Label(self.master, text = "X")
        draw.grid(row = 32, column = 2)
        self.prof2 = tk.Label(self.master, text = 0.00)
        self.prof2.grid(row = 34, column = 2)
        two = tk.Label(self.master, text = "2")
        two.grid(row = 32, column = 3)
        self.prof3 = tk.Label(self.master, text = 0.00)
        self.prof3.grid(row = 34, column = 3)
        
        #total profit label
        self.profitTag = tk.Label(self.master, text = "Net profit")
        self.profitTag.grid(row = 36, column = 2)
        self.profitArb = tk.Label(self.master, text = 0.00)
        self.profitArb.grid(row = 38, column = 2)


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
        arbperc = round((100 - totalArb),2)
        
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
        
        #find net profit(uses the least of potential profit per outcome)
        profits = [pA,pX,pB]
        profits.sort()
        netProfit = profits[0]

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

        #configure the total % profit arb label
        self.percprofitArb.configure(text = f"{arbperc}%")

        #configure the net profit label
        self.profitArb.configure(text = netProfit)

    


