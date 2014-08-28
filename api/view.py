#VIEW
#-display form
#-display received data
class IpView(object):
    def __init__(self):
        #array to hold data from model
        self.__view_array = []
        self.__content = 'test'
    
    def update(self):
        for do in self.__view_array:
            self.__content += do.country
            
    
    
    #getter for private array
    @property 
    def view_array(self):
        pass
    
    #setter for private array
    @view_array.setter
    def view_array(self, arr):
        self.__view_array = arr
