import os
import sys
import unittest

from unittest.mock import patch
from PySide2.QtWidgets import QApplication, QFileDialog
from PySide2.QtTest import QTest
from PySide2.QtCore import Qt

from ui_elements.main_window import Main_window


class Test_get_parameters(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(Test_get_parameters, self).__init__(*args, **kwargs)
    
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
        exp['apixM'] = str(2.01)
        exp['apixT'] = str(3.01)
        exp['diameter'] = str(410)
        exp['micrographs'] = os.getcwd()
        exp['templates'] = os.getcwd()
        
        self.assertEqual(a.get_parameters(), exp)
        
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
        
    def test_browse_something(self):
        a = Main_window()
        with patch('PySide2.QtWidgets.QFileDialog.show') as p, \
             patch('PySide2.QtWidgets.QFileDialog.selectedFiles', 
                   return_value=['/a/path/to/file']) as ret:
            QTest.mouseClick(a.micrographsBrowseButton, Qt.LeftButton)
            p.assert_called_once()
            p.reset_mock()
            self.assertEqual(a.micrographsBox.text(), '/a/path/to/file')
            QTest.mouseClick(a.templatesBrowseButton, Qt.LeftButton)
            p.assert_called_once()
            self.assertEqual(a.templatesBox.text(), '/a/path/to/file')
    
