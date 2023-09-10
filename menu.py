import datetime

from note import Note
from commandNotes import ComandsNotes
from commandView import CommandView
from commandJson import CommandJSON
from menuView import MenuView

class Menu(object):

    def new_note(self):
        note_id = 0
        date = datetime.datetime.now()
        title = input("Введите заголовок заметки: ")
        note = input("Введите заметку: ")
        return Note(note_id, date, title, note)

    def new_noteID(self):
        noteID = input('Введите id заметки: ')
        return noteID

    def start_notes(self):
        MenuView.greeting()
        commands = ComandsNotes(CommandJSON("notes.json"), CommandView)
        while True:
            command = input("1 - создать заметку \n2 - показать все заметки \n"
                            "3 - показать заметку \n4 - редактировать заметку \n"
                            "5 - удалить заметку \n6 - удалить все заметки \n"
                            "0 - закрыть приложение\nВыберите действие: ")
            if command == "0":
                break
            if command == "1":
                MenuView.decorator()
                print("Создать заметку: ")
                commands.create_note(self.new_note())
            elif command == "2":
                if commands.check_notes():
                    MenuView.decorator()
                    print("Список заметок: ")
                    MenuView.decorator()
                    commands.show_notes()
            elif command == "3":
                if commands.check_notes():
                    MenuView.decorator()
                    print("Показать заметку: ")
                    commands.show_note(int(self.new_noteID()))
            elif command == "4":
                if commands.check_notes():
                    MenuView.decorator()
                    print("Редактировать заметку: ")
                    updated_id = int(self.new_noteID())
                    if commands.check_idNote(updated_id):
                        commands.update_note(updated_id, self.new_note())
            elif command == "5":
                if commands.check_notes():
                    MenuView.decorator()
                    print("Удалить заметку: ")
                    delete_id = int(self.new_noteID())
                    if commands.check_idNote(delete_id):
                        commands.delete_note(delete_id)
            elif command == "6":
                if commands.check_notes():
                    MenuView.decorator()
                    print("Удалить ВСЕ заметки !!!??? ")
                    if input("ПОДТВЕРДИТЕ УДАЛЕНИЕ ВСЕХ ЗАМЕТОК Y: ") == "Y":
                        if commands.check_notes():
                            commands.delete_all_notes()
                    else:
                        print("УДАЛЕНИЕ НЕ ПОДТВЕРЖДЕНО")
                        MenuView.decorator()
            else:
                MenuView.mistake()
        MenuView.goodbye()