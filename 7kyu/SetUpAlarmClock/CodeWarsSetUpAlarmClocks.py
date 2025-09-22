#The setTheAlarmsUp function uses the datetime and timedelta module. It first takes the time parameter and changes the string into a datetime object, then takes that object and adds 5 minutes for every time that the user wants with n.
#Then after that, the object is put back into a string and returned.
from datetime import datetime, timedelta
def setTheAlarmsUp(time, n):
    timeObj = datetime.strptime(time, "%H:%M")
    addTime = [(timeObj + timedelta(minutes=5*_)).strftime("%H:%M") for _ in range(n)]
    return addTime

print(setTheAlarmsUp("8:50", 2))
