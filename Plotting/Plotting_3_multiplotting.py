# Добавление нескольких графиков путем наложения
# Подходит для графиков с одинаковыми ограничениями x, y
# Использование команды одиночного графика и легенды
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2.0 * np.pi, 101)
y = np.sin(x)  # расчет точек y по функции синуса
z = np.cos(x)  # расчет точек z по функции косинуса

# значения для отметок по осям x и y
xnumbers = np.linspace(0, 7, 15)
ynumbers = np.linspace(-1, 1, 11)

plt.plot(x, y, 'orange', x, z, 'b')
plt.xlabel("Угол в радианах")  # подпись оси x
plt.ylabel("Амплитуда")  # подпись оси y
plt.title("График некоторых тригонометрических функций")  # подпись графика
plt.xticks(xnumbers)  # Установка текущего местоположения делений и меткок оси x
plt.yticks(ynumbers)  # Установка текущего местоположения делений и меткок оси y
plt.legend(['sin', 'cos'])  # отображение легенды (подписей графиков)
plt.grid()  # создание сетки
plt.axis([0, 6.5, -1.1, 1.1])  # [x_старт, x_конец, y_старт, y_конец] изменение подписи осей
plt.show()  # вывод графика на экран
