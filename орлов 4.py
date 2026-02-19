import tkinter as tk

# Функция-обработчик события submit
def submit_action():
    username = entry_username.get()
    password = entry_password.get()
    if username and password:
        label_result.config(text="Выполнен вход")  # Отображаем надпись
    else:
        label_result.config(text="Заполните поля")

# Функция-обработчик события clear
def clear_action():
    entry_username.delete(0, tk.END)  # Очищаем поле username
    entry_password.delete(0, tk.END)  # Очищаем поле password
    label_result.config(text="")       # Очищаем результат

# Функция-обработчик события close
def close_app():
    root.destroy()                     # Закрываем приложение

# Главное окно приложения
root = tk.Tk()
root.title("Авторизация")
root.geometry("400x350")



# Рамка для центрального размещения элементов
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")  # Центрируем рамку

# Поля ввода
label_username = tk.Label(frame, text="Username:", font=("Arial", 12))
entry_username = tk.Entry(frame, font=("Arial", 12))

label_password = tk.Label(frame, text="Password:", font=("Arial", 12))
entry_password = tk.Entry(frame, show="*", font=("Arial", 12))  # Скрываем пароль звездочками

# Кнопки
submit_btn = tk.Button(frame, text="Submit", command=submit_action, font=("Arial", 12))
clear_btn = tk.Button(frame, text="Clear", command=clear_action, font=("Arial", 12))
close_btn = tk.Button(frame, text="Close", command=close_app, font=("Arial", 12))

# Надпись для вывода результата
label_result = tk.Label(frame, fg="green", font=("Arial", 12))

# Расположим компоненты вертикально друг над другом
label_username.pack(pady=(10, 0))
entry_username.pack(pady=(5, 0))

label_password.pack(pady=(10, 0))
entry_password.pack(pady=(5, 0))

submit_btn.pack(pady=(10, 0))
clear_btn.pack(pady=(5, 0))
close_btn.pack(pady=(5, 0))

label_result.pack(pady=(10, 0))

# Запускаем главный цикл приложения
root.mainloop()