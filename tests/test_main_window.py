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
    
    def test_setting_on_GUI(self):
        a = Main_window()
        a.aPixMBox.setValue(2.01)
        a.aPixTBox.setValue(3.01)
        a.templatesBox.setText(os.getcwd())
        a.micrographsBox.setText(os.getcwd())
        a.diameterBox.setValue(410)
        exp = DEFAULT_PARAMETERS.copy()
        exp['apixM'] = 2.01
        exp['apixT'] = 3.01
        exp['diameter'] = 410
        exp['micrographs'] = os.getcwd()
        exp['templates'] = os.getcwd()
        res = a.get_parameters()
        self.assertTrue(self.dicts_are_equal_for_common_keys(res, exp, diff=True))
    
    def dicts_are_equal_for_common_keys(self, dict1, dict2, diff=False):
        all_keys = set([k for k in dict1.keys()] + \
                    [k for k in dict2.keys()])
        common_keys = [k for k in all_keys 
                       if k in dict1.keys()
                       if k in dict2.keys()]
        equal = [k for k in common_keys if dict1[k] == dict2[k]]
        different = [k for k in common_keys if dict1[k] != dict2[k]]
        if not different:
            return True
        elif different and diff:
            for k in different:
                print (f'Key: {k}. Dict1 = {dict1[k]} != Dict2 = {dict2[k]}')
                return False
        
    def test_default_state(self):
        a = Main_window()
        res = a.get_parameters()
        exp = DEFAULT_PARAMETERS.copy()
        self.assertTrue(self.dicts_are_equal_for_common_keys(res, exp, diff=True))
        
    def test_set_parameters(self):
        a = Main_window()
        exp = DEFAULT_PARAMETERS.copy()
        a.set_parameters(exp)
        res = a.get_parameters()
        self.assertTrue(self.dicts_are_equal_for_common_keys(res, exp, diff=True))
    
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
            QTest.mouseClick(a.templateBrowseButton, Qt.LeftButton)
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
            QTest.mouseClick(a.templateBrowseButton, Qt.LeftButton)
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
        QTest.mouseClick(a.templateBrowseButton, Qt.LeftButton) #popup dialog
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
                
