import tkinter as tk


# Функция для расчета и вывода результата
def calculate():
    try:
        # Числа, введенные пользователем
        a = float(a_entry.get())
        b = float(b_entry.get())

        # Расчет квадратов суммы и разности
        square_sum = round((a + b) ** 2, 2)
        square_diff = round((a - b) ** 2, 2)

        # Форматируем строки для красивого представления результата
        formula_sum = f'({a:.2f} + {b:.2f})² = {square_sum}'
        formula_diff = f'({a:.2f} - {b:.2f})² = {square_diff}'

        # Обновляем надпись с результатом
        result_label.config(text=f'{formula_sum}\n{formula_diff}')
    except Exception as e:
        result_label.config(text="Ошибка: проверьте введённые значения.")


# Сохраняем результат в файл
def save_result():
    content = result_label['text']
    if content.strip() != '' and not content.startswith('Ошибка'):
        with open('kvadrat.txt', 'w', encoding='utf-8') as file:
            file.write(content)
        print("Результат сохранён в kvadrat.txt")
    else:
        print("Нечего сохранять или произошла ошибка.")


# Очищаем файл
def clear_file():
    with open('kvadrat.txt', 'w', encoding='utf-8') as file:
        file.truncate()
    print("Файл очищен.")


# Создание главного окна приложения
window = tk.Tk()
window.title("Калькулятор квадратов суммы и разности")

# Заголовок окна
title_label = tk.Label(window, text="Введите значения a и b:", font=("Arial", 12))
title_label.pack(pady=(10, 5))

# Поля ввода
frame_input = tk.Frame(window)
frame_input.pack(padx=10, pady=5)

tk.Label(frame_input, text="A:").grid(row=0, column=0)
a_entry = tk.Entry(frame_input)
a_entry.grid(row=0, column=1)

tk.Label(frame_input, text="B:").grid(row=1, column=0)
b_entry = tk.Entry(frame_input)
b_entry.grid(row=1, column=1)

# Кнопка расчета
calc_btn = tk.Button(window, text="Рассчитать", command=calculate)
calc_btn.pack(pady=10)

# Надпись для отображения результата
result_label = tk.Label(window, text='', font=("Arial", 12), fg="green")
result_label.pack(pady=10)

# Фрейм для кнопок сохранения и очистки
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# Кнопка сохранения
save_btn = tk.Button(button_frame, text="Сохранить", command=save_result)
save_btn.pack(side=tk.LEFT, padx=5)

# Кнопка очистки файла
clear_btn = tk.Button(button_frame, text="Очистить", command=clear_file)
clear_btn.pack(side=tk.RIGHT, padx=5)

# Запуск основного цикла приложения
window.mainloop()