import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

def solve():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        D = b**2 - 4*a*c
        if D > 0:
            x1 = (-b + D**0.5) / (2*a)
            x2 = (-b - D**0.5) / (2*a)
            result = f"2 корня: x₁ = {x1:.2f}, x₂ = {x2:.2f}"
        elif D == 0:
            x = -b / (2*a)
            result = f"1 корень: x = {x:.2f}"
        else:
            result = "Нет действительных корней"
        result_label.config(text=result)

        x = np.linspace(-10, 10, 400)
        y = a*x**2 + b*x + c
        plt.plot(x, y)
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')
        plt.title("График")
        plt.grid()
        plt.show()
    except Exception as e:
        result_label.config(text=f"Ошибка ввода: {e}")

    
root = tk.Tk()
root.title("Квадратные уравнения")
tk.Label(root, text="Решение квадратного уравнения", font=("Arial", 16), bg="lightblue").pack(fill="x")
root.geometry("600x200")
root.background = "Black"
frame = tk.Frame(root)
frame.pack(pady=10)

entry_a = tk.Entry(frame, width=5, bg="white")
entry_a.grid(row=0, column=0)
tk.Label(frame, text="x² +").grid(row=0, column=1)
entry_b = tk.Entry(frame, width=5, bg="white")
entry_b.grid(row=0, column=2)
tk.Label(frame, text="x +").grid(row=0, column=3)
entry_c = tk.Entry(frame, width=5, bg="white")
entry_c.grid(row=0, column=4)
tk.Label(frame, text="= 0").grid(row=0, column=5)
tk.Button(frame, text="Решить", bg="green", command=solve).grid(row=0, column=6, padx=10)

result_label = tk.Label(root, text="Решение", bg="white", font=("Arial", 12))
result_label.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()
