#MODEL
#-recieve data
class IpModel(object):
    def __init__(self):
        #get values from API url
        #Using new API that allows me to fetch more data.
        # new API is JSON instead of xml - xml was not available for this API
        self.__api_url = "http://www.telize.com/geoip/"
        #holds input value
        self.__ip = '208.80.152.201'
        #holds variable for parsing API data
        self.__api_json = ''
        
    def callApi(self):
        #create request using urllib2 library for api url
        api_request = urllib2.Request(api_url+self.__ip)
        #create api object opener
        api_opener = urllib2.build_opener()
        #get info from api url
        api_result = api_opener.open(api_request)

        #Parsing Data
        self.__api_json = json.load(api_result)
        
        #fetching data from API to store in the controlelr
        ip_data = IpData()
        ip_data.country = api_json['country'] #fetch country
        ip_data.state = api_json['region'] #fetch region
        ip_data.city = api_json['city'] #fetch city
        ip_data.zipcode = api_json['postal_code'] #fetch zip
        ip_data.timezone = api_json['timezone'] #fetch timezone
        ip_data.lan = api_json['longitude'] #fetch longitude
        ip_data.lon = api_json['latitude'] #fetch latitude
    
    #getter for ip value
    @property
    def ip(self):
        pass
    
    #setter to change input value
    @ip.setter
    def ip(self, input_value):
        self.__ip = input_value