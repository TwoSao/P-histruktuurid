import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np


root = tk.Tk()
root.title("Квадратные уравнения")
tk.Label(root, text="Решение квадратного уравнения", font=("Arial", 16), bg="lightblue").pack(fill="x")

frame = tk.Frame(root)
frame.pack(pady=10)

entry_a = tk.Entry(frame, width=5, bg="lightblue")
entry_a.grid(row=0, column=0)
tk.Label(frame, text="x² +").grid(row=0, column=1)
entry_b = tk.Entry(frame, width=5, bg="lightblue")
entry_b.grid(row=0, column=2)
tk.Label(frame, text="x +").grid(row=0, column=3)
entry_c = tk.Entry(frame, width=5, bg="lightblue")
entry_c.grid(row=0, column=4)
tk.Label(frame, text="= 0").grid(row=0, column=5)
tk.Button(frame, text="Решить", bg="green", command=solve).grid(row=0, column=6, padx=10)

result_label = tk.Label(root, text="Решение", bg="yellow", font=("Arial", 12))
result_label.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()
