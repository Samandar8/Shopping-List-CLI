def file_saver(tasks):
    with open('tasks.txt', 'w', encoding='utf-8') as file:
        for task in tasks:
            file.write(task + "\n")
    print("Задачи сохранены!")



tasks = []
try:
    with open("tasks.txt", encoding='utf-8') as file:
        tasks = [line.strip() for line in file.readlines()]
    print("Задачи загружены!")
except FileNotFoundError:
    print("Файл задач не найден. Начинаем с пустого списка.")

while True:
    print("Команды: add, list, done, delete, save, exit")
    cmd = input(">>> ").strip().lower()

    if cmd == "exit":
        print("Пока!")
        break

    elif cmd == "add":
        text = input("Введите задачу: ").strip()
        if text:
            tasks.append("✘ " + text)
            print("Задача добавлена!")
        else:
            print("Задание не может быть пустым!")

    elif cmd == "list":
        if tasks:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
        else:
            print("Список задач пуст!")

    elif cmd == "done":
        if not tasks:
            print("Сначала добавьте задания!")
        else:
            try:
                n = int(input("Введите номер задачи: "))
                if 1 <= n <= len(tasks):
                    if tasks[n-1].startswith("✘ "):
                        tasks[n-1] = tasks[n-1].replace("✘ ", "✔ ")
                        print("Задача помечена как выполненная!")
                    else:
                        print("Задача уже выполнена!")
                else:
                    print("Нет такой задачи!")
            except ValueError:
                print("Введите число!")

    elif cmd == "delete":
        if not tasks:
            print("Список пуст!")
        else:
            try:
                n = int(input("Введите номер задачи: "))
                if 1 <= n <= len(tasks):
                    deleted = tasks.pop(n-1)
                    print(f"Удалена задача: {deleted}")
                else:
                    print("Нет такой задачи!")
            except ValueError:
                print("Введите число!")

    elif cmd == "save":
        file_saver(tasks)

    else:
        print("Неизвестная команда.")



