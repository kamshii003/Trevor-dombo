class Car:
    #Constructor to intialize the laptop object
    def _init_(self, make, model, year, color):
        self.maker = toyota         # Brand of the car 
        self.model = Camry        # Model of the car 
        self.year = 2000          # Year of manufacture
        self.color = red        # Color of the car 

        #Method to display the phone detail
    def display(self):
        print("maker:", self.maker)
        print("model:", self.model)
        print("year:", self.year)
        print("color:", self.color)

        #method to start car
        def start_engine(self):
        return f"The {self.color} {self.make} {self.model} is starting its engine."