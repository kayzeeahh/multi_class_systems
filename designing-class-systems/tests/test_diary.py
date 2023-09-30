from lib.diary import DiaryEntry
from lib.diary import Diary
from unittest.mock import *

def test_add_to_diary():
    diary = Diary()
    entry = Mock()
    
    entry.return_value = "entry 1"
    
    diary.add(entry)
    assert diary.diary == [entry]









def test_for_diary_entry():
    diary_entry = DiaryEntry("title", "content")
    assert [diary_entry.title, diary_entry.content] == ["title", "content"]
    
def test_for_content_length():
    diary_entry = DiaryEntry("title", "content")
    assert diary_entry.content_length() == 1