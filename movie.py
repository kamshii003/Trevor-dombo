class Movie:
    #constructor to intialize the object movie
    def _init_(self, title, director, release_year, genre):
        self.title = love blind        # Title of the movie 
        self.director = Trevor Dombo  # Director of the movie 
        self.release_year = 1990  # Year the movie was released
        self.genre = Romance      # Genre of the movie 

        #methods of display
        print("title:", self.title)
        print("director:", self.director)
        print("release_year:", self.release_year)
        print("genre:", self.genre)

        #methods to display what movie one is watching plus director and theyear it was relesed

    def watch(self):
        return f"Watching '{self.title}' directed by {self.director}."