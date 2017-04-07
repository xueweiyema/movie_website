import webbrowser

class Movie():
    """This class provides a way to store movie related information"""

    def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube_url,movie_imdb):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.imdb=movie_imdb

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
