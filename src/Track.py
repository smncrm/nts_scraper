class Track:
    def __init__(self, artist: str, title: str):
        self.artist = artist
        self.title = title

    def __str__(self):
        return f"{self.artist} - {self.title}"
