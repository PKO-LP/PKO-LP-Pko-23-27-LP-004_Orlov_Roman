import tkinter as tk


class ShoppingCalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Инициализация главного окна
        self.title("Расчёт стоимости покупок")
        self.geometry('300x200')

        # Переменные для хранения введённых значений и итоговой суммы
        self.prices = []
        self.total_label_var = tk.StringVar()
        self.total_label_var.set("Итого: 0 ₽")

        # Поле ввода цены
        self.entry_price = tk.Entry(self)
        self.entry_price.pack(pady=10)

        # Кнопка добавления нового товара
        add_button = tk.Button(self, text="Добавить +", command=self.add_item)
        add_button.pack()

        # Кнопка подсчета общей суммы
        total_button = tk.Button(self, text="Итого", command=self.calculate_total)
        total_button.pack()

        # Метка для вывода общей суммы
        self.total_label = tk.Label(self, textvariable=self.total_label_var)
        self.total_label.pack()

        # Кнопка сохранения результата в файл
        save_button = tk.Button(self, text="Сохранить", command=self.save_to_file)
        save_button.pack(side='left', padx=(20, 0))

        # Кнопка очистки файла
        clear_button = tk.Button(self, text="Очистить", command=self.clear_file)
        clear_button.pack(side='right', padx=(0, 20))

    def add_item(self):
        """ Добавляет новую цену товара """
        try:
            price = float(self.entry_price.get())
            if price > 0:
                self.prices.append(price)
                self.entry_price.delete(0, 'end')  # Очищаем поле ввода
            else:
                raise ValueError("Цена должна быть положительной.")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def calculate_total(self):
        """ Рассчитывает общую сумму всех товаров """
        total_sum = sum(self.prices)
        self.total_label_var.set(f"Итого: {total_sum:.2f} ₽")

    def save_to_file(self):
        """ Сохраняет итоги в файл summ.txt """
        with open('summ.txt', 'w') as file:
            for idx, price in enumerate(self.prices):
                file.write(f"Товар {idx + 1}: {price:.2f}\n")
            file.write(f"\nИтого: {sum(self.prices):.2f}\n")

    def clear_file(self):
        """ Очищает содержимое файла результатов """
        with open('summ.txt', 'w'):
            pass  # Открываем файл и сразу закрываем, очищая его содержание
        self.prices.clear()  # также очищаем список цен внутри программы
        self.total_label_var.set("Итого: 0 ₽")  # обновляем метку


if __name__ == "__main__":
    app = ShoppingCalculatorApp()
    app.mainloop()