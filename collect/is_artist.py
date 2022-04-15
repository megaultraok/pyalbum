import requests
from bs4 import BeautifulSoup

def is_artist(wiki_url: str, artist: str) -> bool:
    """
    Checks whether album is made by artist
    Parameters:
        wiki_url: a string of the Wikipedia entry for the album
        artist: a string of the artist's name (exact spelling)
    Returns:
        A Boolean value describing whether the album is associated with the artist
    """
    # If artist name passed is invalid, raise error
    if artist == None:
        raise AttributeError("No artist found in Wikipedia. Perhaps it was misspelled?")
    try:
        req = requests.get(wiki_url)
        soup = BeautifulSoup(req.text, 'html.parser')
        short_descrp = soup.find(class_="shortdescription")
        # If artist name passed is found in Wikipedia entry, return True
        if artist.lower() in short_descrp.get_text().lower():
            return True
        return False
    except requests.ConnectionError as conerr:
        print(f"{conerr}: Cannot connect to Wikipedia.")