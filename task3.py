import tkinter as tk


def check_time():
    time_str = entry.get()

    try:
        # Проверяем правильность формата времени
        hours, minutes = map(int, time_str.split(':'))

        if not (0 <= hours < 24 and 0 <= minutes < 60):
            raise ValueError("Неверное время")

        # Определяем период суток
        if 6 <= hours < 12:
            label.config(text="Утро")
        elif 12 <= hours < 18:
            label.config(text="День")
        elif 18 <= hours < 24 or hours == 0:
            label.config(text="Вечер")
        else:
            label.config(text="Ночь")

    except Exception as e:
        label.config(text=str(e))


# Создаем главное окно приложения
root = tk.Tk()
root.title('Определение периода суток')

# Поле для ввода времени
entry = tk.Entry(root)
entry.pack(pady=10)

# Кнопка проверки введенного времени
button = tk.Button(root, text='Проверить', command=check_time)
button.pack(pady=5)

# Метка для вывода результата
label = tk.Label(root, font=('Arial', 14), fg='red')
label.pack(pady=10)

# Запускаем основное событие Tkinter
root.mainloop()