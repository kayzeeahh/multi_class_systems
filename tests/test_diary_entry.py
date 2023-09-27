from lib.diary_entry import *

"""
When I add a title and contents 
I can get that title and contents back
"""
def test_getting_content_and_title():
    diary_entry = DiaryEntry("My Title", "My Contents")
    assert diary_entry.title == "My Title"
    assert diary_entry.contents == "My Contents"
    
"""
When I initialise with five-word contents
Then count_words should return five
"""
def test_count_words_rturns_word_count_of_contents():
    diary_entry = DiaryEntry("My Title", "one two three four five")
    assert diary_entry.count_words() == 5
    
"""
When I initialise with five-word contents
Then count_words should return five
"""