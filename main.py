# -*- coding: utf-8 -*-

"""
Translate .csv with some human stats to graph with stats correlation

author - 3olich

pip3 install numpy, matplotlib, pyqt
"""

import os.path
from sys import argv, exc_info

import design

import matplotlib.pyplot as plt
from numpy import corrcoef, seterr
from PyQt5 import QtWidgets
import xlsxwriter


def tranc(matrix):
    """
    Транспонирует матрицу

    matrix - матрица в формате список списков;
    return - транспонированная матрица в том же формате.
    """

    return list(map(list, zip(*matrix)))


def read_csv(filename, start, end):
    '''
    csv в привычном понимании стандартных библиотек
    разделяет ячейки запятыми, а нам 
    на вход поступает файл с разделением ';'
    '''
    csv_file = open(filename, encoding='cp1251')

    # Пропускаем все строки, до цикла начала
    for i in range(start + 1):
        next(csv_file)

    matr = []

    # обходим каждую строку
    for num, row in enumerate(csv_file):

        # Значения в csv хранятся в формате ' %d%d '
        def to_int(x): return int(x.strip())

        # Первые три столбца не хранят значений
        vals = map(to_int, row.split(';')[3:])

        matr.append(vals)

        # Ограничиваем считывание
        if num == end - start:
            break

    matr = tranc(matr)
    csv_file.close()
    return matr


def serializeToExcel(infile, outfile, st, end):
    workbook = xlsxwriter.Workbook(outfile)
    worksheet = workbook.add_worksheet()

    with open(infile, 'r', encoding='cp1251') as inputed:
        header_row = inputed.read().split('\n')[1]
        headers = header_row.split(';')[3:]

    #  Это просто тут нужно
    worksheet.write('J2', 'Корреляционная матрица по К.Пирсону')
    worksheet.write('W1', 'Таблица')

    worksheet.set_column(0, len(headers) + 1, 4)

    for index, header in enumerate(headers):

        # 3 для шапки
        hcell = f'{chr(ord("B") + index)}3'
        vcell = f'A{index + 4}'
        worksheet.write(hcell, header)
        worksheet.write(vcell, header)

    matrix = corrcoef(read_csv(infile, st, end))

    # Убираем NaN (трехзначная логика)
    matrix = [[x if x == x else 0 for x in row] for row in matrix]

    positive_str = workbook.add_format({'bold': True, 'font_color': 'red'})
    positive_weak = workbook.add_format({'bold': False, 'font_color': 'red'})
    negative_str = workbook.add_format({'bold': True, 'font_color': 'blue'})
    negative_weak = workbook.add_format({'bold': False, 'font_color': 'blue'})

    for num, row in enumerate(matrix):
        for let, cell in enumerate(row):
            if cell > 0.7:
                format_ = positive_str
            elif cell > 0:
                format_ = positive_weak
            elif cell < -0.7:
                format_ = negative_str
            elif cell < 0:
                format_ = negative_weak
            else:
                format_ = workbook.add_format()

            # 4 для того, чтобы можно было написать шапку
            worksheet.write(f'{chr(ord("B") + let)}{num + 4}', cell, format_)
    workbook.close()


