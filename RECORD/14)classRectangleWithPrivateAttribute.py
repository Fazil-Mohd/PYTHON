class Rectangle:
    def __init__(self):
        # Private attributes for length and width with default values
        self.__length = 1.0
        self.__width = 1.0

    def __str__(self):
        # Provides a string representation of the class
        return "This is class Rectangle"

    def set_length(self, len=1.0):  # len=1 --> default value
        # Setter for length, with a default value of 1.0
        self.__length = len

    def set_width(self, wid=1.0):  # wid=1 --> default value
        # Setter for width, with a default value of 1.0
        self.__width = wid

    def get_length(self):
        # Getter for length
        return self.__length

    def get_width(self):
        # Getter for width
        return self.__width

    def get_area(self):
        # Calculates and returns the area of the rectangle
        return self.get_width() * self.get_length()

    def __lt__(self, other):
        # Overloads the '<' operator to compare the areas of two rectangles
        # Returns which rectangle is smaller based on area
        if self.get_area() < other.get_area():
            return "1st Rectangle is Smaller."
        else:
            return "2nd Rectangle is Smaller."

# Creating the first rectangle
my_rect1 = Rectangle()
my_rect1.set_length(4.0)  # Setting length to 4.0
my_rect1.set_width(2.0)   # Setting width to 2.0
print("The length is ", my_rect1.get_length())  # Display length
print("The width is ", my_rect1.get_width())    # Display width
print("The area is ", my_rect1.get_area())      # Display area
print(my_rect1)  # Display the rectangle object (calls __str__)

# Creating the second rectangle
my_rect2 = Rectangle()
my_rect2.set_length(5.0)  # Setting length to 5.0
my_rect2.set_width(3.0)   # Setting width to 3.0
print("The length is ", my_rect2.get_length())  # Display length
print("The width is ", my_rect2.get_width())    # Display width
print("The area is ", my_rect2.get_area())      # Display area
print(my_rect2)  # Display the rectangle object (calls __str__)

# Comparing the two rectangles using the overloaded '<' operator
print(my_rect1 < my_rect2)  
