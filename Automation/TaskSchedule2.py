import datetime
import schedule
import time

def Schedule_Minute():
    print("Schedular schedules after a minute...")
    print("Current time is : ",datetime.datetime.now())

def Schedule_Hour():
    print("Schedular schedules after a Hour...")
    print("Current time is : ",datetime.datetime.now())

def Schedule_Sunday():
    print("Schedular schedules after each sunday...")
    print("Current time is : ",datetime.datetime.now())



def main():
    print("Automations using Python")

    schedule.every(1).minutes.do(Schedule_Minute)
    schedule.every().hours.do(Schedule_Hour)
    schedule.every().sunday.do(Schedule_Sunday)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()