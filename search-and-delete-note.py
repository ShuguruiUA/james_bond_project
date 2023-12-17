from collections import UserDict

class Notebook(UserDict):
   
    def search(self, query: str):
        results = []
        for note in self.data.values():
            if query.lower() in note.note_body.lower():
                results.append(note)
        return results
    
    def delete(self, title):
        self.pop(title, None)
        