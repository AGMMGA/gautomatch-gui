# -*- coding: utf-8 -*-

class InvalidParameters(ValueError):
    pass

class gautomatch_runner(object):
    
    def __init__(self):
        super().__init__()
    
    def run(self, exp):
        check = self.check_parameters(exp)
        if check == 1:
            coordinates = self.do_stuff(exp)
            return coordinates
        else:
            raise InvalidParameters(check)
    
    def check_parameters(self):
        '''
        checks that the exp passed to gautomatch are sensible
        returns 1 for success, an error message for failure
        '''
        return 0