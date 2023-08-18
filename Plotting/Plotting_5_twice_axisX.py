# Добавление нескольких графиков по двойной оси Y
# Подходит для графиков с разным диапазоном оси x
# Отдельные оси и фигурные объекты
# Реплицирование объекта осей и построение кривых

import numpy as np
import matplotlib.pyplot as plt

y = np.linspace(0, 2.0*np.pi, 101)
x1 = np.sin(y)
x2 = np.sinh(y)  # гиперболический синус

# значения для отметок по осям x и y
ynumbers = np.linspace(0, 7, 15)  # (минимальное, максимальное, количество значений)
xnumbers1 = np.linspace(-1, 1, 11)
xnumbers2 = np.linspace(0, 300, 7)

# разделяем объект фигуры и объект осей из объекта построения
fig, ax1 = plt.subplots()

# Дублируем оси с другой оси x и та же ось Y
ax2 = ax1.twiny() # ax2 и ax1 будут иметь общую ось Y и разные оси X

# построить кривые по осям 1 и 2 и получить манипуляторы осей
curve1, = ax1.plot(x1, y, label="sin", color='r')
curve2, = ax2.plot(x2, y, label="sinh", color='b')

# Создайте список кривых для доступа к параметрам кривых
curves = [curve1, curve2]

# добавить легенду через объект оси 1 или оси 2.
# обычно достаточно одной команды
# ax1.legend() # не будет отображать легенду для ax2
# ax2.legend() # не будет отображать легенду для ax1
# ax1.legend(curves, [curve.get_label() для кривой в кривых])
ax2.legend(curves, [curve.get_label() for curve in curves]) # также верно

# задаем надписи и цвет осям X
ax1.set_xlabel("Амплитуда", color=curve1.get_color())
ax2.set_xlabel("Амплитуда", color=curve2.get_color())

# задаем надписи и цвет оси Y
ax1.set_ylabel("Угол/значение", color=curve1.get_color())
# ax2.set_ylabel("Magnitude", color=curve2.get_color()) # не будет работать
# ax2 не имеет контроля свойств над осью Y

# y ticks (цифровые отметки оси Y) - сделаем их тоже цветными
ax1.tick_params(axis='y', colors=curve1.get_color())
# ax2.tick_params(axis='y', colors=curve2.get_color()) # не будет работать
# ax2 не имеет контроля свойств над осью Y

# цвет осей x задается через ax1 и ax2
ax1.tick_params(axis='x', colors=curve1.get_color())
ax2.tick_params(axis='x', colors=curve2.get_color())

# установить x значения делений
ax1.set_xticks(xnumbers1)
#ax2.set_xticks(xnumbers2)

# установить y значения делений
ax1.set_yticks(ynumbers)
ax2.set_yticks(ynumbers) # также работает

# цвет сетки (красный), для значений ax1
#ax1.grid(color=curve1.get_color())
# цвет  сетки (синий), для значений ax1
ax1.grid(color=curve2.get_color())

# цвет вертикальных линий сетки (синий), для значений ax2
ax2.grid(color=curve2.get_color())
ax1.xaxis.grid(False)  # запрет отрисовки вертикальных осей для ax1

# Глобальные свойства фигуры
plt.title("График синуса и гиперболического синуса")
plt.show()