class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        # Prints the details of the ride
        print("Taxi ride receipt:")
        print(f"Distance: {self.distance} km")
        print(f"Rate per km: €{self.rate_per_km}")
        print(f"Fare: €{self.fare:.2f}\n")

def main():
    # your program
    ride1 = TaxiRide(rate_per_km=2.50)
    ride2 = TaxiRide(rate_per_km=3.00)

    ride1.calculate_fare(15)
    ride2.calculate_fare(10)

    ride1.print_receipt()
    ride2.print_receipt()

if __name__ == "__main__":
    main()
