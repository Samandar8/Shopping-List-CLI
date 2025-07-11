def file_saver(tasks):
    with open('tasks.txt', 'w', encoding='utf-8') as file:
        for task in tasks:
            file.write(task + "\n")
    print("Задачи сохранены!")

def add_task(tasks):
    text = input("Введите задачу: ").strip()
    if text:
        tasks.append("✘ " + text)
        print("Задача добавлена!")
    else:
        print("Задание не может быть пустым!")
        print()
    return tasks

def list_task(tasks):
    if tasks:
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")
    else:
        print("Список задач пуст!")
        print()


def doner_task(tasks):
    if not tasks:
        print("Сначала добавьте задания!")
        print()
    else:
        try:
            n = int(input("Введите номер задачи: "))
            if 1 <= n <= len(tasks):
                if tasks[n - 1].startswith("✘ "):
                    tasks[n - 1] = tasks[n - 1].replace("✘ ", "✔ ")
                    print("Задача помечена как выполненная!")
                else:
                    print("Задача уже выполнена!")
            else:
                print("Нет такой задачи!")
        except ValueError:
            print("Введите число!")
    return tasks


def delete_task(tasks):
    if not tasks:
        print("Список пуст!")
        print()
    else:
        try:
            n = int(input("Введите номер задачи: "))
            if 1 <= n <= len(tasks):
                deleted = tasks.pop(n - 1)
                print(f"Удалена задача: {deleted}")
            else:
                print("Нет такой задачи!")
        except ValueError:
            print("Введите число!")
    return tasks

tasks = []
try:
    with open("tasks.txt", encoding='utf-8') as file:
        tasks = [line.strip() for line in file.readlines()]
    print("Задачи загружены!")
except FileNotFoundError:
    print("Файл задач не найден. Начинаем с пустого списка.")

while True:
    print("Команды: add, list, done, delete, save, exit, help")
    cmd = input(">>> ").strip().lower()

    if cmd == "exit":
        if len(tasks) > 0:
            file_saver(tasks)
        print("Пока!")
        break

    elif cmd == "add":
        tasks = add_task(tasks)

    elif cmd == "list":
        list_task(tasks)

    elif cmd == "done":
        tasks = doner_task(tasks)

    elif cmd == "delete":
        tasks = delete_task(tasks)

    elif cmd == "save":
        file_saver(tasks)

    elif cmd == "help":
        print("""
Добро пожаловать в To-Do менеджер!
Команды:
add     - Добавить задачу
list    - Показать все задачи
done    - Отметить задачу выполненной
delete  - Удалить задачу
save    - Сохранить задачи в файл
exit    - Выход
""")
        print()
    else:
        print("Неизвестная команда.")





