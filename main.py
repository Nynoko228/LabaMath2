import matplotlib.pyplot as plt  # для графиков
from pylab import mpl
import math
import numpy
from Form import Application
from scipy.signal import savgol_filter
# Аппроксимация полиномиальной кривой с одной переменной


import tkinter as tk  # для интерфейса


def formula():
    global x, y
    data = podgonka(x, y)
    fin = []
    fin += [rf"${data[0][0]}*a_{0}+{data[0][1]}*a_{1} + {data[0][2]}*a_{2}={data[0][3]};$"]
    fin += [rf" ${data[1][0]}*a_{0}+{data[1][1]}*a_{1} + {data[1][2]}*a_{2}={data[1][3]};$"]
    fin += [rf" ${data[2][0]}*a_{0}+{data[2][1]}*a_{1} + {data[2][2]}*a_{2}={data[2][3]};$"]
    root = tk.Toplevel()
    app = Application(fin, master=root)
    app.mainloop()


def mainWidget():
    root1 = tk.Tk()
    root1.geometry("350x350")
    text = tk.Label(root1,
                    text="Номер таблицы",
                    font=("Helvetica 11")).place(x=65, y=150)
    NumTbl = tk.Entry(root1).place(x=95, y=150)
    text1 = tk.Label(root1,
                     text="Значение интерполяции",
                     font=("Helvetica 11")).place(x=65, y=170)
    NumInt = tk.Entry(root1).place(x=95, y=170)
    tk.Button(root1,
              text='N',
              command=root1.quit,
              font=("Helvetica 11")).place(x=170, y=180)
    tk.Button(root1,
              text='Formula',
              command=formula,
              font=("Helvetica 11")).place(x=150, y=280)

    tk.mainloop()


def tkek():
    root = tk.Tk()
    tk.Label(root,
             text="x").grid(row=0)
    tk.Label(root,
             text="y").grid(row=1)

    x1 = tk.Entry(root)
    x2 = tk.Entry(root)
    x3 = tk.Entry(root)
    x4 = tk.Entry(root)
    x5 = tk.Entry(root)
    x6 = tk.Entry(root)
    x7 = tk.Entry(root)
    y1 = tk.Entry(root)
    y2 = tk.Entry(root)
    y3 = tk.Entry(root)
    y4 = tk.Entry(root)
    y5 = tk.Entry(root)
    y6 = tk.Entry(root)
    y7 = tk.Entry(root)

    x1.grid(row=0, column=1)
    x2.grid(row=0, column=2)
    x3.grid(row=0, column=3)
    x4.grid(row=0, column=4)
    x5.grid(row=0, column=5)
    x6.grid(row=0, column=6)
    x7.grid(row=0, column=7)
    y1.grid(row=1, column=1)
    y2.grid(row=1, column=2)
    y3.grid(row=1, column=3)
    y4.grid(row=1, column=4)
    y5.grid(row=1, column=5)
    y6.grid(row=1, column=6)
    y7.grid(row=1, column=7)
    lstX = [x1, x2, x3, x4, x5, x6, x7]
    lstY = [y1, y2, y3, y4, y5, y6, y7]
    tk.Button(root,
              text='OK',
              command=root.quit).grid(row=3,
                                      column=4,
                                      sticky=tk.W,
                                      pady=4)
    global x, y
    for i in range(len(lstX)):
        lstX[i].insert(0, x[i])
        lstY[i].insert(0, y[i])
    tk.mainloop()
    if (len(x) == 0) and (len(y) == 0):
        tk.Label(root,
                 text="interpolation").grid(row=2)
        interpoll = tk.Entry(root)
        interpoll.grid(row=2, column=1)
        X = [float(x1.get()), float(x2.get()), float(x3.get()), float(x4.get()), float(x5.get()), float(x6.get()),
             float(x7.get())]
        Y = [float(y1.get()), float(y2.get()), float(y3.get()), float(y4.get()), float(y5.get()), float(y6.get()),
             float(y7.get())]
        return X, Y
    else:
        X = [x1.get(), x2.get(), x3.get(), x4.get(), x5.get(), x6.get(),
             x7.get()]
        Y = [y1.get(), y2.get(), y3.get(), y4.get(), y5.get(), y6.get(),
             y7.get()]
        for i in range(len(X)):
            if X[i] != "":
                x[i] = float(X[i])
        for i in range(len(Y)):
            if Y[i] != "":
                y[i] = float(Y[i])
    grafik()


def grafik():
    global x, y
    data = podgonka(x, y)
    print(data)
    data1 = [data[0][-1:], data[1][-1:], data[2][-1:]]
    data2 = [data[0][:-1], data[1][:-1], data[2][:-1]]
    print("Значения a0, a1 и a2:")
    param = numpy.linalg.solve(data2, data1)
    print(numpy.linalg.solve(data2, data1))
    print("Новые Y")
    newData = calculate(x, [param[2][0], param[1][0], param[0][0]])
    draw(x, newData, y)
    form = r'$\left\{\begin{matrix} a_{0}n+a_{1}\sum x + a_{2}\sum x^{2}=\sum y\\  ' \
           r'a_{0}\sum x+a_{1}\sum x^{2} + a_{2}\sum x^{3}=\sum yx \\ ' \
           r'a_{0}\sum x^{2}+a_{1}\sum x^{3} + a_{2}\sum x^{4}=\sum yx^{2} \end{matrix}\right.$'
    mpl.rcParams['font.sans-serif'] = ['Arial']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.title(r"$y=a_{0}+a_{1}x+a_{2}x^{2}$")
    plt.legend(loc="upper left")
    plt.show()


