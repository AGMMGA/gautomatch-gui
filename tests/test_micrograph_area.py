import os
import sys
import unittest
from unittest.mock import MagicMock, patch

from ui_elements.micrograph_area import Micrograph_loader, PLACEHOLDER_IMAGE

class Test_micrograph_cycling(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(Test_micrograph_cycling, self).__init__(*args, **kwargs)
    
    def side_effect(self, arg):
        return arg
    
    def test_loads_placeholder_on_empty_init(self):
        l = Micrograph_loader()
        self.assertEqual(l.cached_mics, [PLACEHOLDER_IMAGE])
    
    def test_get_next_mic(self):
        files = ['1.mrc','2.mrc','3.mrc','4.mrc']
        l = Micrograph_loader(files)
        self.assertEqual(l.get_next_mic(), '2.mrc', msg ='normal call')
        self.assertEqual(l.get_next_mic(), '3.mrc', msg ='normal call')
        self.assertEqual(l.get_next_mic(), '4.mrc', msg ='normal call')
        self.assertEqual(l.get_next_mic(), '1.mrc', msg ='wrap-around call')
        self.assertEqual(l.get_next_mic(), '2.mrc', msg ='normal call')
        self.assertEqual(l.get_next_mic(), '3.mrc', msg ='normal call')
        self.assertEqual(l.get_next_mic(), '4.mrc', msg ='normal call')
        self.assertEqual(l.get_next_mic(), '1.mrc', msg ='second wrap-around call')
#         
    def test_get_previous_mic(self):
        files = ['1.mrc','2.mrc','3.mrc','4.mrc']
        l = Micrograph_loader(files)
        self.assertEqual(l.get_previous_mic(), '4.mrc', msg ='wrap-around call')
        self.assertEqual(l.get_previous_mic(), '3.mrc', msg ='normal call')
        self.assertEqual(l.get_previous_mic(), '2.mrc', msg ='normal call')
        self.assertEqual(l.get_previous_mic(), '1.mrc', msg ='normal call')
        self.assertEqual(l.get_previous_mic(), '4.mrc', msg ='second wrap-around call')
        self.assertEqual(l.get_previous_mic(), '3.mrc', msg ='normal call')
        self.assertEqual(l.get_previous_mic(), '2.mrc', msg ='normal call')
        self.assertEqual(l.get_previous_mic(), '1.mrc', msg ='normal call')
        
    def test_get_current_mic(self):
        files = ['1.mrc','2.mrc','3.mrc','4.mrc']
        l = Micrograph_loader(files)
        self.assertEqual(l.get_current_mic(), '1.mrc')
        l.current_mic_index = 3
        self.assertEqual(l.get_current_mic(), '4.mrc')
        
    def test_load_image_batch(self):
        l = Micrograph_loader()
        test_images = [os.path.abspath('../tests/static/test1.tif'), 
                       os.path.abspath('../tests/static/test2.tif')]
        l.load_image_batch(test_images)
        self.assertEqual(l.cached_mics, test_images)
        
    def test_load_image_not_found(self):
        l = Micrograph_loader()
        with self.assertRaises(OSError):
            l.load_image_batch(['notexisting', 'notanimage.tif'])
        
        
    