from lib.music_library import *
from lib.track import *
import pytest

def test_adds_and_lists_multiple_tracks():
    library = MusicLibrary()
    track_1 = Track("My title 1", "My artist 1")
    track_2 = Track("My title 2", "My artist 2")
    library.add(track_1)
    library.add(track_2)
    assert library.track_list == [track_1, track_2]
    
def test_searches_for_tracks_by_full_title():
    library = MusicLibrary()
    track_1 = Track("Dog", "Cat")
    track_2 = Track("Frog", "Toad")
    library.add(track_1)
    library.add(track_2)
    assert library.search("Dog") == [track_1]
