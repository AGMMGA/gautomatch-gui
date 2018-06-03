# -*- coding: utf-8 -*-

import os
import sys

from PySide2.QtWidgets import (QMainWindow, QApplication, QLabel,
                               QDialogButtonBox)
from PySide2.QtCore import QFile, QObject, Signal, Slot
from PySide2.QtGui import QImageReader, QImage, QPixmap

from ui_elements.uiMicrographArea import Ui_micrographWidget

PLACEHOLDER_IMAGE = os.path.abspath('../static/placeholder.tif')

class Micrograph_loader(object):
    
    def __init__(self, mics=None):
        super().__init__()
        if mics:
            self.cached_mics = mics
        else:
            self.cached_mics = [PLACEHOLDER_IMAGE]
        self.current_mic_index = 0
        
    def open_mic(self, mic):
        if not os.path.isfile(mic):
            msg = (f'The image \n {mic}\n does not exist')
            raise OSError(msg)
        return QPixmap(mic)
    
    def get_next_mic(self):
        try:
            m = self.cached_mics[self.current_mic_index+1]
            self.current_mic_index += 1
            return m
        except IndexError: #end of list!
            self.current_mic_index = 0
            return self.cached_mics[0]
        
    def get_previous_mic(self):
        try:
            m = self.cached_mics[self.current_mic_index-1]
            self.current_mic_index -= 1
            return m
        except IndexError: #end of list!
            self.current_mic_index = len(self.cached_mics)-1
            return self.cached_mics[-1]
        
    def get_current_mic(self):
        return self.cached_mics[self.current_mic_index]
    
    def load_image_batch(self, images):
        '''
        Loads a new batch of images and returns the first in the list.
        Expects a list of paths to valid images
        '''
        if not isinstance(images, list): #debug
            raise ValueError('Please pass a list of images to load, even for single image')
        for img in images:
            if not os.path.isfile(img):
                raise OSError(f'File {img} not found')
        self.cached_mics = images
        self.current_mic_index = 0
        return self.cached_mics[self.current_mic_index]
                

class Micrograph_widget(Ui_micrographWidget, QLabel):
    
    def __init__(self, parent=None):
        super().__init__(parent=None)
        super().setupUi(self)
        self.mic_loader = Micrograph_loader() #loads with placeholder image at init
        self.display_image(self.mic_loader.get_current_mic())
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
        # if the object is initialized empty (no micrographs), we gray out the buttons
        if len(self.mic_loader.cached_mics) == 1:
            self.buttonBox.setEnabled(False)
        
        
    def display_image(self, qpixmap):
        self.micrographLabel.setPixmap(qpixmap)
        
    def show_previous_micrograph(self):
        img = self.mic_loader.open_mic(self.mic_loader.get_previous_mic())
        self.display_image(img)
        
    def show_next_micrograph(self):
        img = self.mic_loader.open_mic(self.mic_loader.get_next_mic())
        self.display_image(img)
    
    def load_new_images(self, images):
        if not images: #debug
            raise ValueError('I need a list of images to load')
        self.mic_loader.load_image_batch(images)
        self.display_image(self.mic_loader.get_current_mic())
        if len(self.mic_loader.cached_mics) == 1:
            self.previousButton.setEnabled(False)
            self.nextButton.setEnabled(False)
        elif len(self.mic_loader.cached_mics) > 1:
#             self.previousButton.setEnabled(True) for whatever reason does not work
            self.buttonBox.setEnabled(True) #cascade enables all children. This works.
    
    def show_previous_pick(self):
        print('previous_pick')
    
    def show_current_pick(self):
        print('current_pick')

def main():
    test_images = [os.path.abspath('../tests/static/test1.tif'), 
                   os.path.abspath('../tests/static/test2.tif')]
    app = QApplication(sys.argv)
    a = Micrograph_widget()
    a.show()
    a.load_new_images(test_images)
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()


