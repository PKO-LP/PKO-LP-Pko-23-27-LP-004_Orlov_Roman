import tkinter as tk
from tkinter import messagebox

# Создаем основное окно
root = tk.Tk()
root.title("Форма авторизации")
root.geometry("300x150")

# Элементы интерфейса
label_username = tk.Label(root, text="Имя пользователя:")
label_password = tk.Label(root, text="Пароль:")

entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")  # Скрытие пароля звездочками


# Функциональность кнопки входа
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "1111" and password == "1111":
        messagebox.showinfo("Авторизация успешна", f"Привет, {username}!")
    else:
        messagebox.showerror("Ошибка авторизации", "Неверное имя пользователя или пароль.")


# Кнопка входа
button_login = tk.Button(root, text="Войти", command=login)

# Расположение элементов
label_username.grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_username.grid(row=0, column=1, padx=10, pady=5)

label_password.grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_password.grid(row=1, column=1, padx=10, pady=5)

button_login.grid(row=2, columnspan=2, pady=10)

# Запуск приложения
if __name__ == "__main__":
    root.mainloop()