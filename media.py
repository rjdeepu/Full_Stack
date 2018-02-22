import webbrowser

class Movie():
    """This class gets the details like movie title, storyline, poster and Trailer"""
    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        #Storing all the input values to create an instance when called
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        #Webbrowser open function will open an URL passed into it as input
        webbrowser.open(self.trailer_youtube_url)
