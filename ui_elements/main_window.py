# -*- coding: utf-8 -*-

import os
import sys

from PySide2.QtWidgets import (QMainWindow, QApplication, QDialogButtonBox,
                                QFileDialog)
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

from gautomatch_runner import gautomatch_runner, InvalidParameters
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
        self.runner = gautomatch_runner()
        self.buttonBox.addButton(u'Run Gautomatch', QDialogButtonBox.ApplyRole)
        self.micrographsBrowseButton.clicked.connect(self.open_file_browser)
        self.templatesBrowseButton.clicked.connect(self.open_file_browser)
        
        
    def run_gautomatch(self):
        exp = self.get_parameters()
        try:
            coordinates = self.runner.run(exp)
            self.refresh_coordinates(coordinates)
        except InvalidParameters as e:
            self.alert_user(e.msg)
            
    def get_parameters(self):
        exp = {}
        exp['apixM'] = self.aPixMBox.text()
        exp['apixT'] = self.aPixTBox.text()
        exp['diameter'] = self.diameterBox.text()
        exp['micrographs'] = self.micrographsBox.text()
        exp['templates'] = self.templatesBox.text()
        return exp
    
    def open_file_browser(self):
        if self.sender() == self.templatesBrowseButton:
            target = self.templatesBox
            title = 'Open templates file'
            filters = 'Templates (*.mrc);;All files (*.*)'
        elif self.sender() == self.micrographsBrowseButton:
            target = self.micrographsBox
            title = 'Open micrographs for picking'
            filters = 'Micrographs (*.mrc);;All files (*.*)'
        self.browse_dialog = QFileDialog()
        self.browse_dialog.setFileMode(QFileDialog.ExistingFile)
        self.browse_dialog.setWindowTitle(title)
        self.browse_dialog.setDirectory(os.getcwd()),
        self.browse_dialog.setNameFilter(filters)
        self.browse_dialog.show()
        selected = self.browse_dialog.selectedFiles()
        if selected:
            target.setText(selected[0])
        return
    
    def refresh_coordinates(self, coordinates=[]):
        pass
    
    def alert_user(self):
        pass
    
def main():
    app = QApplication(sys.argv)
    
    a = Main_window()
    a.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()


    