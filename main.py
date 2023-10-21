# Your parking garage class should have the following methods:
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

'''
pseudo code

parking garage

    comes in and gets a ticket
        -price
        number - consecutive tickets numbers
        -timestamp
        -date
        {'paid': True}

    pay for their ticket

    leave the garage
        ticket
        make sure its paid
            if paid
                leave
            if not paid
                make them pay
                then leave
'''

class ParkingGarage():

    ticketPrice = 5
    
    def __init__(self):
        self.tickets = {} # a dict of dicts {'paid': True}
        self.numServedTickets = 0
        self.servedTickets = []

    def getTicket(self):
        # update the number of tickets handed out
        self.numServedTickets += 1

        # add an unpaid ticket to the tickets dict
        self.tickets[self.numServedTickets] = False

    def payForTicket(self):
        ticketNum = self._getTicketNumber()
        if self._checkPaid(ticketNum):
            
            print("Already paid")  
        else:
            while True:
                paidA = int(input(f"Thats {ParkingGarage.ticketPrice} bucks little man"))
            
                if paidA >= ParkingGarage.ticketPrice:
                    self.tickets[ticketNum] = True
                if paidA > ParkingGarage.ticketPrice:
                    change = paidA - ParkingGarage.ticketPrice
                    print(f'Your change is ${change}')
            
        
        
      
        print(self.tickets)


    def _getTicketNumber(self):
        while True:
            try: 
                ticketNum = int(input("What is your ticket number"))
                if ticketNum > 0 and ticketNum in self.tickets.keys():
                    return ticketNum
            except: 
                continue


    def _checkPaid(self, ticketNum):
        
        return self.tickets[ticketNum]
    


        
    def leaveGarage(self):
        
    # leave the garage
    #     ticket
     ticketNum = self._getTicketNumber()

    #     make sure its paid

    #         if paid
    
    #             leave
    #         if not paid
    #             make them pay
    #             then leave

        # add ticket num to served tickets list

     self.servedTickets.append(ticketNum)

        # remove the passed ticket from the tickets dict
     del self.tickets[ticketNum]


myGarage = ParkingGarage()
myGarage.getTicket()
myGarage.getTicket()
myGarage.getTicket()
myGarage.getTicket()
myGarage.getTicket()
myGarage.getTicket()
myGarage.payForTicket()




