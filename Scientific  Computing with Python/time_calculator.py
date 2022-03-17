#Author: Bernardo Calvo

WEEK_DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
HOURS_IDX = 0
MINUTES_IDX = 1
MINS_MAX = 60      #60 mins
HOURS_MAX = 24     #24 hours
PARTDAY_MAX = 12   #12 hours

FORMAT_TIME = "{}:{:02d}"
NEXTDAY = "(next day)"
FORMAT_DAYSLATER = "({} days later)"
AM = "AM"
PM = "PM"

def add_time(start, duration, weekday=""):
  startList = start.split()
  
  st = [int(x) for x in startList[0].split(':')]
  partDay = startList[1]
  du = [int(x) for x in duration.split(':')]

  totalmins = st[MINUTES_IDX] + du[MINUTES_IDX]
  extraHours = int(totalmins/MINS_MAX)
  mins = totalmins%MINS_MAX

  hours = PARTDAY_MAX if partDay == PM else 0        #following this: 1PM = 13h
  totalhours = hours + st[HOURS_IDX] + du[HOURS_IDX] + extraHours
  extraDays = int(totalhours/HOURS_MAX)
  hours = totalhours%HOURS_MAX

  daysLater = ""
  if(extraDays > 0):
    daysLater = " " + (FORMAT_DAYSLATER.format(extraDays) if extraDays > 1 else NEXTDAY)
  
  if hours >= PARTDAY_MAX:
    partDay = PM
    hours = hours%PARTDAY_MAX                      #return to 1PM if 13h 
  else:
  	partDay = AM

  if hours == 0:            #special case: 12PM = 0:00
    hours = 12

  if weekday != "":
    weekday = ", "+ WEEK_DAYS[(WEEK_DAYS.index(weekday.lower())+extraDays)%len(WEEK_DAYS)].capitalize()
    
  return FORMAT_TIME.format(hours, mins) + " " + partDay + weekday + daysLater

print(add_time("11:43 PM", "24:20", "tueSday"))