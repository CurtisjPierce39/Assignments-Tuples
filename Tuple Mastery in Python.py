#Question 1 Task 1

def add_flight(flights):

    traveler = input("Please enter traveler name: ")
    origin = input("Please enter origin: ")
    dest = input("Please enter destination: ")
    flight = (traveler, origin, dest)
    
    if flight in flights:
        print("Itinerary already exists.")
    elif origin == dest:
        print("Origin and destination cannot be the same.")
    else:
        flights.append(flight)
        print("New Itinerary added!")

def display_flights(flights):
    if not flights:
        print("No Itineraries to display!")
    for i, flights in enumerate(flights):
        print(f"Itinerary {i + 1}: {flights[0]} From {flights[1]} to {flights[2]}.")

def main():

    flights = []

    while True:
        print("\nFlight Itinerary System")
        print("1. Add a flight")
        print("2. Display itineraries")
        print("3. Exit")
        
        choice = input("Please enter a choice: ")
        
        if choice == '1':
            add_flight(flights)
        elif choice == '2':
            display_flights(flights)
        elif choice == '3':
            print("\nThank you for using the Flight Itinerary System!")
            break
        else:
            print("Not a valid choice. Please select again")

main()