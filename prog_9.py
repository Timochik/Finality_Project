def add_tag(self, name, note, tag):
    if name in self.names:
        if note in self.notes:
            self.notes[note]['tags'].append(tag)
            print(f"До нотатки {note} був доданий тег: {tag}")
        else:
            print(f"Нотатка {note} не знайдена")
    else:
        print(f"Контакт {name} не знайдений.")