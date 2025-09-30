class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        self.bookedSeats = []

    def getsStatus(self):
        print("************")
        print(f"The name if the trai is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print("************")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookTicket(self):
        if (self.seats > 0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.bookedSeats.append(self.seats)
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full! Kindly try in tatkal")

    def cancelTicket(self, seatNo):
        if (seatNo in self.bookedSeats):
            self.bookedSeats.remove(seatNo)
            self.seats += 1
            print(f"Your ticket for seat number {seatNo} has been cancelled successfully!")
        else:
            print(f"Seat number {seatNo} was not booked, so cannot be cancelled.")

intercity = Train("Intercity Express: 14015", 90, 2)
# intercity = Train("Intercity Express: 14015", 90, 300)
intercity.getsStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getsStatus()
intercity.cancelTicket(2)
intercity.getsStatus()