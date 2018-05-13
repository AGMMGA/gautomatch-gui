import os
import sys
import unittest

from unittest.mock import patch
from PySide2.QtWidgets import QApplication, QFileDialog, QDialogButtonBox
from PySide2.QtTest import QTest
from PySide2.QtCore import Qt

from ui_elements.main_window import Main_window, DEFAULT_PARAMETERS


class Test_get_and_set_parameters(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(Test_get_and_set_parameters, self).__init__(*args, **kwargs)
    
    def setUp(self):
        try:
            self.app = QApplication(sys.argv)
        except RuntimeError:
            pass
    
    def test_works_ok(self):
        a = Main_window()
        a.aPixMBox.setValue(2.01)
        a.aPixTBox.setValue(3.01)
        a.templatesBox.setText(os.getcwd())
        a.micrographsBox.setText(os.getcwd())
        a.diameterBox.setValue(410)
        exp = {}
        exp['apixM'] = 2.01
        exp['apixT'] = 3.01
        exp['diameter'] = 410
        exp['micrographs'] = os.getcwd()
        exp['templates'] = os.getcwd()
        
        self.assertEqual(a.get_parameters(), exp)
        self.assertEqual(type(exp['apixM']), type(1.00))
        self.assertEqual(type(exp['apixT']), type(1.00))
        self.assertEqual(type(exp['diameter']), type(1))
        
    def test_empty_state(self):
        a = Main_window()
        res = a.get_parameters()
        exp = {'apixM' : 0.0,
               'apixT' : 0.0,
               'diameter' : 0,
               'micrographs' : '',
               'templates' : ''}
        self.assertEqual(res, exp)
        
    def test_set_parameters(self):
        a = Main_window()
        p = DEFAULT_PARAMETERS.copy()
        a.set_parameters(p)
        res = a.get_parameters()
        for k in p.copy().keys():
            if k not in res:
                del p[k]
        assert(p.keys() == res.keys())
        self.assertEqual(p, res)
    
    def test_restore_defaults(self):
        a = Main_window()
        p = DEFAULT_PARAMETERS.copy()
        a.restore_defaults()
        res = a.get_parameters()
        for k in p.copy().keys():
            if k not in res:
                del p[k]
        assert(p.keys() == res.keys())
        self.assertEqual(p, res)
        
    def test_restore_defaults_key(self):
        a = Main_window()
        p = DEFAULT_PARAMETERS.copy()
        QTest.mouseClick(a.buttonBox.button(QDialogButtonBox.RestoreDefaults),
                         Qt.LeftButton)
        res = a.get_parameters()
        for k in p.copy().keys():
            if k not in res:
                del p[k]
        assert(p.keys() == res.keys())
        self.assertEqual(p, res)
        
        
class Test_browse_files(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(Test_browse_files, self).__init__(*args, **kwargs)
    
    def setUp(self):
        try:
            self.app = QApplication(sys.argv)
        except RuntimeError:
            pass
       
    def test_browse_canceled(self):
        a = Main_window()
        with patch('PySide2.QtWidgets.QFileDialog.show') as p:
            QTest.mouseClick(a.micrographsBrowseButton, Qt.LeftButton)
            p.assert_called_once()
            p.reset_mock()
            self.assertEqual(a.micrographsBox.text(), '')
            QTest.mouseClick(a.templatesBrowseButton, Qt.LeftButton)
            p.assert_called_once()
            self.assertEqual(a.templatesBox.text(), '')
        
    def test_browse_micrographs_creates_popup(self):
        a = Main_window()
        with patch('PySide2.QtWidgets.QFileDialog.show') as p:
            QTest.mouseClick(a.micrographsBrowseButton, Qt.LeftButton)
            p.assert_called_once()
    
    def test_browse_templates_creates_popup(self):
        a = Main_window()
        with patch('PySide2.QtWidgets.QFileDialog.show') as p:
            QTest.mouseClick(a.templatesBrowseButton, Qt.LeftButton)
            p.assert_called_once()
    
    def test_browse_micrographs_updates_micrographsBox(self):
        a = Main_window()
        #testing with a real file
        import inspect
        test_file = inspect.getfile(os)
        QTest.mouseClick(a.micrographsBrowseButton, Qt.LeftButton) #popup dialog
        a.browse_dialog.selectFile(test_file) #select a file
        QTest.keyClicks(a.browse_dialog, '\r') #return to close
        self.assertEqual(os.path.normpath(test_file).lower(),
                         os.path.normpath(a.micrographsBox.text().lower()))

    def test_browse_micrographs_updates_templatesBox(self):
        a = Main_window()
        import inspect
        test_file = inspect.getfile(os)
        QTest.mouseClick(a.templatesBrowseButton, Qt.LeftButton) #popup dialog
        a.browse_dialog.selectFile(test_file) #select a file
        QTest.keyClicks(a.browse_dialog, '\r') #return to close
        self.assertEqual(os.path.normpath(test_file).lower(),
                         os.path.normpath(a.templatesBox.text().lower()))
        
class Test_run_gautomatch(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(Test_run_gautomatch, self).__init__(*args, **kwargs)
        
    def setUp(self):
        try:
            self.app = QApplication(sys.argv)
        except RuntimeError:
            pass
    
    def test_alerts_on_invalid_parameter(self):
        #using NoMicrographsChosen as a representative of InvalidParameter
        a = Main_window()
        with patch('ui_elements.main_window.Main_window.alert_user') as p:
            QTest.mouseClick(a.runButton, Qt.LeftButton) #will trigger no micrographs selected
            p.assert_called_with()
                
