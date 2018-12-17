import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt
from numpy import meshgrid
from numpy import arange

def simple_plot():
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='About as simple as it gets, folks')
    ax.grid()

    # fig.savefig("test.png")
    plt.show()

def stack_plots():
    x = [1, 2, 3, 4, 5]
    y1 = [1, 1, 2, 3, 5]
    y2 = [0, 4, 2, 6, 8]
    y3 = [1, 3, 5, 7, 9]

    y = np.vstack([y1, y2, y3])

    labels = ["Fibonacci ", "Evens", "Odds"]

    fig, ax = plt.subplots()
    ax.stackplot(x, y1, y2, y3, labels=labels)
    # Легенда
    ax.legend()
    plt.show()

    fig, ax = plt.subplots()
    ax.stackplot(x, y)
    plt.show()

def batman():
    xs = arange(-7.25, 7.25, 0.01)
    ys = arange(-5, 5, 0.01)
    x, y = meshgrid(xs, ys)

    eq1 = ((x / 7) ** 2 * sqrt(abs(abs(x) - 3) / (abs(x) - 3)) + (y / 3) ** 2 * sqrt(
        abs(y + 3 / 7 * sqrt(33)) / (y + 3 / 7 * sqrt(33))) - 1)
    eq2 = (abs(x / 2) - ((3 * sqrt(33) - 7) / 112) * x ** 2 - 3 + sqrt(1 - (abs(abs(x) - 2) - 1) ** 2) - y)
    eq3 = (9 * sqrt(abs((abs(x) - 1) * (abs(x) - .75)) / ((1 - abs(x)) * (abs(x) - .75))) - 8 * abs(x) - y)
    eq4 = (3 * abs(x) + .75 * sqrt(abs((abs(x) - .75) * (abs(x) - .5)) / ((.75 - abs(x)) * (abs(x) - .5))) - y)
    eq5 = (2.25 * sqrt(abs((x - .5) * (x + .5)) / ((.5 - x) * (.5 + x))) - y)
    eq6 = (6 * sqrt(10) / 7 + (1.5 - .5 * abs(x)) * sqrt(abs(abs(x) - 1) / (abs(x) - 1)) - (6 * sqrt(10) / 14) * sqrt(
        4 - (abs(x) - 1) ** 2) - y)

    for f in [eq1, eq2, eq3, eq4, eq5, eq6]:
        plt.contour(x, y, f, [0])
    plt.show()


def main():
    y = np.arange(0.0, 2.0, 0.01)
    x = 1 + np.sin(2 * np.pi * y)

    fig, ax = plt.subplots()
    ax.plot(y, x, color="indigo")

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='Тест', yticks=[0,1,2])


    ax.grid()

    # fig.savefig("test.png")
    plt.show()


if __name__ == '__main__':
    main()