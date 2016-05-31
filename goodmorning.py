import dailyUpdate
import weather
import getNPRFeed


#Get today's weather (to get forecast, use weather.high(1) for tomorrow (can go up to 10 day forecast).
hiTemp = weather.high(0)
loTemp = weather.low(0)
condition = weather.text(0)

feed = getNPRFeed.getFeed() #get news feed from NPR

recipients = []

class recipient:
	def __init__(self, n, e):
		self.name = n
		self.email = e
	

JohnDoe = recipient("John", "JohnDoe123@FakeEmail.com")
recipients.append(JohnDoe)



for r in recipients:
	message = "Goodmorning, " +r.name+ "! The weather today should be " + condition + " with a high of " + hiTemp + " and a low of " + loTemp + "."
	message = message + '\n\n' + feed
	print "sending update to: " +r.name+ " at " +r.email+ "."
	dailyUpdate.sendUpdate(message, r.email)
	#sendUpdate takes an optional third argument which specifies a subject line for the email.
	#The default subject is "Daily Update"
