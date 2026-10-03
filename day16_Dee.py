from datetime import datetime


now = datetime.now()
print("Current day:", now.day)
print("Current month:", now.month)
print("Current year:", now.year)
print("Current hour:", now.hour)
print("Current minute:", now.minute)
print("Timestamp:", now.timestamp())

formatted_now = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted date:", formatted_now)

today = datetime.strptime("December 5, 2019", "%B %d, %Y")
time_string = today.strftime("%m/%d/%Y, %H:%M:%S")
time_value = datetime.strptime(time_string, "%m/%d/%Y, %H:%M:%S")
print("Converted time:", time_value)

new_year = datetime(time_value.year + 1, 1, 1)
print("Time until New Year:", new_year - time_value)

unix_epoch = datetime(1970, 1, 1)
print("Time since 1 January 1970:", now - unix_epoch)

