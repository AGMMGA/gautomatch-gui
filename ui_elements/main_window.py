# -*- coding: utf-8 -*-

import sys

from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

from gautomatch_runner import gautomatch_runner, InvalidParameters
from ui_elements.uiMainWindow import Ui_MainWindow

from 

class main_window( Ui_MainWindow, QMainWindow):
    
    def __init__(self):
        super(main_window, self).__init__()
        self.setupUi(self)
        self.runner = gautomatch_runner()
        
    def run_gautomatch(self):
        parameters = self.get_parameters()
        try:
            coordinates = self.runner.run(parameters)
            self.refresh_coordinates(coordinates)
        except InvalidParameters as e:
            self.alert_user(e.msg)
            
    def get_parameters(self):
        parameters = {}
        parameters['apixM'] = self.aPixMBox.text
        parameters['apixT'] = self.aPixTBox.text
        parameters['diameter'] = self.diameterBox.text
        return parameters
    
    def refresh_coordinates(self, coordinates=[]):
        pass
    
    def alert_user(self):
        pass
    
def main():
    app = QApplication(sys.argv)
    
    a = main_window()
    a.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()


    