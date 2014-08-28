#VIEW
#-display form
#-display received data
class IpView(object):
    def __init__(self):
        #array to hold data from model
        self.__view_array = dict()
        self.__content = ''
    
    def update(self):
        self.__content += 'Country: ' + self.__view_array['country']
        self.__content += '<br>Region: ' + str(self.__view_array['region'])
        self.__content += '<br>City: ' + str(self.__view_array['city'])
        self.__content += '<br>Zip: ' + str(self.__view_array['zipcode'])
        self.__content += '<br>lat: ' + str(self.__view_array['lat'])
        self.__content += '<br>lon: ' + str(self.__view_array['lon'])
        self.__content += '<br>timezone: ' + str(self.__view_array['timezone'])
        #html for map
        self.__content += '<div id="map"><img src="http://maps.googleapis.com/maps/api/staticmap?center=' +str(self.__view_array['lat']) + ','+str(self.__view_array['lon'])+'&zoom=12&size=400x400&maptype=roadmap&markers=size:mid%7Ccolor:red%7C'+ str(self.__view_array['city'])+ '" /></div>'

        
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
