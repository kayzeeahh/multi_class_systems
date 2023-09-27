from lib.diary import *
from lib.diary_entry import *

"""Given 2 entries
it returns the 2 in a list"""
def test_2_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "My Contents 1")
    entry_2 = DiaryEntry("My Title 2", "My Contents 2")
    diary.add(entry_1)
    diary.add(entry_2)
    result = diary.all()
    assert result == [entry_1, entry_2]
    
"""
Given I add 2 diary entries
I can count_words
it returns the total words in the contents
"""
def test_count_words_returns_total_of_all():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "One two")
    entry_2 = DiaryEntry("My Title 2", "Three four five")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 5
    
"""
Given I add two diary entries with a total length of 5
and I call reading_time with a wpm of 2
it returns the total reading time as 2.5
"""
def test_reading_time_returns_time_to_read_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "One two")
    entry_2 = DiaryEntry("My Title 2", "Three four five")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(2) == 3
    

"""Given no diary entries
find_best_entry returns None
"""
def test_find_best_entries_returns_none_for_empty_list():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "One two three four five six seven")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2,3) == None
"""
Given I add two diary entries, one long and one short
and I call find_best_entry
it returns the shorter one
"""
#def test_find_best_entry_for_reading_time():
    #diary = Diary()
    #entry_1 = DiaryEntry("My Title 1", "One two three")
    #entry_2 = DiaryEntry("My Title 2", "Three four five six seven")
    #diary.add(entry_1)
    #diary.add(entry_2)
    #assert diary.find_best_entry_for_reading_time(2, 3) == entry_1
    
"""
Given I add two diary entries, one long and one short
and I call find_best_entry and I can read both
it returns the longer one
"""
def test_find_best_test_for_long_reading_entry():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "One two three")
    entry_2 = DiaryEntry("My Title 2", "Three four five six seven")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 4) == entry_2