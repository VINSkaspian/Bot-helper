from models.note import Note

class NoteBook:
    def __init__(self):
        self.notes = []

    def add_note(self, text, tags=None):
        note = Note(text, tags)
        self.notes.append(note)

    def find_note(self, keyword):
        return [n for n in self.notes if keyword.lower() in n.text.lower()]

    def delete_note(self, text):
        self.notes = [n for n in self.notes if text.lower() not in n.text.lower()]

    def edit_note(self, old_text, new_text):
        for note in self.notes:
            if old_text.lower() in note.text.lower():
                note.text = new_text

    def find_by_tag(self, tag):
        return [n for n in self.notes if tag in n.tags]
