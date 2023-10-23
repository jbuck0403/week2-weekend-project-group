class ParkingGarage():

    ticketPrice = 5
    
    def __init__(self, totalSpaces = 50):
        self.tickets = {} # a dict of dicts {#: bool}
        self.numServedTickets = 0
        self.servedTickets = []
        self.totalSpaces = totalSpaces
        self.occupiedSpaces = 0

    def getTicket(self):
        # if there are still spaces left in the garage
        if self.occupiedSpaces < self.totalSpaces:
            # update the number of tickets handed out
            self.numServedTickets += 1

            # add an unpaid ticket to the tickets dict
            self.tickets[self.numServedTickets] = False

            # increase number of occupied spaces
            self.occupiedSpaces += 1

            print(f"Ticket #{self.numServedTickets}\n")
        else:
            print("Sorry, the garage is full!")

    def payForTicket(self, ticketNum = False):
        
        """Excepts the ticket number to return a Bool value  
        """
        
        if not ticketNum: # to check if a ticket number was provided 
            ticketNum = self._getTicketNumber()
            
        if ticketNum == False:
            return False

        if self._checkPaid(ticketNum):
            print("Already paid\n")
        else:
            while True:
                paidA = int(input(f"\nThats {ParkingGarage.ticketPrice} bucks little man: "))
            
                if paidA > ParkingGarage.ticketPrice:
                    change = paidA - ParkingGarage.ticketPrice
                    print(f'Your change is ${change}\n')
                if paidA >= ParkingGarage.ticketPrice:
                    self.tickets[ticketNum] = True
                    break

        # returns True if ticket is paid, otherwise False
        return self._checkPaid(ticketNum)
            
    def leaveGarage(self):
        # ask for ticket
        ticketNum = self._getTicketNumber()

        if ticketNum == False:
            return

        # if ticket paid
        
        if paid := self.payForTicket(ticketNum):
            # add ticket num to served tickets list
            self.servedTickets.append(ticketNum)
            # remove the passed ticket from the tickets dict
            del self.tickets[ticketNum]

            # decrease number of occupied spaces
            self.occupiedSpaces -= 1

            # say goodbye
            print("Have a nice day!\n")

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
                ticketNum = int(input("\nWhat is your ticket number: "))
                if ticketNum > 0 and ticketNum in self.tickets.keys():
                    return ticketNum
                if not ticketNum in self.tickets.keys():
                    print("Ticket not available...\n")
                    return False
            except:
                continue

    def _checkPaid(self, ticketNum):
        #used to check if paid for ticket
        return self.tickets[ticketNum]

myGarage = ParkingGarage()
myGarage.garageRunner()





