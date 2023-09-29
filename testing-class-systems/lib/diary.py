from math import ceil 
class Diary:
    def __init__(self):
        self._entries = []

    def add(self, entry):
        self._entries.append(entry)

    def all(self):
        return self._entries

    def count_words(self):
        word_counts = [entry.count_words() for entry in self._entries]
        return sum(word_counts)
        

    def reading_time(self, wpm):
        if self._entries == []:
            raise Exception("No entries added yet")
        word_count = self.count_words()
        return ceil(word_count / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        words_use_could_ready = wpm * minutes
        most_readable = None
        longest_readable = 0
        for entry in self._entries:
            if entry.count_words() <= words_use_could_ready:
                if entry.count_words() > longest_readable:
                    most_readable = entry
                    longest_readable = entry.count_words()
        return most_readable