


def find_length(title):
    return len(title)


class Song():
    
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist
        self.length = find_length(title)

    def __repr__(self):
        return str(self.length)