def HelloWidget(lstx, lsty):
    root1 = tk.Tk()
    root1.geometry("350x350")
    text = tk.Label(root1,
                    text="Вы хотите изменить данные?",
                    font=("Helvetica 11")).place(x=65, y=150)
    tk.Button(root1,
              text='Y',
              command=tkek,
              # command=root1.quit,
              font=("Helvetica 11")).place(x=95, y=180)
    tk.Button(root1,
              text='N',
              command=grafik,
              font=("Helvetica 11")).place(x=200, y=180)

    tk.Button(root1,
              text='Formula',
              command=formula,
              font=("Helvetica 11")).place(x=150, y=280)

    tk.mainloop()


# Функция podgonka высчитывает коэффициенты для системы нормальных уравнений
def podgonka(data_x, data_y):
    size = len(data_x)
    i = 0
    sum_x = 0
    sum_sqare_x = 0
    sum_third_power_x = 0
    sum_four_power_x = 0
    average_x = 0
    average_y = 0
    sum_y = 0
    sum_xy = 0
    sum_sqare_xy = 0
    while i < size:
        sum_x += data_x[i]
        sum_y += data_y[i]
        sum_sqare_x += math.pow(data_x[i], 2)
        sum_third_power_x += math.pow(data_x[i], 3)
        sum_four_power_x += math.pow(data_x[i], 4)
        sum_xy += data_x[i] * data_y[i]
        sum_sqare_xy += math.pow(data_x[i], 2) * data_y[i]
        i += 1;
    average_x = sum_x / size
    average_y = sum_y / size
    # print([[size, sum_x, sum_sqare_x, sum_y],
    #         [sum_x, sum_sqare_x, sum_third_power_x, sum_xy],
    #         [sum_sqare_x,sum_third_power_x,sum_four_power_x,sum_sqare_xy]])
    return [[size, sum_x, sum_sqare_x, sum_y],
            [sum_x, sum_sqare_x, sum_third_power_x, sum_xy],
            [sum_sqare_x, sum_third_power_x, sum_four_power_x, sum_sqare_xy]]


# Вычислить значение подобранной кривой


def calculate(data_x, parameters):
    data_y = []
    for x in data_x:
        data_y.append(parameters[2] + parameters[1] * x + parameters[0] * x * x)
    print(data_y)
    return data_y


# Функция draw рисует наши кривые на координатной плоскости
def draw(data_x, data_y_new, data_y_old):
    global x, y
    t = numpy.polyfit(x, y, 2)
    f = numpy.poly1d(t)
    print(f)
    x1 = numpy.linspace(-2, 4, 30)
    print(x1)
    print(f(x1))
    plt.plot(data_x, data_y_new, label="подгоночная кривая", color="black")
    # plt.plot(x1, f(x1), label="подгоночная кривая", color="black")
    plt.scatter(sorted(data_x), sorted(data_y_old), label="табличные данные")
    # plt.plot(sorted(data_x), sorted(data_y_old))


print("Введите номер таблицы: ", end="")
# table = int(input())
table = 8
match table:
    case 0:
        x = ""
        y = ""
        x, y = tkek()
    case 1:
        x = [-2, 0, 1, 3, 5, 6, 8]
        y = [5, -1, 2, 10, 24, 36, 38]
        HelloWidget(x, y)
    case 2:
        x = [0.5, 1, 1.5, 2, 2.5, 3, 3.5]
        y = [0.4, 0.3, 1, 1.7, 2.1, 3.4, 4]
        HelloWidget(x, y)
    case 3:
        x = [0.4, 0.8, 1.2, 1.6, 2, 2.4, 2.8]
        y = [0.43, 0.94, 1.91, 3.01, 4, 4.56, 5]
        HelloWidget(x, y)

    case 4:
        x = [4.5, 5.0, 5.5, 6.0, 6.5, 7, 7.5]
        y = [7.7, 9.4, 11.4, 13.6, 15.6, 17, 18]
        HelloWidget(x, y)
    case 5:
        x = [0, 0.5, 1, 1.5, 2, 2.5, 3]
        y = [25, 26, 4, 7, 6, 13, 20]
        HelloWidget(x, y)
    case 6:
        x = [1, 1.5, 2, 2.5, 3, 3.5, 4]
        y = [0.22, 23, 31, 43, 56, 82, 60]
        HelloWidget(x, y)
    case 7:
        x = [4.5, 5, 5.5, 6, 6.5, 7, 7.5]
        y = [7.7, 9.4, 11.4, 13.6, 15.6, 18.6, 20]
        HelloWidget(x, y)
    case 8:
        x = [-2, -1, 0, 1, 2, 3, 4]
        y = [4, 0, -1, 0, 5, 10, 12]
        HelloWidget(x, y)
    case 9:
        x = [0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 1]
        y = [1, 2, 4, 7, 10, 16, 13]
        HelloWidget(x, y)

    case 10:
        x = [2, 4, 5, 7, 9, 10, 12]
        y = [0.4, 0.16, 2.5, 4.9, 9, 100, 120]
        HelloWidget(x, y)
