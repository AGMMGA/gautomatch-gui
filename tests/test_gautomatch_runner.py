import os
import sys
import unittest
import inspect

from ui_elements.main_window import DEFAULT_PARAMETERS
from gautomatch_runner import Gautomatch_runner
from gautomatch_runner import (MicrographNotFound, TemplateNotFound, 
                               NoMicrographsChosen)

class test_check_parameters(unittest.TestCase):
    
    def setUp(self):
        self.parameters = DEFAULT_PARAMETERS.copy()
        self.test_file = inspect.getfile(os) #quickly get a file that must exist
        
    def test_raises_NoMicrographsChosen(self):
        r = Gautomatch_runner()
        with self.assertRaises(NoMicrographsChosen):
            r.run(self.parameters)
    
    def test_raises_MicrographsNotFound(self):
        r = Gautomatch_runner()
        self.parameters['micrographs'] = 'notafile'
        with self.assertRaises(MicrographNotFound):
            r.run(self.parameters)
            
    def test_raises_TemplateNotFound(self):
        r = Gautomatch_runner()
        self.parameters['templates'] = 'notafile'
        self.parameters['micrographs'] = self.test_file
        with self.assertRaises(TemplateNotFound):
            r.run(self.parameters)
    
    def test_accepts_empty_templates(self):
        r = Gautomatch_runner()
        self.parameters['templates'] = ''
        self.parameters['micrographs'] = self.test_file
        self.assertTrue(r.check_parameters(self.parameters)) #returns 1 on success