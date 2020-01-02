# Given two calendar and two daily bounds and a meeting duration.
# Return a list of availabilities during which we can schedule our meeting.

employee_1 = [("9:00", "10:30"), ("12:00", "13:00"), ("16:00", "18:00")]
employee_1_office_hours = ("9:00", "20:00")

employee_2 = [("10:30", "11:30"), ("12:30", "14:30"), ("14:30", "15:00"), ("16:00", "17:00")]
employee_2_office_hours = ("10:00", "18:30")

meeting_duration = "0:30"

def meeting(cal1, cal2, office_hour1, office_hour2, duration):
    calendar = merge_calendar(cal1, cal2)
    office_hours = (max(office_hour1[0], office_hour2[0]), min(office_hour1[1], office_hour2[1]))
    available_hours = []
    for i in range(len(calendar) - 1):
        t1 = convert_to_min(calendar[i][1])
        t2 = convert_to_min(calendar[i + 1][0])
        if t1 < t2 and t2 - t1 >= duration:
            available_hours.append((calendar[i][1], calendar[i + 1][0]))

    # Office hours start to first event
    t0_office = convert_to_min(office_hours[0])
    t0_calendar = convert_to_min(calendar[0][0])
    if t0_office < t0_calendar and t0_calendar - t0_office >= duration:
        available_hours.append((office_hours[0], calendar[0][0]))
    # Office hours end to end office hour
    t_last_office = convert_to_min(office_hours[1])
    t_last_calendar = convert_to_min(calendar[-1][1])
    if t_last_calendar < t_last_office and t_last_office - t_last_calendar >= duration:
        available_hours.append((calendar[-1][1], office_hours[1]))
    return available_hours

# Convert time to min
def convert_to_min(t):
    t = list(map(int, t.split(":")))
    return t[0] * 60 + t[1]

# Merge two calendar
def merge_calendar(cal1, cal2):
    calendar = []
    i = 0
    j = 0
    while i < len(cal1) and j < len(cal2):
        t1 = convert_to_min(cal1[i][0])
        t2 = convert_to_min(cal2[j][0])
        if t1 < t2:
            calendar.append(cal1[i])
            i += 1
        else:
            calendar.append(cal2[j])
            j += 1
    if i != len(cal1):
        calendar += cal1[i:]
    if j != len(cal2):
        calendar += cal2[j:]
    return calendar


print(meeting(employee_1, employee_2, employee_1_office_hours, employee_2_office_hours, 30))
