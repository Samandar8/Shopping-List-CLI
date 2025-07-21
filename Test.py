d = {}
def adder():
    item = input("Введите товар: ")
    price = int(input("Введите цену: "))
    d.update({item: price})
    print("Добавлено!")



def remover():

    if not d:
        print("Вы ещё ничего не добавляли! С начало добавте продукты!")
    else:
        b = input("Введите название товара, который хотите удалить: ")
        if b in d:
            del d[b]
            print("Удалено!")
        else:
            print("Такого продукта нет!")




def saver():
    with open("shopping.txt", "w", encoding="utf-8") as file:
        file.write(str(d))
        print("Покупки были сохранены в файле shopping.txt")


while True:
    print("Команды: add, remove, list, total, save, exit")
    a = input(">>> ")
    if a == "add":
        adder()

    elif a == "remove":
        remover()

    elif a == "list":
        if d:
            for i, (k, v) in enumerate(d.items(), 1):
                print(f"{i}. {k} — {v} сум")
        else:
            print("Список пуст.")

    elif a == "total":
        print(f"Сумма: {sum(d.values())}")

    elif a == "save":
        saver()

    elif a == "exit":
        break

    else:
        print("Напишите только команды! (add, remove, list, total, save, exit)")













