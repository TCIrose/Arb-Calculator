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
        title.grid(row = 0, column = 10)
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
        two.grid(row = 4, column = 4)
        thirdentry = tk.Entry(self.master, textvariable = self.odds3)
        thirdentry.grid(row = 6, column = 4)
        
        #Adding the stake entry and  labels 
        #stakes variables
        self.staketotal = tk.StringVar()
        
        #total stake entry
        totalstake = tk.Label(self.master, text = "Total Stake")
        totalstake.grid(row = 2, column = 6 )
        tstake = tk.Entry(self.master, textvariable = self.staketotal)
        tstake.grid(row = 6, column = 6)

        #button to get outcomes
        savebutton = tk.Button(self.master, text = "save", command = self.Calc3way)
        savebutton.grid(row = 8, column = 6)

        #total %profit label
        self.percprofitTag = tk.Label(self.master, text = "Arb percentage")
        self.percprofitTag.grid(row = 2, column = 8)
        self.percprofitArb = tk.Label(self.master, text = "0.00%")
        self.percprofitArb.grid(row = 6, column = 8)

        stakes = tk.Label(self.master, text = "Stakes")
        stakes.grid(row = 2, column = 10)

        #home team stake
        one = tk.Label(self.master, text = "1")
        one.grid(row = 4, column = 10)
        self.hstake = tk.Label(self.master, text = 0.00)
        self.hstake.grid(row = 6, column = 10)

        #draw stake
        draw = tk.Label(self.master, text = "X")
        draw.grid(row = 4, column = 12)
        self.dstake = tk.Label(self.master, text = 0.00)
        self.dstake.grid(row = 6, column = 12)

        #away team stake
        two = tk.Label(self.master, text = "2")
        two.grid(row = 4, column = 14)
        self.astake = tk.Label(self.master, text = 0.00)
        self.astake.grid(row = 6, column = 14)

        #Outcomes labels
        outcomesLabel = tk.Label(self.master, text = "Outcomes")
        outcomesLabel.grid(row = 2, column = 16)

        one = tk.Label(self.master, text = "1")
        one.grid(row = 4, column = 16)
        self.outcome1 = tk.Label(self.master, text = 0.00)
        self.outcome1.grid(row = 6, column = 16)

        draw = tk.Label(self.master, text = "X")
        draw.grid(row = 4, column = 18)
        self.outcomex = tk.Label(self.master, text = 0.00)
        self.outcomex.grid(row = 6, column = 18)
        
        two = tk.Label(self.master, text = "2")
        two.grid(row = 4, column = 20)
        self.outcome2 = tk.Label(self.master, text = 0.00)
        self.outcome2.grid(row = 6, column = 20)

        #profit labels
        one = tk.Label(self.master, text = "1")
        one.grid(row = 4, column = 22)
        self.prof1 = tk.Label(self.master, text = 0.00)
        self.prof1.grid(row = 6, column = 22)
        draw = tk.Label(self.master, text = "X")
        draw.grid(row = 4, column = 24)
        self.prof2 = tk.Label(self.master, text = 0.00)
        self.prof2.grid(row = 6, column = 24)
        two = tk.Label(self.master, text = "3")
        two.grid(row = 4, column = 26)
        self.prof3 = tk.Label(self.master, text = 0.00)
        self.prof3.grid(row = 6, column = 26)
        
        #total profit label
        self.profitTag = tk.Label(self.master, text = "Net profit")
        self.profitTag.grid(row = 2, column = 28)
        self.profitArb = tk.Label(self.master, text = 0.00)
        self.profitArb.grid(row = 6, column = 28)


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

    


