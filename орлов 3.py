import tkinter as tk
from tkinter import messagebox
import csv
import os.path



# Функция для расчёта хэша (сумма кодов символов)
def calculate_hash(password):
    return sum(map(ord, password))


# Обработчик кнопки Hash
def on_hash_button():
    global password_entry, hash_value_label
    password = password_entry.get()
    if not password.strip():  # Проверяем наличие хотя бы одного символа
        messagebox.showwarning("Ошибка", "Пароль пуст!")
        return

    # Вычисляем хэш
    hashed_password = calculate_hash(password)
    hash_value_label.config(text=f'Хэш: {hashed_password}')


# Обработчик кнопки Сохранить
def save_to_csv():
    global password_entry, filename
    password = password_entry.get().strip()  # Получаем введённый пароль
    hashed_password = int(hash_value_label.cget('text').split(':')[1].strip())  # Берём значение хэша

    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([password, hashed_password])

    messagebox.showinfo("Успех", f"Пара \"{password}\" и её хэш успешно сохранены.")


# Обработчик кнопки Очистить
def clear_data():
    global filename
    if os.path.exists(filename):  # Если файл существует
        os.remove(filename)  # Удаляем файл
        messagebox.showinfo("Очищено", "Файл очищен")
    else:
        messagebox.showinfo("Информация", "Нет данных для очистки.")


# Настройка окна приложения
root = tk.Tk()
root.title("Простое хэширование пароля")
root.geometry("400x400")

# Виджет для ввода пароля
password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=10)

# Кнопка для вычисления хэша
hash_button = tk.Button(root, text="Hash", command=on_hash_button)
hash_button.pack(pady=5)

# Метка отображающая полученный хэш
hash_value_label = tk.Label(root, text='Хэш:')
hash_value_label.pack(pady=5)

# Кнопка для сохранения результата
save_button = tk.Button(root, text="Сохранить", command=save_to_csv)
save_button.pack(pady=5)

# Кнопка для удаления содержимого файла
clear_button = tk.Button(root, text="Очистить", command=clear_data)
clear_button.pack(pady=5)

filename = "пароль.csv.py"

root.mainloop()