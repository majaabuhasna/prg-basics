import random

class Thermometer:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("You turned the thermometer on")
    
    def turn_off(self):
        self.is_on = False
        print("You turned the thermometer off")

    def measure(self):
        if self.is_on:
            self.temperature = round(random.uniform(34.0,42.0),1)
            print("Temperature measured")
        else:
            print("Turn on the thermometer first!")

    def display(self):
        if self.temperature >= 41.0:
            print(f"Temperature: {self.temperature}C (CRITICAL TEMPERATURE!!)")
        elif self.temperature >= 37.0:
            print(f"Temperature: {self.temperature}C (fever)")
        else:
            print(f"Temperature: {self.temperature}C")

def main():
    my_thermometer = Thermometer()
    my_thermometer.turn_on()
    my_thermometer.measure()
    my_thermometer.display()
    my_thermometer.turn_off()

if __name__ == "__main__":
    main()