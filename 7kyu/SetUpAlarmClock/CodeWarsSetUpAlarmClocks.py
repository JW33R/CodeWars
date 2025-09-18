from datetime import datetime, timedelta
def setTheAlarmsUp(time, n):
    timeObj = datetime.strptime(time, "%H:%M")
    addTime = [(timeObj + timedelta(minutes=5*_)).strftime("%H:%M") for _ in range(n)]
    return addTime
print(setTheAlarmsUp("8:50", 2))