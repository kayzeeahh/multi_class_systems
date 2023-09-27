import pytest
from lib.diary import *
"""
When given an no entries
returns an empty list
"""
def test_no_diary_entries():
    diary = Diary()
    result = diary.all()
    assert result == []
    
"""
Initially, word count is zero
"""
def test_initially_word_count_zero():
    diary = Diary()
    assert diary.count_words() == 0
    
"""
Initially, reading_time should raise an error
"""
def test_reading_time_error():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.reading_time(2)
    assert str(err.value) == "No entries added yet"