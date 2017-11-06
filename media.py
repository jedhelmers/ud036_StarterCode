import webbrowser

class Movie():
    """valid ratings are the standard movie ratings.
__init__ creates class and space in memory.
show_trailer opens web browser to show trailer."""


    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, star_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.ratings = star_rating
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
