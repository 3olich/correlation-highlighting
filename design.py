# -*- coding: utf-8 -*-

# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 450)
        MainWindow.setMinimumSize(QtCore.QSize(500, 450))
        MainWindow.setMaximumSize(QtCore.QSize(500, 450))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.wick = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.wick.setMaximum(1.0)
        self.wick.setSingleStep(0.1)
        self.wick.setObjectName("wick")
        self.gridLayout_2.addWidget(self.wick, 8, 2, 1, 1)
        self.goButton = QtWidgets.QPushButton(self.centralwidget)
        self.goButton.setObjectName("goButton")
        self.gridLayout_2.addWidget(self.goButton, 9, 1, 1, 3)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 8, 1, 1, 1)
        self.fileLabel = QtWidgets.QLabel(self.centralwidget)
        self.fileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fileLabel.setObjectName("fileLabel")
        self.gridLayout_2.addWidget(self.fileLabel, 0, 0, 1, 5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 7, 1, 1, 3)
        self.cyclesFrom = QtWidgets.QSpinBox(self.centralwidget)
        self.cyclesFrom.setObjectName("cyclesFrom")
        self.cyclesFrom.setRange(0, 999)
        self.gridLayout_2.addWidget(self.cyclesFrom, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 5, 1, 1, 3)
        self.fileSelector = QtWidgets.QPushButton(self.centralwidget)
        self.fileSelector.setObjectName("fileSelector")
        self.gridLayout_2.addWidget(self.fileSelector, 1, 1, 1, 3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 3, 1, 1, 3)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 6, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 4, 1, 1)
        self.cyclesTo = QtWidgets.QSpinBox(self.centralwidget)
        self.cyclesTo.setObjectName("cyclesTo")
        self.cyclesTo.setRange(0, 999)
        self.gridLayout_2.addWidget(self.cyclesTo, 4, 3, 1, 1)
        self.strong = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.strong.setMaximum(1.0)
        self.strong.setSingleStep(0.1)
        self.strong.setObjectName("strong")
        self.gridLayout_2.addWidget(self.strong, 6, 2, 1, 1)
        self.warningLabel = QtWidgets.QLabel(self.centralwidget)
        self.warningLabel.setMinimumSize(QtCore.QSize(0, 80))
        self.warningLabel.setText("")
        self.warningLabel.setObjectName("warningLabel")
        self.gridLayout_2.addWidget(self.warningLabel, 10, 0, 1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.goButton.setText(_translate("MainWindow", "Обработать"))
        self.label_7.setText(_translate("MainWindow", "До"))
        self.fileLabel.setText(_translate("MainWindow", "Выберите файл"))
        self.label_6.setText(_translate("MainWindow", "Слабое взаимодействие"))
        self.label_3.setText(_translate("MainWindow", "До"))
        self.label_4.setText(_translate("MainWindow", "Сильное взаимодействие"))
        self.fileSelector.setText(_translate("MainWindow", "Обзор"))
        self.label.setText(_translate("MainWindow", "Обработать циклы"))
        self.label_5.setText(_translate("MainWindow", "От"))
        self.label_2.setText(_translate("MainWindow", "От"))

