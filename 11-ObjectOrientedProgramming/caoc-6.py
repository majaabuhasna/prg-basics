class Phone():
    def __init__(self,model,system,price):
        self.model = model
        self.system = system
        self.price = price
        self.is_on = False
        self.is_calling = False
        self.is_being_charged = False

    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False

    def calling(self):
        self.is_calling = True

    def not_calling(self):
        self.is_calling = False

    def charging(self):
        self.is_being_charged = True

    def not_charging(self):
        self.is_being_charged = False

    def display_info(self):
        print(f"My phone's model is {self.model}.")
        print(f"It runs on {self.system}.")
        print(f"It cost {self.price} PLN.")
        if self.is_on:
            print("It's currently turned on!")
        else:
            print("My phone's turned off right now. I'll use it later.")
        if self.is_calling:
            print("Someone's calling me.")
        else:
            print("Nobody's calling me at the moment.")
        if self.is_being_charged:
            print("It's being charged. It was low on battery.")
        else:
            print("I don't need to charge it yet.")

def main():
    my_phone = Phone('iPhone 12','iOS',3000)
    my_phone.turn_on()
    my_phone.calling()
    my_phone.charging()
    my_phone.display_info()

if __name__ == '__main__':
    main()