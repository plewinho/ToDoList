choice = -1
tasks = []

def show_tasks():
    task_index = 0
    for task in tasks:
        print(task + "[" + str(task_index) + "]")
        task_index += 1

def add_task():
    task = input("Wpisz tresc zadania: ")
    tasks.append(task)
    print("Dodano zadanie! ")

def delete_task():
    task_index = int(input("Podaj numer zadania do usuniecia: "))
    if task_index < 0 or task_index > len(tasks) - 1:
        print("Nie ma takiego zadania!")
        return
    tasks.pop(task_index)
    print("Usunieto zadanie!")

def save_tasks_to_file():
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()

def load_tasks_from_file():
    try:
        file=open("tasks.txt")
        for line in file.readlines():
            tasks.append(line.strip())
        file.close()
    except FileNotFoundError:
        return

    
load_tasks_from_file()
    
while choice != 5:
    
    if choice == 1:
        show_tasks()
   
    if choice == 2:
       add_task()

    if choice == 3:
        delete_task()

    if choice == 4:
        save_tasks_to_file()



    print()
    print("1. Pokaz zadanie")
    print("2. Dodaj zadanie")
    print("3. Usun zadanie")
    print("4. Zapisz zmiany w pliku")
    print("5. Zamknij program!")

    choice = int(input("Wybierz liczbe: "))
    print()