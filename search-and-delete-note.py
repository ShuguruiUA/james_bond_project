from collections import UserDict

class Notebook(UserDict):
   
    def search(self, query):
       results = []
       for note in self.data.values():
          if (
            query.lower() in note.title.lower()
            or any(query in teg.lower() for teg in note.tegs)
            or query.lower() in note.note_body.lower()
            ):
                results.append(note)
       return results
    
    def delete(self, title):
        self.pop(title, None)