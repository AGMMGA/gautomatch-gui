# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MicrographArea.ui'
#
# Created: Sun Jun  3 09:59:39 2018
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_micrographWidget(object):
    def setupUi(self, micrographWidget):
        micrographWidget.setObjectName("micrographWidget")
        micrographWidget.resize(640, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(micrographWidget.sizePolicy().hasHeightForWidth())
        micrographWidget.setSizePolicy(sizePolicy)
        self.layoutWidget = QtWidgets.QWidget(micrographWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 642, 691))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.micrographArea = QtWidgets.QScrollArea(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(64)
        sizePolicy.setVerticalStretch(64)
        sizePolicy.setHeightForWidth(self.micrographArea.sizePolicy().hasHeightForWidth())
        self.micrographArea.setSizePolicy(sizePolicy)
        self.micrographArea.setMinimumSize(QtCore.QSize(640, 640))
        self.micrographArea.setWidgetResizable(True)
        self.micrographArea.setObjectName("micrographArea")
        self.micrographAreaContents = QtWidgets.QWidget()
        self.micrographAreaContents.setGeometry(QtCore.QRect(0, 0, 638, 681))
        self.micrographAreaContents.setObjectName("micrographAreaContents")
        self.micrographLabel = QtWidgets.QLabel(self.micrographAreaContents)
        self.micrographLabel.setGeometry(QtCore.QRect(0, 0, 640, 640))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.micrographLabel.sizePolicy().hasHeightForWidth())
        self.micrographLabel.setSizePolicy(sizePolicy)
        self.micrographLabel.setScaledContents(True)
        self.micrographLabel.setObjectName("micrographLabel")
        self.micrographArea.setWidget(self.micrographAreaContents)
        self.verticalLayout.addWidget(self.micrographArea)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.NoButton)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(micrographWidget)
        QtCore.QMetaObject.connectSlotsByName(micrographWidget)

    def retranslateUi(self, micrographWidget):
        micrographWidget.setWindowTitle(QtWidgets.QApplication.translate("micrographWidget", "Form", None, -1))
        self.micrographLabel.setText(QtWidgets.QApplication.translate("micrographWidget", "TextLabel", None, -1))

