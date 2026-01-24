"""
Ref: https://medium.com/@nishi.paul.in/datetime-in-python-all-in-one-c66bfef006d9
"""

from datetime import datetime

print(datetime.now())

# display datetime in format
print(datetime.now().strftime("%Y-%m-%d %H-%M-%S"))

# today day name is %A
print(datetime.today().strftime("%A"))

# initialize datetime
dt = datetime.strptime("2026-01-14 22:23:10", "%Y-%m-%d %H:%M:%S")
dt2 = datetime.strptime("2026-01-16 07:12:45", "%Y-%m-%d %H:%M:%S")
diff = dt2 - dt

# Total duration combined days, minutes and seconds
print("Just diff seconds", diff.seconds)
print("Total Diff Duration", diff.total_seconds())

print()
# print(datetime.strptime(str(diff), "%H:%M:%S"))
