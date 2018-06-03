import os
import sys
import unittest
from unittest.mock import MagicMock, patch

from PySide2.QtWidgets import QApplication

from ui_elements.micrograph_area import (Micrograph_loader, PLACEHOLDER_IMAGE,
                                         Micrograph_widget) 

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

class test_micrograph_control_buttons(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def setUp(self):
        try:
            self.app = QApplication(sys.argv)
        except RuntimeError:
            pass

    def test_prev_next_buttons_grayed_out_on_empty_init(self):
        '''
        Checks that previous and next buttons on micrograph widget are disabled if
        placeholder image is loaded on empty init
        '''
        l = Micrograph_widget()
        assert len(l.mic_loader.cached_mics) == 1
        self.assertFalse(l.nextButton.isEnabled())
        self.assertFalse(l.previousButton.isEnabled())
        
    def test_prev_next_buttons_grayed_out_on_single_mic_init(self):
        '''
        Checks that previous and next buttons on micrograph widget are disabled if
        a single image is loaded
        '''
        l = Micrograph_widget(os.path.abspath('static/test1.tif'))
        assert len(l.mic_loader.cached_mics) == 1
        self.assertFalse(l.nextButton.isEnabled())
        self.assertFalse(l.previousButton.isEnabled())
        
    def test_prev_next_buttons_are_enabled_on_mic_list_init(self):
        mics = [os.path.abspath('static/test1.tif'),
                os.path.abspath('static/test2.tif')]
        l = Micrograph_widget()
        l.load_new_images(mics)
        assert len(l.mic_loader.cached_mics) == 2
        self.assertTrue(l.nextButton.isEnabled())
        self.assertTrue(l.previousButton.isEnabled())
        
    def test_prev_next_buttons_are_disabled_again_on_mic_reload(self):
        mics = [os.path.abspath('static/test1.tif'),
                os.path.abspath('static/test2.tif')]
        l = Micrograph_widget(mics)
        l.load_new_images([os.path.abspath('static/test1.tif')])
        assert len(l.mic_loader.cached_mics) == 1
        self.assertFalse(l.nextButton.isEnabled())
        self.assertFalse(l.previousButton.isEnabled())
        
        
        
        
    