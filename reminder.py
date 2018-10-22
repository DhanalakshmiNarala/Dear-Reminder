__author__ = "Dhanalakshmi Narala"

""""""

import sys
import time
from datetime import datetime
from win10toast import ToastNotifier


def read_file(file):
    events = {}
    with open(file, "r") as f:
        for event in f:
            event = event.split()
            events[tuple(event[:5])] = " ".join(event[5:])
    return events

def check_events(events):
    now = datetime.now().strftime("%Y %m %d %I:%M %p")
    for event in events:
        event_time = " ".join(event)
        if event_time == now:
            send_notification("Notification", events[event])
            break

def send_notification(title,msg):
    toaster = ToastNotifier()
    toaster.show_toast(title, msg, duration=10)

def main():
    while True:
        events = read_file(r"C:\Dear Reminder\reminder.txt")
        check_events(events)
        time.sleep(60)

if __name__ == "__main__":
    sys.exit(main())