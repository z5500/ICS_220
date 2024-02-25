import pygraphviz as pgv

# Create a new graph
G = pgv.AGraph(strict=True, directed=True)

# Add classes with attributes and methods
G.add_node("Passenger", shape="rectangle", style="bold")
G.add_node("Flight", shape="rectangle", style="bold")
G.add_node("Seat", shape="rectangle", style="bold")

# Add attributes and methods to Passenger class
G.add_node("+ name: str")
G.add_node("+ ticket_number: str")
G.add_node("+ electronic_ticket: bool")
G.add_node("+ boarding_time: str")
G.add_node("+ gate: str")
G.add_node("+ update_boarding_time(new_time: str): void")
G.add_node("+ update_gate(new_gate: str): void")

# Add attributes and methods to Flight class
G.add_node("+ number: str")
G.add_node("+ date: str")
G.add_node("+ departure: str")
G.add_node("+ arrival: str")
G.add_node("+ terminal: str")
G.add_node("+ change_departure_time(new_time: str): void")
G.add_node("+ change_arrival_time(new_time: str): void")

# Add attributes and methods to Seat class
G.add_node("+ number: str")
G.add_node("+ class_type: str")
G.add_node("+ change_seat(new_seat: str): void")

# Add relationships
G.add_edge("Passenger", "Flight", label="* has")
G.add_edge("Passenger", "Seat", label="* has")
G.add_edge("Flight", "Seat", label="* has")

# Add inheritance
G.add_edge("Passenger", "Person", label="inherits")
G.add_edge("Flight", "Airplane", label="inherits")

# Add aggregation
G.add_edge("Flight", "Crew", label="* has")

# Add multiplicity
G.add_edge("Flight", "Airport", label="[1]")
G.add_edge("Passenger", "Baggage", label="[0..*]")

# Save the graph
G.draw("revised_detailed_class_diagram.png", prog="dot")
