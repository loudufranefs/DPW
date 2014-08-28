#VIEW object will handle showing results
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
        
        #using another API to fetch flag image based on country code
        #the value needs to be converted to lowercase to work properly
        self.__content += '<li><img src="http://flagpedia.net/data/flags/mini/' + str(self.__view_array['code']).lower() + '.png" /> The IP you entered is in the ' + self.__view_array['country'] + '</li>'
        self.__content += '<li>City: ' + str(self.__view_array['city']) + '</li>'
        self.__content += '<li>Zip Code: ' + str(self.__view_array['zipcode']) + '</li>'
        self.__content += '<li>State/Region: ' + str(self.__view_array['region']) + '</li>'
        self.__content += '<li>Latitude and Longitude: ( ' + str(self.__view_array['lat']) + ' , '+ str(self.__view_array['lon']) + ' ) </li>'
        self.__content += '<li>Timezone: ' + str(self.__view_array['timezone']) + '</li>'
        self.__content += '<li>Area Code: ' + str(self.__view_array['area_code']) + '</li>'
        #end list
        self.__content += '</ul>'
        #Generating map from Google API using the values brought in from the IP API
        self.__content += '<div id="map"><img src="http://maps.googleapis.com/maps/api/staticmap?center=' +str(self.__view_array['lat']) + ','+str(self.__view_array['lon'])+'&zoom=12&size=400x300&maptype=roadmap&markers=size:mid%7Ccolor:red%7C'+ str(self.__view_array['city'])+ '" /></div>'
        self.__content += '</div>'
    
        #add footer
        self.__content += '''
        <div id="credits">
        Thank you for using this web app.
        
        This app is using <a href="http://ip.pycox.com/json/">PyCox</a> API to fetch IP data, <a href="https://developers.google.com/maps/">Google Maps API</a> for the map, and <a href="http://flagpedia.net">Flagpedia</a> to fetch the country flag.
        </div>
        
        '''

        
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
