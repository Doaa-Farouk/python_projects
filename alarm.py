import datetime
from playsound import playsound

alarmH = int(input("Hour: "))
alarmM = int(input("Minute: "))
ampm = str(input("am or pm ? "))

print(f"Waiting for alarm: {alarmH}:{alarmM} {ampm} ")
if (ampm == "pm"):
    # time is dispalyed with 24 format
    alarmH += 12

while(True):
    if (alarmH == datetime.datetime.now().hour and alarmM == datetime.datetime.now().minute):
        print("Ringing .... IT IS TIME.")
        playsound("D:\python projects\\nightmour-someone-is-calling-you.mp3")
        break
