# -*- coding: utf-8 -*-

import os
import sys

from PySide2.QtWidgets import (QMainWindow, QApplication, QLabel,
                               QDialogButtonBox)
from PySide2.QtCore import QFile, QObject, Signal, Slot
from PySide2.QtGui import QImageReader, QImage, QPixmap

from ui_elements.uiMicrographArea import Ui_micrographWidget

class Micrograph_widget(Ui_micrographWidget, QLabel):
    
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.previousButton = self.buttonBox.addButton(u'<', 
                                                  QDialogButtonBox.ApplyRole)
        self.nextButton = self.buttonBox.addButton(u'>', 
                                                  QDialogButtonBox.ApplyRole)
        self.previousPickButton = self.buttonBox.addButton(u'Previous pick', 
                                                  QDialogButtonBox.ApplyRole)
        self.currentPickButton = self.buttonBox.addButton(u'Current pick', 
                                                  QDialogButtonBox.ApplyRole)
        self.previousButton.clicked.connect(self.show_previous_micrograph)
        self.nextButton.clicked.connect(self.show_next_micrograph)
        self.previousPickButton.clicked.connect(self.show_previous_pick)
        self.currentPickButton.clicked.connect(self.show_current_pick)
        
    def load_image(self, image_path):
        if not os.path.isfile(image_path):
            msg = (f'The image \n {image_path}\n does not exist')
            raise OSError(msg)
        pixmap = QPixmap(image_path)
#         r = QImageReader(image_path)
#         r.setAutoTransform(True)
#         img =r.read()
        self.micrographLabel.setPixmap(pixmap)
        
    def show_previous_micrograph(self):
        print('previous mic')
    
    def show_next_micrograph(self):
        print('next_mic')
    
    def show_previous_pick(self):
        print('previous_pick')
    
    def show_current_pick(self):
        print('current_pick')

def main():
    app = QApplication(sys.argv)
    a = Micrograph_widget()
    image_path = os.path.normpath(
        os.path.abspath('..\\tests\static\micrograph.tif'))
    a.load_image(image_path)
    a.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()


