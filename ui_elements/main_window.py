# -*- coding: utf-8 -*-

import os
import sys

from PySide2.QtWidgets import (QMainWindow, QApplication, QDialogButtonBox,
                                QFileDialog, QMessageBox)
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QObject, Signal, Slot
from PySide2.QtGui import QPixmap

from gautomatch_runner import Gautomatch_runner, InvalidParameter
from ui_elements.uiMainWindow import Ui_Gautomatcher
from ui_elements.micrograph_area import Micrograph_widget

DEFAULT_PARAMETERS={'micrographs':'',
                    'templates':'',
                    'apixM': 1.34,
                    'apixT': 1.34,
                    'diameter': 400,
                    'T': 'NONE',
                    'ang_step': 5,
                    'speed': 2,
                    'boxsize': 128,
                    'min_dist': 300,
                    'cc_cutoff': 0.1,
                    'lsigma_cutoff': 1.2,
                    'lsigmaD': 100,
                    'lave_min': -1.0,
                    'lave_max': 1.0,
                    'lave_D': 400,
                    'lp': 30,
                    'hp': 1000,
                    'pre_hp': 1000,
                    'pre_lp': 8.0}
DEFAULT_FLAGS = {'do_pre_filter': False}

class Main_window(Ui_Gautomatcher, QMainWindow):
    
    def __init__(self):
        super(Main_window, self).__init__()
        self.setupUi(self)
        self.runner = Gautomatch_runner()
        self.runButton = self.buttonBox.addButton(u'Run Gautomatch', 
                                                  QDialogButtonBox.ApplyRole)
        self.micrographsBrowseButton.clicked.connect(self.open_file_browser)
        self.templateBrowseButton.clicked.connect(self.open_file_browser)
        self.runButton.clicked.connect(self.run_gautomatch)
        self.buttonBox.rejected.connect(sys.exit)
        self.buttonBox.button(QDialogButtonBox.RestoreDefaults).clicked.connect(
            self.restore_defaults)
        self.set_parameters(DEFAULT_PARAMETERS)
#         self.micrographWidget = Micrograph_widget()
#         self.micrographWidget.setParent(self)
        
    def run_gautomatch(self):
        parameters = self.get_parameters()
        try:
            coordinates = self.runner.run(parameters)
            self.refresh_coordinates(coordinates)
        except InvalidParameter as e:
            self.alert_user(e)
            
    def get_parameters(self):
        parms = {}
        m = self.micrographsBox.text()
        parms['micrographs'] = os.path.normpath(m) if m else ''
        t = self.templatesBox.text()
        parms['templates'] = os.path.normpath(t) if t else ''
        parms['apixM'] = float(self.aPixMBox.value())
        parms['apixT'] = float(self.aPixTBox.value())
        parms['diameter'] = int(self.diameterBox.value())
        parms['ang_step'] = int(self.angStepBox.value())
        parms['speed'] = int(self.speedBox.value())
        parms['boxsize'] = int(self.boxSizeBox.value())
        parms['min_dist'] = int(self.minDistanceBox.value())
        parms['cc_cutoff'] = float(self.ccCutoffBox.value())
        parms['lsigma_cutoff'] = float(self.localSigmaCutoffBox.value())
        parms['lsigmaD'] = float(self.localSigmaDiameterBox.value())
        parms['lave_min'] = float(self.localAverageMinBox.value())
        parms['lave_max'] = float(self.localAverageMaxBox.value())
        parms['lave_D'] = int(self.localAverageDiameterBox.value())
        parms['lp'] = int(self.lowPassBox.value())
        parms['hp'] = int(self.highPassBox.value())
        parms['pre_hp'] = int(self.preHighPassBox.value())
        parms['pre_lp'] = int(self.preLowPassBox.value())
        return parms
    
    def set_parameters(self, parms):
        self.aPixMBox.setValue(parms['apixM'])
        self.aPixTBox.setValue(parms['apixT'])
        self.diameterBox.setValue(parms['diameter'])
        self.angStepBox.setValue(parms['ang_step'])
        self.speedBox.setValue(parms['speed'])
        self.boxSizeBox.setValue(parms['boxsize'])
        self.minDistanceBox.setValue(parms['min_dist'])
        self.ccCutoffBox.setValue(parms['cc_cutoff'])
        self.localSigmaCutoffBox.setValue(parms['lsigma_cutoff'])
        self.localSigmaDiameterBox.setValue(parms['lsigmaD'])
        self.localAverageMinBox.setValue(parms['lave_min'])
        self.localAverageMaxBox.setValue(parms['lave_max'])
        self.localAverageDiameterBox.setValue(parms['lave_D'])
        self.lowPassBox.setValue(parms['lp'])
        self.highPassBox.setValue(parms['hp'])
        self.preHighPassBox.setValue(parms['pre_hp'])
        self.preLowPassBox.setValue(parms['pre_lp'])
        
    def open_file_browser(self):
        if self.sender() == self.templateBrowseButton:
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
        self.alert.setWindowTitle(exception.window_title)
        if exception.informative_text:
            self.alert.setInformativeText(exception.informative_text)
        #TODO: fix the annoying beeping issue
        #self.alert.setIcon(QMessageBox.Warning) disabled because stupid beeping
        self.alert.show()
    
    def restore_defaults(self):
        self.set_parameters(DEFAULT_PARAMETERS)
        
    
    
def main():
    app = QApplication(sys.argv)
    a = Main_window()
    a.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()


    