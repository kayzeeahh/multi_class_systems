from lib.track import *

def test_matches_on_full_title():
    track = Track("Cat Title", "Dog Artist")
    assert track.matches("Cat Title") == True
    

def test_matches_on_partial_title():
    track = Track("Cat Title", "Dog Artist")
    assert track.matches("Cat") == True
    
def test_matches_on_full_artist():
    track = Track("Cat Title", "Dog Artist")
    assert track.matches("Dog Artist") == True
    
def test_matches_on_partial_artist():
    track = Track("Cat Title", "Dog Artist")
    assert track.matches("Dog") == True
    
def test_does_not_match_artist_or_title():
    track = Track("Cat Title", "Dog Artist")
    assert track.matches("Frog") == False