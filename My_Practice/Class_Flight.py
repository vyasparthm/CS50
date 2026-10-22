class Flight:
    def __init__(self, flight_number: str, capacity: int) -> None:
        if not flight_number or  not isinstance(flight_number,str):
            raise ValueError("Invalid Flight Number")
        if capacity <0:
            raise ValueError("Capacity must be greater than 0")

        self.flight_number = flight_number.strip().upper()
        self.capacity = capacity
        self.passengers: list[str] = []


    def add_passengers(self,name: str)-> bool:
        """Instance method: Reads and updates the specific instance's list"""
        if len(self.passengers) >= self.capacity:
            return False
        self.passengers.append(name.strip().title())
        return True

a = Flight("stark-001",100)
a.add_passengers("tony stark")
a.add_passengers("pepper potts")
print(f"{a.flight_number} has capacity of: {a.capacity} and currently holds:{len(a.passengers)} passengers, The passenger(s) are: {a.passengers}")
