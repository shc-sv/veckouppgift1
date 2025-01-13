# Veckouppgift 1 by Shu-Hui Chen 2025-01-10
# Q4: 1a, 1b, 1c, 2, 3a, 3b
import math
from datetime import datetime, timedelta

def q4_1a_1b_1c():
    # 1a:
    print("Det är ca 470 km mellan Stockholm och Göteborg. Nu vill vi räkna ut hur lång tid det ska ta!")
    drive_distance = 470
    drive_speed = input("Ange här hur fort man ska köra i km/h: ")
    try:
        drive_speed = int(drive_speed)

        #Vi convert km/h to m/s by dividing with 3.6
        drive_speed = int(drive_speed / 3.6)
        print(f'Vi omvandlar km/h till m/s, så blir hastigheten: {drive_speed} (m/s)')

        drive_time_second = int(drive_distance * 1000 / drive_speed)
        print(f'1a. Man behöver {drive_time_second} sekunder att köra från Stockholm till Göteborg.')

        # 1b
        drive_time_minute = int(drive_distance * 1000 / drive_speed /60)
        print(f'1b. Man behöver {drive_time_minute} minuter att köra från Stockholm till Göteborg.')

        # 1c
        drive_time_hour = drive_time_second // 3600
        drive_time_minute = int ((drive_time_second % 3600) /60)
        print(f'1c. Man behöver {drive_time_hour} timmar och {drive_time_minute} minuter att köra från Stockholm till Göteborg.')
    except ValueError:
        print(f"{drive_speed} är inte ett heltal.")

def q4_2():
    # 2
    print("2. Här räknar vi ut längden på hypotenusan i en rätvinklig triangel.")
    side1_length = input("Ange här längden på en av de två kortare sidorna: ")
    side2_length = input("Ange här längden på den andra av de två kortare sidorna: ")
    try:
        side1_length = int(side1_length)
        side2_length = int(side2_length)

        side1_length = math.pow(side1_length, 2)
        side2_length = math.pow(side2_length, 2)

        square_root = format(math.sqrt(side1_length + side2_length), ".2f")
        print(f"längden på hypotenusan är {square_root }")
    except ValueError:
        print(f"{side_length} är inte ett heltal.")


def q4_3a_3b():
    # 3a
    date_now = datetime.now().date()
    print(f'3a. Dagens datum är {date_now}.')

    #3b
    # List of month name
    month_names = [
        'Januari', 'Februari', 'Mars', 'April', 'Maj', 'Juni',
        'Juli', 'Augusti', 'September', 'Oktober', 'November', 'December'
    ]

    date_after_7_days = date_now + timedelta(days = 7)
    month_name = month_names[date_after_7_days.month - 1]

    print(f'3b. Om 7 dagar är datumet {date_after_7_days} eller den {date_after_7_days.day} { month_name} {date_after_7_days.year}.')



