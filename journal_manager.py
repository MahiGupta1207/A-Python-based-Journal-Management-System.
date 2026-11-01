from datetime import datetime
File='journal.txt' 
def add_entry():
    title=input('Enter journal title: ')
    mood=input('How is your mood today? ')
    location=input('Where are you now? ')
    tags=input('Enter tags: ')
    text=input('Write your journal: ')
    current_time=datetime.now()
    date=current_time.strftime('%d-%m-%Y %H:%M')
    with open(File,'a') as file:
        file.write(f'{date}->{title}->{mood}->{location}->{tags}->{text}\n')
    print('Entry added succesfully!!')
def view_entries():
    try:
        with open(File,'r') as file:
            entries=file.readlines()
        if not entries:
            print('No journal entries found!!')
            return
        print('======================================== MY JOURNAL =========================================\n')
        for number,entry in enumerate(entries,1):
            date,title,mood,location,tags,text=entry.strip().split('->')
            print(f'\nEntry {number}')
            print('Date:      ',date)
            print('Title:     ',title)
            print('Mood:      ',mood)
            print('Location:  ',location)
            print('Tags:      ',tags)
            print('Entry:     ',text)
    except FileNotFoundError:
        print('No journal entries found')
def search_entry():
    keyword=input('Enter keyword you want to search: ').lower()
    try:
        with open(File,'r') as file:
            found=False
            for entry in file:
                if keyword in entry.lower():
                    print('\n'+entry.strip())
                    found=True
            if not found:
                print('No journal entries found!!')
    except FileNotFoundError:
        print('No journal entries found')
def edit_entry():
    try:
        with open(File,'r') as file:
            entries=file.readlines()
        number=int(input('Enter entry number you want to edit: '))
        if number<1 or number>len(entries):
            print('Invalid number entry!!')
            return
        title=input('Enter new title: ')
        mood=input('Enter new mood: ')
        location=input('Enter new location: ')
        tags=input('Enter new tags: ')
        text=input('Enter new journal text: ')
        current_time=datetime.now()
        date=current_time.strftime('%d-%m-%Y %H:%M')
        entries[number-1]=(f'{date}->{title}->{mood}->{location}->{tags}->{text}\n')   
        with open(File,'w') as file:
            file.writelines(entries)
        print('Entry updated successfully!!')
    except FileNotFoundError:
        print('No journal entries found')
def delete_entry():
    try:
        with open(File,'r') as file:
            entries=file.readlines()
        number=int(input('Enter the entry number which you want to delete: '))
        if number<1 or number>len(entries):
                    print('Invalid number entry!!')
                    return
        entries.pop(number-1)
        with open(File,'w') as file:
            file.writelines(entries)
        print('Entry deleted successfully!!')
    except FileNotFoundError:
            print('No journal entries found')
while True:
    print('======================================== MY JOURNAL =========================================')
    print('1. Add Entry')
    print('2. View Enteries')
    print('3. Search Entry')
    print('4. Edit Entry')
    print('5. Delete Entry')
    print('6. Exit')
    choice=input('Enter your choice: ')
    if choice=='1':
        add_entry()
    elif choice=='2':
        view_entries()
    elif choice=='3':
        search_entry()
    elif choice=='4':
        edit_entry()
    elif choice=='5':
        delete_entry()
    elif choice=='6':
        print('Thank you for using Journal Manager!!')
        break
    else:
        print('Please enter a valid choice!!')