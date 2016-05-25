import feedparser #may need to install feedparser module
from pprint import pprint
from urllib2 import urlopen
from json import load

url = 'http://api.npr.org/query?apiKey='
key = 'get_api_key_from_npr'
url = url + key
url = url + '&format=json&id=1001' #1001 is news id

#open url, load JSON
response = urlopen(url)
json_obj = load(response)


   
#parse story
def getFeed():
    feed = '<h1>News From NPR:<h1>'
    for story in json_obj['list']['story']:
        feed = feed + '<h2><a href=' + story['link'][0]['$text'] + '>' + story['title']['$text'] + '</a></h2> \n <p>' + story['teaser']['$text'] + '</p> \n'
    return feed
    
