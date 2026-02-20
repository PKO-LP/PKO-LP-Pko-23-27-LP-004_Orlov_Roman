import tkinter as tk


# Функция для сохранения данных в файл
def save_data():
    first_name = entry_firstname.get()
    last_name = entry_lastname.get()
    class_number = entry_class.get()
    group_number = entry_group.get()

    # Формируем строку для записи в файл
    data_string = f"{first_name}, {last_name}, Класс: {class_number}, Группа: {group_number}"

    try:
        with open("orlov.txt", "a") as file:
            file.write(f"{data_string}\n")
        print("Данные успешно сохранены!")
    except Exception as e:
        print(f"Ошибка: {e}")


# Основное окно приложения
root = tk.Tk()
root.title("Регистрация студента")

# Входные поля
label_firstname = tk.Label(root, text="Имя:")
label_firstname.grid(row=0, column=0, padx=10, pady=5)
entry_firstname = tk.Entry(root)
entry_firstname.grid(row=0, column=1, padx=10, pady=5)

label_lastname = tk.Label(root, text="Фамилия:")
label_lastname.grid(row=1, column=0, padx=10, pady=5)
entry_lastname = tk.Entry(root)
entry_lastname.grid(row=1, column=1, padx=10, pady=5)

label_class = tk.Label(root, text="Класс:")
label_class.grid(row=2, column=0, padx=10, pady=5)
entry_class = tk.Entry(root)
entry_class.grid(row=2, column=1, padx=10, pady=5)

label_group = tk.Label(root, text="Группа:")
label_group.grid(row=3, column=0, padx=10, pady=5)
entry_group = tk.Entry(root)
entry_group.grid(row=3, column=1, padx=10, pady=5)

# Кнопка для сохранения данных
btn_save = tk.Button(root, text="Сохранить", command=save_data)
btn_save.grid(row=4, columnspan=2, pady=15)

# Главный цикл приложения
root.mainloop()