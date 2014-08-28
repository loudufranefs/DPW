import urllib2 #importing urllib2 for url_info
import json #parsing json
from controller import IpData #import Controller Class
#MODEL
#-recieve data
class IpModel(object):
    def __init__(self):
        #get values from API url
        #Using new API that allows me to fetch more data.
        # new API is JSON instead of xml - xml was not available for this API
        self.__api_url = "http://ip.pycox.com/json/"
        #holds input value
        self.__ip = ''
        #holds variable for parsing API data
        self.__api_json = ''
        
    def callApi(self):
        #create request using urllib2 library for api url
        api_request = urllib2.Request(self.__api_url+self.__ip)

        #create api object opener
        api_opener = urllib2.build_opener()
        #get info from api url
        api_result = api_opener.open(api_request)
        #Parsing Data
        self._api_json = json.load(api_result)
        
        
        #dictionary object to hold the fetched data
        self.__model_array = dict()
        #accessing controller
        ip_data = IpData()
        #fetching data from API to store in the controller
        ip_data.country = self._api_json['country_name'] #fetch country
        ip_data.region = self._api_json['region_name'] #fetch region
        ip_data.city = self._api_json['city'] #fetch city
        ip_data.zipcode = self._api_json['postal_code'] #fetch zip
        ip_data.timezone = self._api_json['time_zone'] #fetch timezone
        ip_data.lon = self._api_json['longitude'] #fetch longitude
        ip_data.lat = self._api_json['latitude'] #fetch latitude
        ip_data.code = self._api_json['country_code'] #fetch latitude
        ip_data.area_code = self._api_json['area_code'] #fetch latitude

        #filling dictionary with fetched data
        self.__model_array = {'country':ip_data.country, 'region':ip_data.region, 'city':ip_data.city, 'zipcode':ip_data.zipcode, 'timezone':ip_data.timezone, 'lat':ip_data.lat, 'lon':ip_data.lon, 'code':ip_data.code,'area_code':ip_data.area_code}

        

    #getter for ip value
    @property
    def ip(self):
        pass
    
    #setter to change input value
    #this will be used in the GET method and added to the URL parameter
    @ip.setter
    def ip(self, get_value):
        self.__ip = get_value
    
    # getter for array so it can be accessed.
    #this array will pass the data over to the view object
    @property
    def model_array(self):
        return self.__model_array
    
