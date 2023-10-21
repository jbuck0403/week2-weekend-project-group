class ParkingGarage():

    ticketPrice = 5
    
    def __init__(self):
        self.tickets = {} # a dict of dicts {#: True}
        self.numServedTickets = 0
        self.servedTickets = []

    def getTicket(self):
        # update the number of tickets handed out
        self.numServedTickets += 1

        # add an unpaid ticket to the tickets dict
        self.tickets[self.numServedTickets] = False

    def payForTicket(self, ticketNum = False):
        
        """Exceptes the ticket number to return a Bool value  
        """
        
        if not ticketNum: # to check if a ticket number was provided 
            ticketNum = self._getTicketNumber()
            
        if self._checkPaid(ticketNum):
            print("Already paid")
        else:
            while True:
                paidA = int(input(f"Thats {ParkingGarage.ticketPrice} bucks little man: "))
            
                if paidA > ParkingGarage.ticketPrice:
                    change = paidA - ParkingGarage.ticketPrice
                    print(f'Your change is ${change}')
                if paidA >= ParkingGarage.ticketPrice:
                    self.tickets[ticketNum] = True
                    break

        # returns True if ticket is paid, otherwise False
        return self._checkPaid(ticketNum)
            
    def leaveGarage(self):
        # ask for ticket
        ticketNum = self._getTicketNumber()
        # if ticket paid
        
        if paid := self.payForTicket(ticketNum):
            # add ticket num to served tickets list
            self.servedTickets.append(ticketNum)
            # remove the passed ticket from the tickets dict
            del self.tickets[ticketNum]
            # say goodbye
            print("Have a nice day!")

        return paid
            
    def garageRunner(self):
        """Primary function to run code - allows for user input to run methods"""
        while True:
            userInput = input("What would you like to do?\n[T]icket/[P]ay Ticket/[L]eave Garage or [Q]uit: ")
            try:
                userInput = userInput.lower()[0]
            except:
                continue

            if userInput == 't':
                self.getTicket()
            elif userInput == 'p':
                self.payForTicket()
            elif userInput == 'l':
                self.leaveGarage()
            elif userInput == 'q':
                print("Thanks for parking!")
                break

    def _getTicketNumber(self):
        """requests user input
        
        returns ticketNum"""
       
        while True:
            try: # used exception handling to only accept the correct input
                ticketNum = int(input("What is your ticket number: "))
                if ticketNum > 0 and ticketNum in self.tickets.keys():
                    return ticketNum
            except:
                continue

    def _checkPaid(self, ticketNum):
        #used to check if paid for ticket
        
        return self.tickets[ticketNum]

myGarage = ParkingGarage()
myGarage.garageRunner()





