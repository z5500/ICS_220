import pygraphviz as pgv

# Create a new graph
G = pgv.AGraph(strict=True, directed=True)

# Add actors and use cases
G.add_node("Passenger", shape="box")
G.add_node("Airline Staff", shape="box")
G.add_node("Generate Boarding Pass", shape="ellipse")
G.add_node("Update Passenger Information", shape="ellipse")
G.add_node("Cancel Boarding Pass", shape="ellipse")

# Add relationships
G.add_edge("Passenger", "Generate Boarding Pass", label="performs")
G.add_edge("Passenger", "Update Passenger Information", label="performs")
G.add_edge("Passenger", "Cancel Boarding Pass", label="performs")
G.add_edge("Airline Staff", "Generate Boarding Pass", label="performs")
G.add_edge("Airline Staff", "Update Passenger Information", label="performs")
G.add_edge("Airline Staff", "Cancel Boarding Pass", label="performs")

# Add system boundary
G.add_node("System Boundary", shape="box", style="dashed")

# Place elements within the system boundary
G.add_edge("System Boundary", "Passenger", style="invisible")
G.add_edge("System Boundary", "Airline Staff", style="invisible")
G.add_edge("System Boundary", "Generate Boarding Pass", style="invisible")
G.add_edge("System Boundary", "Update Passenger Information", style="invisible")
G.add_edge("System Boundary", "Cancel Boarding Pass", style="invisible")

# Save the graph
G.draw("revised_airline_use_case_diagram.png", prog="dot")
