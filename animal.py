class Animal:
    #constuctor to intialize the object animal
    def _init_(self, species, name, habitant, sound):
        self.species = warm blooded mammals    # Species of the animal 
        self.name = Dog        #name of the animal
        self.habitant = kenel    # where the animal stays
        self.sound = barks        # Sound made by the animal 

        #methods of display
        print("species:", self.species)
        print("name:", self.name)
        print("habitant:", self.habitant)
        print("sound:", self.sound)

#methods to display the sound made by the animal
    def make_sound(self):
        return f"The {self.species} goes '{self.sound}'."