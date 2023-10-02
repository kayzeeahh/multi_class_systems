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
        
        return '/n/n'.join([entry.format_entry() for entry in self.diary])#self.diary 
        
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
        return len(self.content.split())
    
    def format_entry(self):
        return f'{self.title}: {self.content}'
    
diary_ent1 = DiaryEntry('My title', 'This is my title my really lovely title')
diary_ent2 = DiaryEntry('Yet another title.', 'This one is for you.') 

secret_diary = Diary()

Diary.add(diary_ent1)
Diary.add(diary_ent2)

print(secret_diary.read())