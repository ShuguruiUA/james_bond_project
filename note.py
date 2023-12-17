from collections import UserDict

class Note:
    def __init__(self, name, note):
        self.name = name
        self.note = note
        self.teg = []

    def add_teg(self, teg):
        self.teg.append(teg)

    def change_note(self, new_text):
        self.note = new_text

    def del_teg(self, teg):
        if teg in self.teg:
            self.teg.remove(teg)
            return 'mission complete'
        return 'teg is not found'
    
    def __str__(self):
        return f"Note name: {self.name}, tegs: {'; '.join(p for p in self.teg)}, note: {self.note}"
    
class Notebook(UserDict):
    def add_note(self, note):
        if isinstance(note, Note):
            self.data[note.name] = note

    def find_note(self, name):
        for note in self.data.values():
            if name in note.name:
                return note
    
    def find_note_teg(self, teg):
        res = None
        res = []
        for note in self.data.values():
            if teg in note.teg:
                res.append(note)
        return res

