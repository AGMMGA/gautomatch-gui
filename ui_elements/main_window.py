# -*- coding: utf-8 -*-

import os
import sys

from PySide2.QtWidgets import (QMainWindow, QApplication, QDialogButtonBox,
                                QFileDialog, QMessageBox)
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QObject, Signal, Slot
from PySide2.QtGui import QPixmap

from gautomatch_runner import Gautomatch_runner, InvalidParameter
from ui_elements.uiMainWindow import Ui_MainWindow

DEFAULT_PARAMETERS={'micrographs':'',
                    'templates':'',
                    'apixM': 1.34,
                    'aPixT': 1.34,
                    'diameter': 400,
                    'T': 'NONE'}

class Main_window( Ui_MainWindow, QMainWindow):
    
    def __init__(self):
        super(Main_window, self).__init__()
        self.setupUi(self)
        self.runner = Gautomatch_runner()
        self.runButton = self.buttonBox.addButton(u'Run Gautomatch', QDialogButtonBox.ApplyRole)
        self.micrographsBrowseButton.clicked.connect(self.open_file_browser)
        self.templatesBrowseButton.clicked.connect(self.open_file_browser)
        self.runButton.clicked.connect(self.run_gautomatch)
        
    def run_gautomatch(self):
        parameters = self.get_parameters()
        try:
            coordinates = self.runner.run(parameters)
            self.refresh_coordinates(coordinates)
        except InvalidParameter as e:
            self.alert_user(e)
            
    def get_parameters(self):
        parms = {}
        parms['apixM'] = float(self.aPixMBox.value())
        parms['apixT'] = float(self.aPixTBox.value())
        parms['diameter'] = int(self.diameterBox.value())
        m = self.micrographsBox.text()
        parms['micrographs'] = os.path.normpath(m) if m else ''
        t = self.templatesBox.text()
        parms['templates'] = os.path.normpath(t) if t else ''
        return parms
    
    def open_file_browser(self):
        print('dicked')
        if self.sender() == self.templatesBrowseButton:
            target = self.templatesBox
            title = 'Open templates file'
            filters = 'Templates (*.mrc);;All files (*.*)'
        elif self.sender() == self.micrographsBrowseButton:
            target = self.micrographsBox
            title = 'Open micrographs for picking'
            filters = 'Micrographs (*.mrc);;All files (*.*)'
        #We make the browse file dialog non modal by using show instead of exec_
        #this is the only way we can write tests
        #To retrieve its result, we connect it to a custom slot and embed its target
        #in an attribute
        #only one file_dialog can be present at a time, because it's stored in
        #an attribute and a second dialog would overwrite
        self.browse_dialog = QFileDialog()
        self.browse_dialog.filesSelected.connect(self.get_nonmodal_return)
        self.browse_dialog.setFileMode(QFileDialog.ExistingFile)
        self.browse_dialog.setWindowTitle(title)
        self.browse_dialog.setDirectory(os.getcwd()),
        self.browse_dialog.setNameFilter(filters)
        self.browse_dialog.target = target
        self.browse_dialog.show() 
        return
    
    @Slot(str)
    def get_nonmodal_return(self):
        sender = self.sender()
        sender.target.setText(sender.selectedFiles()[0])
        
    
    def refresh_coordinates(self, coordinates=[]):
        pass
    
    def alert_user(self, exception):
        self.alert = QMessageBox()
        self.alert.setText(str(exception))
        if exception.informative_text:
            self.alert.setInformativeText(exception.informative_text)
        #TODO: fix the annoying beeping issue
        #self.alert.setIcon(QMessageBox.Warning) disabled because stupid beeping
        self.alert.show()
        
    
def main():
    app = QApplication(sys.argv)
    
    a = Main_window()
    a.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()


    