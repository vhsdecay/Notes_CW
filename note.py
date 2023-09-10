class Note(object):

    def __init__(self, note_id, date, title, note):
        self.note_id = note_id
        self.date = date
        self.title = title
        self.note = note

    @property
    def note_id(self):
        return self._note_id

    @note_id.setter
    def note_id(self, note_id):
        self._note_id = note_id

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def text(self):
        return self._note

    @text.setter
    def text(self, note):
        self._note = note

    def __str__(self):
        return f'ID заметки: {self.note_id}\nДата создания(редактирования):' \
               f' {self.date}\nЗаголовок: {self.title}\nЗаметка: {self.note}'