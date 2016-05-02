import dailyUpdate
import weather

#Get today's weather (to get forecast, use weather.high(1) for tomorrow (can go up to 10 day forecast).
hiTemp = weather.high(0)
loTemp = weather.low(0)
condition = weather.text(0)

message = "Goodmorning, {name}! The weather today should be " + condition + " with a high of " + hiTemp + " and a low of " + loTemp + "."


rec = raw_input("Who would you like to send the email to?") #delete this
dailyUpdate.sendUpdate(message, rec) #replace rec with your email address.
#sendUpdate takes an optional third argument which specifies a subject line for the email.
#The default subject is "Daily Update"
