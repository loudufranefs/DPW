#MODEL
#-recieve data
class IpModel(object):
    def __init__(self):
        pass
    
        #proof of concept code
        
        #get values from API url
        #I am using another API, still the same concept as the proof of concept
        #however this API allows me to get at least 6 pieces of information
        #where as the first API I used only had 5 relevant pieces of data.
        
        '''
        api_url = "http://ip-api.com/xml/208.80.152.201"
        #create request using urllib2 library for api url
        api_request = urllib2.Request(api_url)
        #create api object opener
        api_opener = urllib2.build_opener()
        #get info from api url
        api_result = api_opener.open(api_request)
        #use minidom to parse xml
        apixml = minidom.parse(api_result)
        
        #setting up variables for return values temporarily
        timezone = apixml.getElementsByTagName('timezone')[0].firstChild.nodeValue
        lon = apixml.getElementsByTagName('lon')[0].firstChild.nodeValue
        lat = apixml.getElementsByTagName('lat')[0].firstChild.nodeValue
        zipcode = apixml.getElementsByTagName('zip')[0].firstChild.nodeValue
        city = apixml.getElementsByTagName('city')[0].firstChild.nodeValue
        country = apixml.getElementsByTagName('country')[0].firstChild.nodeValue
        '''