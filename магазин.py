import tkinter as tk
from tkinter import messagebox
import hashlib
import random
import string
from PIL import Image, ImageTk
import os


class AuthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Авторизация и регистрация")

        # Фиксированный размер окна
        self.root.geometry("450x600")
        self.root.resizable(False, False)

        # Центрируем окно
        self.center_window(450, 600)

        # Данные пользователей
        self.users = {}

        # Текущий пользователь
        self.current_user = None

        # Создаем интерфейс
        self.create_widgets()

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def create_widgets(self):
        # Основной контейнер с отступами
        main_frame = tk.Frame(self.root, bg='#f0f0f0', padx=30, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Заголовок
        title_label = tk.Label(main_frame, text="АВТОРИЗАЦИЯ / РЕГИСТРАЦИЯ",
                               font=("Arial", 16, "bold"),
                               bg='#f0f0f0', fg='#2c3e50')
        title_label.pack(pady=(0, 20))

        # Рамка для формы
        form_frame = tk.Frame(main_frame, bg='white', relief=tk.GROOVE, bd=2)
        form_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Внутренние отступы формы
        form_content = tk.Frame(form_frame, bg='white', padx=25, pady=25)
        form_content.pack(fill=tk.BOTH, expand=True)

        # Логин
        tk.Label(form_content, text="Логин:", font=("Arial", 11),
                 bg='white', anchor='w').pack(fill=tk.X, pady=(0, 5))

        self.login_entry = tk.Entry(form_content, font=("Arial", 11),
                                    bg='#f8f9fa', relief=tk.SUNKEN, bd=2)
        self.login_entry.pack(fill=tk.X, pady=(0, 15), ipady=5)
        self.login_entry.focus()

        # Пароль
        tk.Label(form_content, text="Пароль:", font=("Arial", 11),
                 bg='white', anchor='w').pack(fill=tk.X, pady=(0, 5))

        self.password_entry = tk.Entry(form_content, font=("Arial", 11),
                                       show="*", bg='#f8f9fa',
                                       relief=tk.SUNKEN, bd=2)
        self.password_entry.pack(fill=tk.X, pady=(0, 20), ipady=5)

        # Кнопки
        btn_frame = tk.Frame(form_content, bg='white')
        btn_frame.pack(fill=tk.X, pady=10)

        # Первый ряд кнопок
        btn_row1 = tk.Frame(btn_frame, bg='white')
        btn_row1.pack(fill=tk.X, pady=5)

        tk.Button(btn_row1, text="Войти", command=self.login,
                  bg='#3498db', fg='white', font=("Arial", 11, "bold"),
                  width=12, height=1, cursor='hand2', relief=tk.RAISED, bd=2).pack(side=tk.LEFT, padx=5)

        tk.Button(btn_row1, text="Регистрация", command=self.register,
                  bg='#2ecc71', fg='white', font=("Arial", 11, "bold"),
                  width=12, height=1, cursor='hand2', relief=tk.RAISED, bd=2).pack(side=tk.LEFT, padx=5)

        # Второй ряд кнопок
        btn_row2 = tk.Frame(btn_frame, bg='white')
        btn_row2.pack(fill=tk.X, pady=5)

        tk.Button(btn_row2, text="Сброс", command=self.clear_fields,
                  bg='#e74c3c', fg='white', font=("Arial", 11, "bold"),
                  width=25, height=1, cursor='hand2', relief=tk.RAISED, bd=2).pack()

        # Требования к паролю
        requirements_frame = tk.Frame(form_content, bg='#f8f9fa', relief=tk.SUNKEN, bd=1)
        requirements_frame.pack(fill=tk.X, pady=15)

        tk.Label(requirements_frame, text="Требования к паролю:",
                 font=("Arial", 10, "bold"), bg='#f8f9fa', fg='#2c3e50').pack(anchor='w', padx=10, pady=(10, 5))

        tk.Label(requirements_frame, text="• Минимум 8 символов",
                 font=("Arial", 10), bg='#f8f9fa', fg='#7f8c8d', anchor='w').pack(anchor='w', padx=20)

        tk.Label(requirements_frame, text="• Должен содержать символ ($ # @)",
                 font=("Arial", 10), bg='#f8f9fa', fg='#7f8c8d', anchor='w').pack(anchor='w', padx=20, pady=(0, 10))

        # Статус
        status_frame = tk.Frame(main_frame, relief=tk.SUNKEN, bd=1, bg='white')
        status_frame.pack(fill=tk.X, pady=10)

        self.status_label = tk.Label(status_frame, text="Ожидание ввода...",
                                     font=("Arial", 10), bg='white', fg='#7f8c8d')
        self.status_label.pack(pady=8)

        # Привязываем Enter
        self.root.bind('<Return>', lambda event: self.login())

    def validate_password(self, password):
        """Проверка пароля: минимум 8 символов и содержит спецсимвол ($ # @)"""
        if len(password) < 8:
            return False, "Пароль должен содержать минимум 8 символов"

        # Проверяем наличие спецсимволов $ # @
        special_chars = ['$', '#', '@']
        if not any(char in special_chars for char in password):
            return False, "Пароль должен содержать один из символов: $ # @"

        return True, "Пароль корректен"

    def login(self):
        """Обработка входа"""
        login = self.login_entry.get().strip()
        password = self.password_entry.get()

        if not login or not password:
            messagebox.showerror("Ошибка", "Заполните все поля!")
            self.status_label.config(text="Ошибка: заполните все поля", fg='#e74c3c')
            return

        # Проверяем существование пользователя
        if login in self.users and self.users[login]['password'] == password:
            self.current_user = login

            # Очищаем форму и открываем магазин
            self.clear_fields()
            self.root.withdraw()  # Скрываем главное окно
            self.open_store()

        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль!")
            self.status_label.config(text="Ошибка входа", fg='#e74c3c')

    def register(self):
        """Обработка регистрации"""
        login = self.login_entry.get().strip()
        password = self.password_entry.get()

        if not login or not password:
            messagebox.showerror("Ошибка", "Заполните все поля!")
            self.status_label.config(text="Ошибка: заполните все поля", fg='#e74c3c')
            return

        if login in self.users:
            messagebox.showerror("Ошибка", "Пользователь с таким логином уже существует!")
            self.status_label.config(text="Логин занят", fg='#e74c3c')
            return

        is_valid, message = self.validate_password(password)
        if not is_valid:
            messagebox.showerror("Ошибка", message)
            self.status_label.config(text=message, fg='#e74c3c')
            return

        # Сохраняем нового пользователя
        self.users[login] = {'password': password}

        messagebox.showinfo("Успех", "Регистрация прошла успешно!\nТеперь вы можете войти.")
        self.clear_fields()
        self.status_label.config(text="Регистрация успешна", fg='#2ecc71')

    def clear_fields(self):
        """Очистка полей ввода"""
        self.login_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.login_entry.focus()

    def open_store(self):
        """Открывает виртуальный магазин после успешной авторизации"""
        store_root = tk.Toplevel()
        store_root.title("Магазин электроники")
        store_root.geometry("800x600")
        store_root.resizable(True, True)

        # Настройка интерфейса магазина
        store_app = StoreApp(store_root)
        store_root.mainloop()


class StoreApp:
    def __init__(self, root):
        self.root = root
        self.products = {
            'Смартфоны': [
                {"id": 1, "name": "iPhone 14 Pro Max", "price": 1200},
                {"id": 2, "name": "Samsung Galaxy S23 Ultra", "price": 1100},
                {"id": 3, "name": "Xiaomi Mi 13 Pro", "price": 800}
            ],
            'Ноутбуки': [
                {"id": 4, "name": "MacBook Air M2", "price": 1500},
                {"id": 5, "name": "Dell XPS 13", "price": 1300},
                {"id": 6, "name": "Lenovo ThinkPad X1 Carbon Gen 10", "price": 1400}
            ],
            'Планшеты': [
                {"id": 7, "name": "iPad Pro 12.9", "price": 1000},
                {"id": 8, "name": "Galaxy Tab S8+", "price": 900},
                {"id": 9, "name": "Huawei MatePad Pro", "price": 700}
            ]
        }

        self.cart_items = []

        # Интерфейс магазина
        self.create_store_interface()

    def create_store_interface(self):
        # Основная панель
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Навигационная панель слева
        nav_frame = tk.Frame(main_frame, bg="#eaeaea", width=200)
        nav_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Категории товаров
        categories = list(self.products.keys())
        for category in categories:
            button = tk.Button(nav_frame, text=category, font=("Arial", 12),
                               command=lambda cat=category: self.show_products(cat),
                               bg="#3498db", fg="white", relief=tk.RAISED, bd=2)
            button.pack(fill=tk.X, pady=5)

        # Контент справа
        content_frame = tk.Frame(main_frame, bg="white")
        content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Панель продуктов
        self.product_list_frame = tk.Frame(content_frame, bg="white")
        self.product_list_frame.pack(fill=tk.BOTH, expand=True)

        # Корзина покупок
        cart_frame = tk.Frame(content_frame, bg="#eaeaea", height=100)
        cart_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Информация о корзине
        tk.Label(cart_frame, text="Корзина:", font=("Arial", 12), bg="#eaeaea").pack(side=tk.LEFT, padx=10)
        self.cart_label = tk.Label(cart_frame, text="", font=("Arial", 12), bg="#eaeaea")
        self.cart_label.pack(side=tk.LEFT, padx=10)

        # Кнопка оформления заказа
        checkout_button = tk.Button(cart_frame, text="Оформить заказ", font=("Arial", 12),
                                    command=self.checkout_cart, bg="#2ecc71", fg="white", relief=tk.RAISED, bd=2)
        checkout_button.pack(side=tk.RIGHT, padx=10)

    def show_products(self, category):
        """Отображает товары выбранной категории"""
        products = self.products.get(category, [])

        # Очищаем предыдущий список товаров
        for widget in self.product_list_frame.winfo_children():
            widget.destroy()

        # Отображение товаров
        for product in products:
            item_frame = tk.Frame(self.product_list_frame, bg="white", relief=tk.GROOVE, bd=2)
            item_frame.pack(fill=tk.X, pady=5)

            name_label = tk.Label(item_frame, text=product['name'], font=("Arial", 14), bg="white")
            name_label.pack(side=tk.LEFT, padx=10)

            price_label = tk.Label(item_frame, text=f"Цена: ${product['price']}", font=("Arial", 12), bg="white")
            price_label.pack(side=tk.RIGHT, padx=10)

            add_to_cart_button = tk.Button(item_frame, text="Добавить в корзину", font=("Arial", 10),
                                           command=lambda prod=product: self.add_to_cart(prod),
                                           bg="#3498db", fg="white", relief=tk.RAISED, bd=2)
            add_to_cart_button.pack(side=tk.RIGHT, padx=10)

    def add_to_cart(self, product):
        """Добавляет товар в корзину"""
        self.cart_items.append(product)
        self.update_cart_label()

    def remove_from_cart(self, index):
        """Удаляет товар из корзины по индексу"""
        del self.cart_items[index]
        self.update_cart_label()

    def update_cart_label(self):
        """Обновляет отображение содержимого корзины"""
        total_price = sum([item["price"] for item in self.cart_items])
        items_count = len(self.cart_items)
        self.cart_label.config(text=f"Товары ({items_count}) | Общая сумма: ${total_price:.2f}")

    def checkout_cart(self):
        """Оформление заказа"""
        if not self.cart_items:
            messagebox.showwarning("Предупреждение", "Корзина пуста!")
            return

        result = messagebox.askyesno("Подтверждение заказа",
                                     f"Ваша корзина содержит {len(self.cart_items)} товара(-ов).\nОбщая стоимость: ${sum([item['price'] for item in self.cart_items]):.2f}\n\nВы подтверждаете покупку?")
        if result:
            messagebox.showinfo("Заказ подтвержден", "Ваш заказ принят.\nСпасибо за покупку!")
            self.cart_items.clear()
            self.update_cart_label()


# Запуск приложения
if __name__ == "__main__":
    # Проверяем наличие Pillow
    try:
        from PIL import Image, ImageTk
    except ImportError:
        print("=" * 50)
        print("УСТАНОВИТЕ БИБЛИОТЕКУ Pillow:")
        print("pip install Pillow")
        print("=" * 50)
        exit()

    root = tk.Tk()
    app = AuthApp(root)
    root.mainloop()