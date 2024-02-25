from PyClasses import BoardingPass, Flight, Passenger, Seat


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
