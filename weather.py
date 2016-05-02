import requests

#request the full weather data for {Boston} (woeid=2367105) from Yahoo weather.                                    {woeid}
r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid=2367105&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys')

j = r.json() #convert the response to a json format


#grab the 10 day forecast
forecast = j['query']["results"]['channel']['item']['forecast']

def code(day):
    return(forecast[day]['code'])
    #gets the code to display a weather condition image

def text(day):
    return(forecast[day]['text'])
    #gets the weather condition for the given day

def high(day):
    return(forecast[day]['high'])
    #gets the high temp for the day

def low(day):
    return (forecast[day]['low'])
    #gets the low temp for the day

def date(day):
    return (forecast[day]['date'])
    #returns the calendar date (e.g. '27 Apr 2016')

def day(day):
    return (forecast[day]['day'])
    #returns the day of the week
