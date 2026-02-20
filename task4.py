import tkinter as tk
import os

# Список планет
planets_earthlike = ["Меркурий", "Венера", "Земля", "Марс"]
planets_gasgiants = ["Юпитер", "Сатурн", "Уран", "Нептун"]

# Инициализация окон
root = tk.Tk()
root.title("Планеты Солнечной системы")

# Поле вывода результата
result_text = tk.Text(root)
result_text.pack(pady=10)


# Функция для сохранения в файл
def save_to_file():
    with open('planets.txt', 'w') as file:
        # Заголовки колонок
        file.write(f'{"Планеты-землеподобные":^20}| {"Газовые гиганты":^20}\n')

        for planet in planets_earthlike + planets_gasgiants:
            if planet in planets_earthlike:
                file.write(f'{planet:<20}| ')
            else:
                file.write(f' {planet:<20}')

            # Переход на новую строку каждые четыре элемента
            if len(planets_earthlike) % 4 == 0 and len(planets_gasgiants) % 4 == 0:
                file.write('\n')

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Данные успешно сохранены в файл planets.txt\n")


# Функция для очистки файла
def clear_file():
    try:
        os.remove('planets.txt')
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Файл очищен.\n")
    except FileNotFoundError:
        pass


# Кнопки действий
save_button = tk.Button(root, text="Распределить и сохранить", command=save_to_file)
save_button.pack(side='left', padx=(10, 5))

clear_button = tk.Button(root, text="Очистить", command=clear_file)
clear_button.pack(side='right', padx=(5, 10))

# Основной цикл приложения
if __name__ == "__main__":
    root.mainloop()