import datetime
import time
import winsound
def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            winsound.Beep(1000, 1000)
            break
        else:
            time.sleep(1)
def main():
    print("Alarm Clock!")
    print("Please enter the alarm time (in HH:MM:SS format):")
    alarm_time = input()
    set_alarm(alarm_time)
if __name__ == "__main__":
    main()