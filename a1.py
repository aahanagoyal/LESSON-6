from datetime import date,time,datetime

today=date.today()
print("Today's date is " ,today)
print("Date components:",today.day,"/",today.month,"/",today.year)
now=datetime.now()
print("Current time and date is: ",now)