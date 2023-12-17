elif parts[0] == "search-note":
    # Команда для пошуку нотаток за текстовим запитом
    name = parts[1]
    query = " ".join(parts[2:])
    record = book.find(name)
    if record:
        matching_notes = [note for note in record.notes if query.lower() in note.text.lower()]
        if matching_notes:
            print(f"Результати пошуку нотаток для {name} за запитом '{query}':")
            for note in matching_notes:
                print(f"- {note.text}")
        else:
            print(f"Нотатки для {name} за запитом '{query}' не знайдено.")
    else:
        print(f"No such name found in the address book. Please add the name first.")

elif parts[0] == "edit-note":
    # Команда для редагування нотатки
    name = parts[1]
    index = int(parts[2]) - 1  # Індекс нотатки для редагування (з 1 до N)
    new_text = " ".join(parts[3:])
    record = book.find(name)
    if record and 0 <= index < len(record.notes):
        record.notes[index].value = new_text
        print(f"Нотатка #{index + 1} для {name} була успішно відредагована.")
    else:
        print(f"Invalid index or no such name found in the address book.")

elif parts[0] == "delete-note":
    # Команда для видалення нотатки
    name = parts[1]
    index = int(parts[2]) - 1  # Індекс нотатки для видалення (з 1 до N)
    record = book.find(name)
    if record and 0 <= index < len(record.notes):
        deleted_note = record.notes.pop(index)
        print(f"Нотатка #{index + 1} для {name} була успішно видалена.")
        print(f"Видалена нотатка: {deleted_note.value}")
    else:
        print(f"Invalid index or no such name found in the address book.")