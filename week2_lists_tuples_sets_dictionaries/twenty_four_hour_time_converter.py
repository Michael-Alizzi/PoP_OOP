from datetime import datetime
import time

time = input("What is the time? ")

time_list = list(time)

selected_hours = time_list[0]+time_list[1]

selected_minutes = time_list[2]+time_list[3]

if selected_hours == "24":
    selected_hours = "00"
    
dt = datetime(
    year = 1968, month = 6, day = 24,
    hour = int(selected_hours), minute = int(selected_minutes)
)
print(f"{time} is {dt.strftime('%I:%M %p')}")

