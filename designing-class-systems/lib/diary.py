'''
We want a dairy that takes dairy entries
'''
class Diary():
    def __init__(self):
        self.diary = []

    def add(self, entry):
        self.diary.append(entry)

    def read(self):
        'We want to take the title and content from withing the entry'
        'We want to format it in the form of Title: Content'
        
        return '\n\n'.join([entry.format_entry() for entry in self.diary])
        
    def reading_now(self,wpm,minutes):
        words = wpm * minutes
        return '\n\n'.join([entry.format_entry() for entry in self.diary if words >= entry.content_length()])

class DiaryEntry():
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def content_length(self):
        return len(self.content.split())
    
    def format_entry(self):
        return f'{self.title}: {self.content}'