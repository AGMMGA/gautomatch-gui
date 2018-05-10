# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Thu May 10 18:58:25 2018
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 243)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 40, 781, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.basicOptionsLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.basicOptionsLayout.setContentsMargins(0, 0, 0, 0)
        self.basicOptionsLayout.setObjectName("basicOptionsLayout")
        self.aPixTLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.aPixTLabel.setObjectName("aPixTLabel")
        self.basicOptionsLayout.addWidget(self.aPixTLabel, 1, 3, 1, 1)
        self.templateLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.templateLabel.setObjectName("templateLabel")
        self.basicOptionsLayout.addWidget(self.templateLabel, 1, 0, 1, 1)
        self.micrographsBrowseButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.micrographsBrowseButton.setObjectName("micrographsBrowseButton")
        self.basicOptionsLayout.addWidget(self.micrographsBrowseButton, 0, 2, 1, 1)
        self.templatesBrowseButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.templatesBrowseButton.setObjectName("templatesBrowseButton")
        self.basicOptionsLayout.addWidget(self.templatesBrowseButton, 1, 2, 1, 1)
        self.templatesBox = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.templatesBox.setObjectName("templatesBox")
        self.basicOptionsLayout.addWidget(self.templatesBox, 1, 1, 1, 1)
        self.micrographsBox = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.micrographsBox.setObjectName("micrographsBox")
        self.basicOptionsLayout.addWidget(self.micrographsBox, 0, 1, 1, 1)
        self.micrographsLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.micrographsLabel.setObjectName("micrographsLabel")
        self.basicOptionsLayout.addWidget(self.micrographsLabel, 0, 0, 1, 1)
        self.aPixMLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.aPixMLabel.setObjectName("aPixMLabel")
        self.basicOptionsLayout.addWidget(self.aPixMLabel, 0, 3, 1, 1)
        self.diameterLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.diameterLabel.setObjectName("diameterLabel")
        self.basicOptionsLayout.addWidget(self.diameterLabel, 3, 3, 1, 1)
        self.aPixTBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.aPixTBox.setObjectName("aPixTBox")
        self.basicOptionsLayout.addWidget(self.aPixTBox, 1, 4, 1, 1)
        self.aPixMBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.aPixMBox.setObjectName("aPixMBox")
        self.basicOptionsLayout.addWidget(self.aPixMBox, 0, 4, 1, 1)
        self.diameterBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.diameterBox.setMaximum(1000)
        self.diameterBox.setObjectName("diameterBox")
        self.basicOptionsLayout.addWidget(self.diameterBox, 3, 4, 1, 1)
        self.basicOptionsLabel = QtWidgets.QLabel(self.centralwidget)
        self.basicOptionsLabel.setGeometry(QtCore.QRect(0, 10, 71, 16))
        self.basicOptionsLabel.setObjectName("basicOptionsLabel")
        self.micrographWidget = QtWidgets.QWidget(self.centralwidget)
        self.micrographWidget.setGeometry(QtCore.QRect(0, 180, 781, 641))
        self.micrographWidget.setObjectName("micrographWidget")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.micrographWidget)
        self.buttonBox.setGeometry(QtCore.QRect(0, 0, 271, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.aPixTLabel.setText(QtWidgets.QApplication.translate("MainWindow", "Å/pixel (templates)", None, -1))
        self.templateLabel.setText(QtWidgets.QApplication.translate("MainWindow", "Templates", None, -1))
        self.micrographsBrowseButton.setText(QtWidgets.QApplication.translate("MainWindow", "Browse...", None, -1))
        self.templatesBrowseButton.setText(QtWidgets.QApplication.translate("MainWindow", "Browse...", None, -1))
        self.micrographsLabel.setText(QtWidgets.QApplication.translate("MainWindow", "Micrographs", None, -1))
        self.aPixMLabel.setText(QtWidgets.QApplication.translate("MainWindow", "Å/pixel (micrograph)", None, -1))
        self.diameterLabel.setText(QtWidgets.QApplication.translate("MainWindow", "Particle diameter (Å)", None, -1))
        self.basicOptionsLabel.setText(QtWidgets.QApplication.translate("MainWindow", "Basic Options", None, -1))

