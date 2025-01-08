class Car:
    def __init__(self, company, price, color):
        self.company = company
        self.price = price
        self.color = color

    def display_details(self):
        print("Company:", self.company)
        print("Price:", self.price)
        print("Color:", self.color)
        print()

# Create 3 car objects
car1 = Car("Toyota", 20000, "Red")
car2 = Car("Honda", 25000, "Blue")
car3 = Car("Ford", 18000, "Black")

# Display details of each car
car1.display_details()
car2.display_details()
car3.display_details()
