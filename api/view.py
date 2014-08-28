#VIEW
#-display form
#-display received data
class IpView(object):
    def __init__(self):
        #array to hold data from model
        self.__view_array = dict()
        self.__content = ''
    
    #function that will be executed when view_array gets values from model
    def update(self):
        #Building html to show the values that were passed from the model
        self.__content += '''
        <div class="resultList">
        <ul>
        '''
        self.__content += '<li>Country: ' + self.__view_array['country'] + '</li>'
        self.__content += '<li>Region: ' + str(self.__view_array['region']) + '</li>'
        self.__content += '<li>City: ' + str(self.__view_array['city']) + '</li>'
        self.__content += '<li>Zip: ' + str(self.__view_array['zipcode']) + '</li>'
        self.__content += '<li>lat: ' + str(self.__view_array['lat']) + '</li>'
        self.__content += '<li>lon: ' + str(self.__view_array['lon']) + '</li>'
        self.__content += '<li>timezone: ' + str(self.__view_array['timezone']) + '</li>'
        self.__content += '<li>code: ' + str(self.__view_array['code']) + '</li>'
        #end list
        self.__content += '</ul>'
        #Generating map from Google API using the values brought in from the IP API
        self.__content += '<div id="map"><img src="http://maps.googleapis.com/maps/api/staticmap?center=' +str(self.__view_array['lat']) + ','+str(self.__view_array['lon'])+'&zoom=12&size=400x400&maptype=roadmap&markers=size:mid%7Ccolor:red%7C'+ str(self.__view_array['city'])+ '" /></div>'
        self.__content += '</div>'

        
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
