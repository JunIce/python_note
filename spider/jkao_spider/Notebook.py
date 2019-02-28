#coding=utf-8
import datetime
lastid = 0
class Note:
    def __init__(self, memo, tag):
        global lastid
        lastid += 1
        self.memo = memo
        self.tag = tag
        self.create_at = datetime.date.today()
        self.id = lastid
    
    def search(self, string):
        return string in self.memo or string in self.note

class Notebooks:
    def __init__(self):
        self.notelists = []
    
    def lists(self):
        print(self.notelists)
    
    def add(self, memo, tag):
        self.notelists.append(Note(memo, tag))
        self.lists()
    
    def _get_note(self, note_id):
        for note in self.notelists:
            if note.id == note_id:
                return note
            return None
        
    def modify_memo(self, note_id, memo):
        self._get_note(note_id).memo = memo
    
    def modify_tag(self, note_id, tag):
        self._get_note(note_id).tag = tag
    

class Menu:
    def __init__(self):
        print('''
        Notebook Menu


        1. Show all notes
        2. Search Notes
        3. Add Note
        4. Modify Note

        ''')

if __name__ == '__main__':
    Menu()