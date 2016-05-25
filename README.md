# DailyUpdate

Python program for Raspberry Pi that sends an email every morning with the weather for that day and the top NPR news stories.

I have included in this repo the necessary oauth2 module.

Goodmorning.py is the file which actually sends the email to all desired recipients. The program grabs the days weather from the included weather module. Weather forecast can be added by including additional calls to weather, increasing the day value in each call (i.e. hiTemp=weather.high(1) will get the forecasted high temperature for tomorrow). The news feed is grabbed from the included getNPRFeed module. Inside this file is a list of recipients and a constructor to make new recipients. An example is included which show how to create a new recipient and add them to the list. Finally the email with the weather and news is sent to each recipient in the list.

Weather.py gets weather data from Yahoo weather. By default the weather module gets weather data for Boston, but this can be changed by editing the woeid in the url. The response from the weather api is converted to json and the 10 day forecast is extracted. The module includes methods to get the weather code, condition, high and low temps, date, and day of the week for each of the ten days in the forecast.

GetNPRFeed.py uses NPR's API to access its news feed. To use this module you must register an API key with NPR. By default the module gets the top stories from the News category (id=1001). The getFeed method goes through every story in the feed and grabs the title and subtitle ('teaser') and converts it to an HTML format. 

DailyUpdate.py is the module used to connect with gmail and authorize the app to send emails from your Gmail account. This uses oauth2 authorization so there is no need to enable less secure apps in your google account. To use this with your Gmail account you must go to the Google Developer console and register the app and receive credentials for it. An example credentials json file is included in this repo. The program goes through the credentials and make the correct calls to Google to authorize the app to send emails. When supplied with a message, and recipient, and optionally a subject, the sendUpdate method will send the specified email.

#NOTE: Go here to learn how to create the necessary tokens to use oauth2 authentication!
https://github.com/google/gmail-oauth2-tools/wiki/OAuth2DotPyRunThrough

Features to add:
  - Improve style of email
  - end email with daily quote
