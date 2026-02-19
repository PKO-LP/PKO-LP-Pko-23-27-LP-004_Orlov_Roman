import tkinter as tk

# Основная функция проверки наличия цифр от 0 до 9
def check_numbers():
    input_text = entry.get()  # Получаем введённый текст
    numbers = set(str(i) for i in range(10))  # Множество цифр от 0 до 9
    count = sum(1 for char in input_text.split(',') if char.strip() in numbers)
    result_label.config(text=f"Ваш ввод содержит {count} чисел от 0 до 9.")

# Интерфейс приложения
root = tk.Tk()
root.title("Проверка наличия чисел")
root.geometry("350x150")

# Виджет для ввода данных
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Кнопка для запуска проверки
check_button = tk.Button(root, text="Проверить", command=check_numbers)
check_button.pack(pady=5)

# Виджет для отображения результата
result_label = tk.Label(root, text="", fg="blue")
result_label.pack(pady=10)

# Основной цикл приложения
root.mainloop()