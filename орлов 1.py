import tkinter as tk
from tkinter import messagebox


def show_position(pos):
    position_description = {
        'NW': "Верхний левый угол",
        'N': "Центр верхней стороны",
        'NE': "Верхний правый угол",
        'W': " Центр левой стороны",
        'CENTER': "Центр окна",
        'E': "Центр правой стороны",
        'SW': "Нижний левый угол",
        'S': "Центр нижней стороны",
        'SE': "Нижний правый угол"
    }
    messagebox.showinfo("Позиция кнопки", f"{pos}: {position_description[pos]}")

# Основные настройки окна
root = tk.Tk()
root.title("Диагональная компоновка кнопок")
root.geometry("400x400")

buttons_positions = ['NW', 'N', 'NE', 'W', 'CENTER', 'E', 'SW', 'S', 'SE']
button_placements = [
    {'relx': 0.1, 'rely': 0.1},   #
    {'relx': 0.5, 'rely': 0.1},
    {'relx': 0.9, 'rely': 0.1},
    {'relx': 0.1, 'rely': 0.5},
    {'relx': 0.5, 'rely': 0.5},
    {'relx': 0.9, 'rely': 0.5},
    {'relx': 0.1, 'rely': 0.9},
    {'relx': 0.5, 'rely': 0.9},
    {'relx': 0.9, 'rely': 0.9}
]

for i, pos in enumerate(buttons_positions):
    btn = tk.Button(root, text=pos, width=8, height=2,
                   command=lambda p=pos: show_position(p))
    btn.place(**button_placements[i], anchor="center")


root.mainloop()