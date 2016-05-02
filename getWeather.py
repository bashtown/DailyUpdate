import weather



for i in range(10): #cannot get forecast more than 10 days out
    print 'code: ', weather.code(i)
    print 'day: ', weather.day(i)
