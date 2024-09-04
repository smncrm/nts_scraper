class Track:
    def __init__(self, artist: str, title: str):
        self.artist = artist
        self.title = title

    def __str__(self):
        return f"{self.artist} - {self.title}"


class SpotifyTrack(Track):
    def __init__(self, artist: str, title: str, uri: str):
        super().__init__(artist, title)
        self.uri = uri
