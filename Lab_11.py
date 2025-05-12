def display_contacts(phonebook):
    """Displays the phonebook in a table format."""
    if not phonebook:
        print("Phonebook is empty.")
        return
    print("{:<10} {:<15} {:<15} {:<10}".format("Name", "Surname", "Phone", "City"))
    print("-" * 50)
    for contact in phonebook:
        print("{:<10} {:<15} {:<15} {:<10}".format(
            contact['name'], contact['surname'], contact['phone'], contact['city']
        ))

def search_contacts(phonebook, search_term, search_field):
    """Searches for contacts based on the given term and field."""
    results = [
        contact for contact in phonebook
        if search_term.lower() in contact[search_field].lower()
    ]
    return results

def update_contact(phonebook, name_to_update):
    """Updates the details of a contact."""
    for i, contact in enumerate(phonebook):
        if contact['name'].lower() == name_to_update.lower():
            print(f"Знайдено контакт: {contact['name']} {contact['surname']}")
            confirm = input("Бажаєте оновити цей контакт? (так/ні): ").lower()
            if confirm == 'так':
                print("Введіть нові дані:")
                phonebook[i]['name'] = input("Нове ім'я: ")
                phonebook[i]['surname'] = input("Нове прізвище: ")
                phonebook[i]['phone'] = input("Новий телефон: ")
                phonebook[i]['city'] = input("Нове місто: ")
                print("Контакт оновлено.")
                return True
            else:
                print("Оновлення скасовано.")
                return False
    print(f"Contact with name '{name_to_update}' not found.")
    return False

def delete_contact(phonebook, name_to_delete):
    """Deletes a contact from the phonebook."""
    for i, contact in enumerate(phonebook):
        if contact['name'].lower() == name_to_delete.lower():
            print(f"Знайдено контакт: {contact['name']} {contact['surname']}")
            confirm = input("Бажаєте видалити цей контакт? (так/ні): ").lower()
            if confirm == 'так':
                del phonebook[i]
                print("Контакт видалено.")
                return True
            else:
                print("Видалення скасовано.")
                return False
    print(f"Contact with name '{name_to_delete}' not found.")
    return False

def analyze_phonebook(phonebook):
    """Analyzes the phonebook to provide statistics."""
    if not phonebook:
        print("Phonebook is empty, analysis impossible.")
        return

    cities = {contact['city'] for contact in phonebook}
    print("\nUnique cities:", cities)

    city_counts = {}
    for contact in phonebook:
        city = contact['city']
        city_counts[city] = city_counts.get(city, 0) + 1

    print("\nNumber of contacts per city:")
    for city, count in city_counts.items():
        print(f"{city}: {count}")

    most_common_city = max(city_counts, key=city_counts.get) if city_counts else None
    if most_common_city:
        print(f"\nCity with the most contacts: {most_common_city} ({city_counts[most_common_city]} contacts)")
    else:
        print("\nNo cities to analyze.")

# Task 1: Create a multi-level phonebook
phonebook = [
    {"name": "Іван", "surname": "Петров", "phone": "050-123-45-67", "city": "Київ"},
    {"name": "Марія", "surname": "Сидорова", "phone": "067-987-65-43", "city": "Львів"},
    {"name": "Петро", "surname": "Іванов", "phone": "095-555-11-22", "city": "Київ"},
    {"name": "Анна", "surname": "Коваленко", "phone": "063-111-22-33", "city": "Одеса"},
    {"name": "Ігор", "surname": "Шевченко", "phone": "099-222-33-44", "city": "Київ"}
]

print("Початкова телефонна книга:")
display_contacts(phonebook)

# Task 2: Extended contact search
while True:
    print("\nПошук контактів:")
    search_by = input("Шукати за (ім'я/прізвище/місто/вихід): ").lower()
    if search_by == 'вихід':
        break
    elif search_by in ['name', 'surname', 'city']:
        search_term = input(f"Введіть значення для пошуку за '{search_by}': ")
        if search_term:
            results = search_contacts(phonebook, search_term, search_by)
            if results:
                print("\nРезультати пошуку:")
                display_contacts(results)
            else:
                print("Контакти не знайдено.")
        else:
            print("Будь ласка, введіть критерій пошуку.")
    else:
        print("Некоректний параметр пошуку. Спробуйте ще раз.")

# Task 3: Update and Analytics
while True:
    print("\nОновлення/Видалення/Аналітика:")
    action = input("Оберіть дію (оновити/видалити/аналітика/вихід): ").lower()
    if action == 'вихід':
        break
    elif action == 'оновити':
        name_to_update = input("Введіть ім'я контакту для оновлення: ")
        update_contact(phonebook, name_to_update)
        print("\nПоточна телефонна книга після оновлення:")
        display_contacts(phonebook)
    elif action == 'видалити':
        name_to_delete = input("Введіть ім'я контакту для видалення: ")
        delete_contact(phonebook, name_to_delete)
        print("\nПоточна телефонна книга після видалення:")
        display_contacts(phonebook)
    elif action == 'аналітика':
        analyze_phonebook(phonebook)
    else:
        print("Некоректна дія. Спробуйте ще раз.")
