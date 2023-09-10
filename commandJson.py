import json

from note import Note
from commandView import CommandView

class CommandJSON(object):
    def __init__(self, fileNotes):
        self.fileNotes = fileNotes
        self.notes = list()
    def read_notes(self):
        return self.read_fileNotes()

    def read_note(self, read_id):
        self.notes = self.read_notes()
        for note in self.notes:
            if note.note_id == read_id:
                return note

    def create_note(self, note):
        self.notes = self.read_notes()
        max_id = 0
        for item in self.notes:
            if item.note_id > max_id:
                max_id = item.note_id
        note_id = max_id + 1
        note.note_id = note_id

        self.notes.append(note)
        self.write_fileNotes(self.notes)
    def update_note(self, update_id, note):
        self.notes = self.read_notes()
        for item in self.notes:
            if item.note_id == update_id:
                item.date = note.date
                item.title = note.title
                item.note = note.note
        self.write_fileNotes(self.notes)
    def delete_note(self, delete_id):
        self.notes = self.read_notes()
        for index, note in enumerate(self.notes):
            if note.note_id == delete_id:
                del self.notes[index]
        self.write_fileNotes(self.notes)
    def delete_all_notes(self):
        self.notes = self.read_notes()
        self.notes.clear()
        self.write_fileNotes(self.notes)
    def read_fileNotes(self):
        notes_list = list()
        try:
            with open(self.fileNotes, "r", encoding='utf-8') as my_file:
                notes_json = my_file.read()
            data = json.loads(notes_json)
            data.sort(key=lambda x: x['date'])
            for item in data:
                notes_list.append(Note(item['id'], item['date'], item['title'], item['text']))
            return notes_list
        except ValueError:
            return self.notes
    def write_fileNotes(self, notes):
        notes_list = list()
        for note in notes:
            notes_list.append({'id': note.note_id, 'date': note.date, 'title': note.title, 'text': note.note})

        notes_json = json.dumps(notes_list, indent=4, ensure_ascii=False, sort_keys=False, default=str)

        with open(self.fileNotes, "w", encoding='utf-8') as my_file:
            my_file.write(notes_json)
