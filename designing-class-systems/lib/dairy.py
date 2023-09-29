'''
We want a dairy that takes dairy entries
'''
class Diary():
    def __init__(self):
        self.diary = []

    def add(self, entry):
        self.diary.append(entry)

    def read(self):
        return self.diary 
        
    def reading_now(self,wpm,minutes):
        words = wpm * minutes
        readable_entry = []
        for diary_entry in self.diary:
            if words >= diary_entry.content_length():
                readable_entry.append(diary_entry)
        return readable_entry 

class DiaryEntry():
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def content_length(self):
        return len(self.content)

