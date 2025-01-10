# Vecouppgift 1
# Q4: 1a, 1b, 1c

def q4_1a_1b_1c():

    # 1a:
    print("Det är ca 470 km mellan Stockholm och Göteborg. Nu vill vi räkna ut hur lång tid det.")
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
        # Heltalsdivision för att få timmar
        drive_time_hour = drive_time_second // 3600
        drive_time_minute = int ((drive_time_second % 3600) /60)
        print(f'1c. Man behöver {drive_time_hour} timmar och {drive_time_minute} minuter att köra från Stockholm till Göteborg.')
    except ValueError:
        print(f"{drive_speed} är inte ett heltal.")