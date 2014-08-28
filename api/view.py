
#VIEW
#-display form
#-display received data
class IpView(object):
    def __init__(self):
        #array to hold data from model
        self.__view_array = []
        self.__content = 'test'
    
    def update(self):
        
        self.__content += 'test' + self.__view_array[1]

        
    #getter for content
    @property 
    def content(self):
        return self.__content
    
    #getter for private array
    @property
    def view_array(self):
        pass
    
    #setter for private array
    @view_array.setter
    def view_array(self, arr):
        self.__view_array = arr
        self.update()
