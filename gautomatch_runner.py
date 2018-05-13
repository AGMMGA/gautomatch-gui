# -*- coding: utf-8 -*-
import os
import glob

class InvalidParameter(Exception):

    def __init__(self, msg, informative_text=None, window_title='Alert'):
        self.informative_text = informative_text
        self.msg = msg
        self.window_title = window_title
        
    def __str__(self):
        return self.msg
    
class MicrographNotFound(InvalidParameter):
    pass

class TemplateNotFound(InvalidParameter):
    pass

class NoMicrographsChosen(InvalidParameter):
    pass

class Gautomatch_runner(object):
    
    def __init__(self):
        super().__init__()
    
    def run(self, parameters):
        self.check_parameters(parameters) #raises appropriate exceptions
        coordinates = self.do_stuff(parameters)
        return coordinates
    
    def check_parameters(self, parameters):
        '''
        checks that the exp passed to gautomatch are sensible
        returns 1 for success, an error message for failure
        '''
        #check micrographs are given as input
        if not parameters['micrographs']:
            msg = 'No micrographs selected'
            t = 'Please select one or more micrographs to process'
            window_title = 'File not found'
            raise NoMicrographsChosen(msg, 
                                      informative_text=t,
                                      window_title=window_title)
        #check micrographs exists
        if not glob.glob(parameters['micrographs']):
            msg = ('The micrograph\n {}\ndoes not exist'.format(
                                                    parameters['micrographs']))
            window_title = 'File not found'
            raise MicrographNotFound(msg, window_title=window_title)
        #check templates exist if given as input
        if parameters['templates'] and not glob.glob(parameters['templates']):
            msg = ('The template\n {}\ndoes not exist'.format(
                                                    parameters['templates']))
            window_title = 'File not found'
            raise TemplateNotFound(msg, window_title=window_title)
        #apixM, apixT are >0 and type == float from GUI specifications
        #diameter is >0 and type == int from GUI specifications
        return 1
        
    def do_stuff(self, parameters):
        pass
    
def main():
    a = Gautomatch_runner()
    import inspect
    test_file = inspect.getfile(os)
    parameters = {'micrographs': test_file,
                    'templates':'dsv',}
    a.run(parameters)

if __name__ == '__main__':
    main()