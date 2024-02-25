class BoardingPass:
    def __init__(self, passenger, flight, seat):
        self.passenger = passenger
        self.flight = flight
        self.seat = seat

    def update_passenger_information(self, new_info):
        pass  # Update passenger information

    def cancel_boarding_pass(self):
        pass  # Cancel boarding pass


class Passenger:
    def __init__(self, name, ticket_number, electronic_ticket):
        self.name = name
        self.ticket_number = ticket_number
        self.electronic_ticket = electronic_ticket
        self.boarding_time = None
        self.gate = None

    def update_boarding_time(self, new_time):
        pass  # Update boarding time

    def update_gate(self, new_gate):
        pass  # Update gate


class Flight:
    def __init__(self, number, date, departure, arrival, terminal):
        self.number = number
        self.date = date
        self.departure = departure
        self.arrival = arrival
        self.terminal = terminal

    def change_departure_time(self, new_time):
        pass  # Change departure time

    def change_arrival_time(self, new_time):
        pass  # Change arrival time


class Seat:
    def __init__(self, number, class_type):
        self.number = number
        self.class_type = class_type

    def change_seat(self, new_seat):
        pass  # Change seat


# Instantiate objects
passenger = Passenger("James Smith", "629", True)
flight = Flight("NA4321", "06 DEC 20", "Chicago ORD", "New York JFK", "2")
seat = Seat("09A", "First Class")
boarding_pass = BoardingPass(passenger, flight, seat)

# Populate and display boarding pass details
print("Passenger:", boarding_pass.passenger.name)
print("Flight Number:", boarding_pass.flight.number)
print("Date:", boarding_pass.flight.date)
print("Departure:", boarding_pass.flight.departure)
print("Arrival:", boarding_pass.flight.arrival)
print("Terminal:", boarding_pass.flight.terminal)
print("Seat:", boarding_pass.seat.number)
