import threading

class asynchronous():
    def __init__(self, F): 
        self.F = F

    class Future(object):
        def tmp(self, F, *args):
            self.res = F(*args)

        def __init__(self, F, *args):
            self.my_thread = threading.Thread(target=self.tmp, args=[F, *args])
            self.my_thread.start()

        def is_done(self):
            return not self.my_thread.is_alive()
        
        def get_result(self):
            if not self.is_done():
                raise asynchronous.NotYetDoneException("NotYetDoneException")
            return self.res
        
    def start(self, *args):
        return asynchronous.Future(self.F, *args)
    
    class NotYetDoneException(Exception):
        def __init__(self, message):
            self.message = message