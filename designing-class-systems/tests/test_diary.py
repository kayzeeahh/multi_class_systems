from lib.diary import DiaryEntry
from lib.diary import Diary
from unittest.mock import *

def test_add_to_diary_using_mock():
    diary = Diary()
    entry = Mock()
    
    entry.return_value = "entry 1"
    
    diary.add(entry)
    assert diary.diary == [entry]



def test_for_reading_now():
    diary = Diary()
    diary_ent1 = DiaryEntry('My title', '1 2 3 4 5 6 7 8 9')
    diary_ent2 = DiaryEntry('Yet another title', '1 2 3 4') 
    diary.add(diary_ent1)
    diary.add(diary_ent2)
    assert diary.reading_now(4,2) == diary_ent2.format_entry()






def test_for_diary_entry():
    diary_entry = DiaryEntry("title", "content")
    assert [diary_entry.title, diary_entry.content] == ["title", "content"]
    
def test_for_content_length():
    diary_entry = DiaryEntry("title", "content")
    assert diary_entry.content_length() == 1