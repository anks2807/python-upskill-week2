import datetime as dt
import os

#Format the date 2020-02-25 as "Tuesday 25 February 2020"
date_str = "2020-02-25"
date_obj = dt.datetime.strptime(date_str, "%Y-%m-%d")
formatted_date = date_obj.strftime("%A %d %B %Y")
print(formatted_date)

# Calculate the date that is 7 days before 2020-02-25
seven_days_before = date_obj - dt.timedelta(days=7)
print(seven_days_before.strftime("%Y-%m-%d"))

# Convert the date "Feb 25 2020 4:20PM" to the format "2020-02-25 16:20:00"
date_str = "Feb 25 2020 4:20PM"
date_obj = dt.datetime.strptime(date_str, "%b %d %Y %I:%M%p")
formatted_date = date_obj.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)

# Get today's date, tomorrow's date, and yesterday's date
tday = dt.datetime.now()
tomorrow = tday + dt.timedelta(days=1)
yesterday = tday - dt.timedelta(days=1)
print(yesterday)
print(tday)
print(tomorrow)


date_str = "March 22, 2020 10:00AM"
date_obj = dt.datetime.strptime(date_str, "%B %d, %Y %I:%M%p")
formatted_date = date_obj.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)
date_obj = date_obj + dt.timedelta(weeks=1, hours=12)
formatted_date = date_obj.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)



# Get the size of a file in bytes
file_path = "500_lines.txt"
print(f"file size: {os.path.getsize(file_path)}")

# Rename a file from "output.txt" to "new_output.txt"
old_name = "output.txt"
new_name = "new_output.txt"

os.rename(old_name, new_name)