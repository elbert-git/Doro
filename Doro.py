from pyfiglet import figlet_format
from CustomModules import Colours
from CustomModules import ClearScreen
import time

ClearScreen.Clear()

#--------functions
def format_seconds(secs):
    #find minutes
    minVal = (secs - (secs % 60)) / 60
    minVal = int(minVal)
    #find seconds
    secondVal = secs % 60
    #return final format
    return str(minVal).zfill(2) + ":" + str(secondVal).zfill(2);


 
while True:
    #-------ask for input
    #ask for input in minutes
    ClearScreen.Clear()
    print(figlet_format("TIME?", justify="center"))
    arg = input("How many Minutes?")

    #-------process input

    #check if number
    try:
        arg = int(arg)
    except:
        print("That's not an integer you baka")
        break

    #Convert to seconds
    seconds = arg * 60

    #-------countdown
    while seconds != 0:
       print(figlet_format(format_seconds(seconds), justify="center"))
       seconds -= 1
       time.sleep(1)
       ClearScreen.Clear()
