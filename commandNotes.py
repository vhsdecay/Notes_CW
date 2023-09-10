class ComandsNotes(object):

    def __init__(self, json, view):
        self.json = json
        self.view = view

    def show_notes(self):
        notes = self.json.read_notes()
        self.view.show_notes_list(notes)

    def show_note(self, read_id):
        note = self.json.read_note(read_id)
        if note != None:
            self.view.show_note(note)
        else: self.view.show_note_null(read_id)


    def create_note(self, note):
        self.json.create_note(note)
        self.view.show_note_add()

    def update_note(self, update_id, note):
        self.json.update_note(update_id, note)
        self.view.show_note_update(update_id)

    def delete_note(self, delete_id):
        try:
            self.json.delete_note(delete_id)
            self.view.show_note_delete(delete_id)
        except ValueError:
            self.view.show_note_null(delete_id)

    def delete_all_notes(self):
        self.json.delete_all_notes()
        self.view.show_all_note_delete()

    def check_notes(self):
        notes = self.json.read_notes()
        if len(notes) == 0:
            self.view.show_notes_null()
            return False
        else:
            return True

    def check_idNote(self, check_id):
        notes = self.json.read_notes()
        for note in notes:
            if note.note_id == check_id:
                return True
        else:
            self.view.show_note_null(check_id)
            return False