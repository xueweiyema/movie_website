import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

    def __init__(self, movie_title, movie_storyline, poster_image_url,
                 trailer_youtube_url, movie_imdb):
        """
        initial function
        Args:
            self: nothing more than a convention
            movie_title: title of movie
            movie_storyline: storyline of movie
            poster_image_url: url of poster
            trailer_youtube_url: url of trailer
            movie_imdb: score of imdb

        Returns:
            None

        Raises:
            None
        """

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.imdb = movie_imdb

    def show_trailer(self):
        """
        Open a browser to play a trailer
        Args:
            self: nothing more than a convention

        Returns:
            None

        Raises:
            None
        """
        webbrowser.open(self.trailer_youtube_url)