class inner_scheme:
    '''
    Объект класса преобразовывает аппаратно-фиксированные значения в схему,
    учитывая взаимную корреляцию значений
    '''

    # Ключ - название центра на схеме
    # Значение[0] - название по - русски
    # Значение[1] - порядок в исходном CSV
    # Значение[2] - координата по X
    # Значение[3] - координата по Y
    positions = {"RP": ["Подж/сел", 0, 3, 0], "F": ["Печень", 1, -3, 0], "E": ["Желудок", 3, 4, 0],
                 "R": ["Почки", 8, -2, -2], "V": ["Моч.поз", 9, -3, -3], "IG": ["Тонкая кишка", 19, -2, 3],
                 "TR": ["Лимф. система", 14, 2, 3], "C": ["Сердце", 18, -1, 2],
                 "MC": ["Эндокринная система", 13, 1, 2],
                 "VB": ["Желчный пузырь", 7, -4, 0], "P": ["Легкие", 11, 2, -2],
                 "GI": ["Толстая кишка", 12, 3, -3]}

    # Показывает, какие линии должны быть нанесены
    lines = (("VB", "V"), ("VB", "IG"), ("VB", "C"),
             ("VB", "R"), ("VB", "F"), ("F", "V"),
             ("F", "R",), ("F", "IG"), ("F", "C"),
             ("F", "MC"), ("F", "P"), ("V", "R"),
             ("V", "GI"), ("V", "P"), ("R", "C"),
             ("R", "MC"), ("R", "P"), ("R", "GI"),
             ("R", "RP"), ("GI", "E"), ("GI", "RP"),
             ("GI", "P"), ("P", "C"), ("P", "MC"),
             ("P", "RP"), ("P", "E"), ("E", "MC"),
             ("E", "RP"), ("E", "TR"), ("RP", "C"),
             ("RP", "MC"), ("RP", "F"), ("RP", "TR"),
             ("MC", "C"), ("MC", "TR"), ("MC", "IG"),
             ("TR", "IG"), ("TR", "C"), ("IG", "C"))

    def __init__(self, source, start, end, strong_corr_coeff, weak_corr_coeff):
        """Конструктор класса

        Keyword arguments:
        source -- исходный файл в формате csv
        start -- номер цикла, с которого начинается обработка
        end -- номер цикла, которым заканчивается обработка
        strong_corr_coeff -- абсолютное значение корреляции,
        с которого взаимодействие считается сильным
        weak_corr_coef -- абсолютное значение корреляции,
        меньше которого взаимодействие считается слабым
        """

        if end <= start:
            raise ValueError(f'Invalid cycle number: start={start}, end={end}')

        if strong_corr_coeff < weak_corr_coeff:
            raise ValueError(f'Invalid coeffs: strong={strong_corr_coeff}, weak={weak_corr_coeff}')

        if not os.path.exists(source):
            raise FileExistsError('File not found')

        self.source = source
        self.start_cycle = start
        self.end_cycle = end
        self.strong_corr_coeff = strong_corr_coeff
        self.weak_corr_coeff = weak_corr_coeff

        # Нужны для названия файлов
        big_percent = str(int(100 * self.strong_corr_coeff))
        small_percent = str(int(100 * self.weak_corr_coeff))

        # Все файлы будут находиться в отдельной папке
        self.result_dir = os.path.join(os.path.dirname(
            os.path.abspath(source)), f'{source[:-4]}[{start}-{end}]({big_percent}-{small_percent})')

        if not os.path.exists(self.result_dir):
            os.makedirs(self.result_dir)

        self.process()

    def process(self):
        self.corr = corrcoef(
            read_csv(self.source, self.start_cycle, self.end_cycle))

        self.draw_init()
        self.draw_nodes()
        self.draw_inner_edges()
        self.draw_outer_edges()
        self.draw_ending()

        serializeToExcel(self.source, os.path.join(
            self.result_dir, 'corr_matrix.xlsx'), self.start_cycle, self.end_cycle)
        plt.show()

    def draw_init(self):
        # Создаем объект под хранение схемы
        self.fig = plt.figure()
        self.ax = self.fig.gca()

        plt.title('Исследование корреляции')

        # Отключаем видимость фрейма и координатную сетку
        self.fig.patch.set_visible(False)
        self.ax.axis('off')

    def draw_nodes(self):
        # Генерируем координаты вершин
        # В Python v3+ map возвращает итератор, а для plotly нужен список
        x = [node[2] for node in inner_scheme.positions.values()]
        y = [node[3] for node in inner_scheme.positions.values()]

        # Наносим вершины на рисунок
        plt.scatter(x, y, color='gray', s=25**2, alpha=1, zorder=2, )

        for center in inner_scheme.positions.keys():

                # Текст отрисовывается особым образом, просто так красивее результат
            def pred(x): return x-0.12
            plt.text(
                *map(pred, inner_scheme.positions[center][2:4]), s=center,)

    def draw_inner_edges(self):
        for line in inner_scheme.lines:
            self.draw_edge(*line)

    def draw_outer_edges(self):
        pass

    def draw_ending(self):
        # outfile = f'{self.source[:-4]}[{self.start_cycle}-{self.end_cycle}]'
        plt.savefig(os.path.join(self.result_dir, 'scheme.jpeg'))

    def draw_edge(self, lhs, rhs):

        x = [inner_scheme.positions[lhs][2], inner_scheme.positions[rhs][2]]
        y = [inner_scheme.positions[lhs][3], inner_scheme.positions[rhs][3]]

        color_positive = "red"
        color_negative = "blue"

        # https://matplotlib.org/examples/color/named_colors.html
        color_light_negative = "skyblue"
        color_light_positive = "darksalmon"

        color_zero = "Black"
        width_fat = 4
        width_thin = 2

        coeff = self.corr[inner_scheme.positions[lhs]
                          [1]][inner_scheme.positions[rhs][1]]

        if -1 <= coeff <= - self.strong_corr_coeff:
            color_ = color_negative
            width_ = width_fat
        elif -self.strong_corr_coeff < coeff <= -self.weak_corr_coeff:
            color_ = color_negative
            width_ = width_thin
        elif -self.weak_corr_coeff < coeff < 0:
            color_ = color_light_negative
            width_ = width_thin
        elif 0 < coeff < self.weak_corr_coeff:
            color_ = color_light_positive
            width_ = width_thin
        elif self.weak_corr_coeff <= coeff < self.strong_corr_coeff:
            color_ = color_positive
            width_ = width_thin
        elif self.strong_corr_coeff <= coeff <= 1:
            color_ = color_positive
            width_ = width_fat
        else:
            color_ = color_zero
            width_ = width_thin

        plt.plot(x, y, color=color_, linewidth=width_, zorder=1)


class GUI(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fileSelector.clicked.connect(self.browse_folder)
        self.goButton.clicked.connect(self.work)

    def browse_folder(self):
        self.fileLabel.clear()
        self.filename = QtWidgets.QFileDialog.getOpenFileName(
            self, "Выберите папку")

        if self.filename:
            self.fileLabel.setText(self.filename[0])
        else:
            self.warningLabel.setText("Не выбран файл!!!")

    def work(self):
        try:
            scheme = inner_scheme(self.filename[0], self.cyclesFrom.value(
            ), self.cyclesTo.value(), self.strong.value(), self.wick.value())
            print(self.filename[0], self.cyclesFrom.value(
            ), self.cyclesTo.value(), self.strong.value(), self.wick.value())
            self.warningLabel.setText(
                f"Все хорошо\nРезультат сохранен в {scheme.result_dir}")
        except:
            self.warningLabel.setText(f"Error: {exc_info()[1]}")


if '__main__' == __name__:
    """
    Формула для коэффициента корреляции Пирсона делит (слово дня - нормализация)
    ковариацию X и Y на произведение их стандартных отклонений.
    Так как Y может иметь нулевую дисперсию,
    ее стандартное отклонение также равно нулю.

    Вот почему иногда появляется ошибка true_divide - деление на ноль.

    Почти во всех файлах есть пара столбцов, где [100, 100, 100, 100, ..]
    При небольшом количестве циклов вылетает в аут.
    """
    seterr(divide='ignore', invalid='ignore')

    app = QtWidgets.QApplication(argv)
    window = GUI()
    window.show()
    app.exec_()
