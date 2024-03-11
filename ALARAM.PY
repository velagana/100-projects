#ALARAM CLOCK PROJECT
import datetime
import winsound
import time

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake Up!")
            # Play sound
            winsound.Beep(1000, 2000)  # Frequency and duration of the beep
            break
        time.sleep(1)

def main():
    print("Welcome to the Alarm Clock Program!")
    alarm_hour = int(input("Enter the hour for the alarm (24-hour format, 0-23): "))
    alarm_minute = int(input("Enter the minute for the alarm (0-59): "))
    
    alarm_time = f"{alarm_hour:02d}:{alarm_minute:02d}:00"
    
    print(f"Alarm is set for {alarm_time}")
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()
