import random
import time

def getRandomDate(s,e):
    print("Printing random date between",s,"and",e)
    randomGenerator=random.random()
    dateFormat = '%m/%d/%Y'
    SDate=time.mktime(time.strptime(s, dateFormat))
    EDate=time.mktime(time.strptime(e, dateFormat))
    randomTime= SDate + randomGenerator * (EDate - SDate)
    randomDate=time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print("Random Date=", getRandomDate("01/01/2026","12/01/2026"))
