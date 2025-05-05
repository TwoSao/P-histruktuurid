import numpy as np
import matplotlib.pyplot as plt

# Создаем график
fig, ax = plt.subplots()
ax.set_title("Kilpkonn")  # Черепаха (по-эстонски)

# Функции и их диапазоны
x1 = np.linspace(-12, 12, 24)
y1 = (-1/18)*x1**2 + 12

x2 = np.linspace(-4, 4, 8)
y2 = (-1/8)*x2**2 + 6

x3 = np.linspace(-12, -4, 8)
y3 = (-1/8)*(x3+8)**2 + 6

x4 = np.linspace(4, 12, 8)
y4 = (-1/8)*(x4-8)**2 + 6

x5 = np.linspace(-4, 0.3, 8)
y5 = 2*(x5+3)**2 - 9

x6 = np.linspace(-4, 0.2, 8)
y6 = 1.5*(x6+3)**2 - 10
# Рисуем все линии
ax.plot(x1, y1, 'g')
ax.plot(x2, y2, 'g')
ax.plot(x2, y3, 'r')
ax.plot(x3, y4, 'r')
ax.plot(x4, y5, 'g')
ax.plot(x5, y6, 'g')


plt.grid(True)
plt.show()
