'''
We want a journal_book which holds our
phonebook, task_tracker and diary
'''
class JournalBook():
    def __init__(self, diary, phonebook, task_tracker):
        self.diary = diary
        self.phonebook = phonebook
        self.task_tracker = task_tracker

    
