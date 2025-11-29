normal_format = input("Enter time (24-hour format): ")
splitted = normal_format.split(':')

hours = int(splitted[0])
minutes = int(splitted[1])
smth = "am"

if hours >= 12 and hours <= 23:
    hours -= 12
    smth = "pm"
elif hours == 0:
    hours = 12

print(f'The time is {hours}:{minutes:02d} {smth}')
