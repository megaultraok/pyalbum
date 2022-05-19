import requests
from bs4 import BeautifulSoup

def gather_tracks(wiki_url: str) -> dict:
    """
    Collects track list from Wikipedia entry of album

    Parameters:
        wiki_url: a string of the Wikipedia entry for the album
    Returns:
        A playlist dictionary of the album
    """
    try:
        req = requests.get(wiki_url)
        soup = BeautifulSoup(req.text, 'html.parser')
        tracks_tables = soup.find_all("table", class_="tracklist")
        side_tables = [t for t in tracks_tables if "Side" in t.caption.text]
        track_order = {}
        track_names = []
        track_durations = []

        if tracks_tables is None:
            raise AttributeError("No track list found in this album's Wikipedia entry.")

        if side_tables:
            tracks_tables = side_tables

            for table in tracks_tables:
                for tr in table.find_all("tr"):
                    td = tr.find("td")
                    if td is None or td.b:
                        continue
                    elif not td.find_all("a"):
                        track_names.append(td.get_text().strip("\""))
                    else:
                        track_names.append(td.text.replace("\"", ""))

                    track_duration = tr.find("td", attrs={
                        'style': 'padding-right:10px;text-align:right;vertical-align:top'
                    })
                    track_durations.append(track_duration.get_text())
        else:
            tracks_table = soup.find("table", class_="tracklist")

            for tr in tracks_table.find_all("tr"):
                td = tr.find("td")
                if td is None or td.b:
                    continue
                elif not td.find_all("a"):
                    track_names.append(td.get_text().strip("\""))
                else:
                    track_names.append(td.text.replace("\"", ""))

                track_duration = tr.find("td", attrs={
                    'style': 'padding-right:10px;text-align:right;vertical-align:top'
                })
                track_durations.append(track_duration.get_text())

        track_nums = list(range(1, len(track_names)+1))

        for num, track_info in zip(track_nums, zip(track_names, track_durations)):
            track_order[num] = {'track': track_info[0], 'duration': track_info[1]}
        return track_order
    except requests.ConnectionError as conerr:
        print(f"{conerr.__class__.__name__}: Cannot connect to Wikipedia.")
