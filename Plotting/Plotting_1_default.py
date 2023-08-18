# Построение синусоиды
import matplotlib.pyplot as plt  # библиотека для построения графиков
import numpy as np  # библиотека для работы с массивами данных

x = np.linspace(0, 2.0 * np.pi, 100)  # угол варьируется от 0 до 2*pi, 100 точек между началом и концом
y = np.sin(x)  # расчет точек y по функции синуса

plt.plot(x, y)  # расчет точек графика
plt.show()  # показ графика
