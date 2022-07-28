def add_time(start, duration, day=None):
    
    # We check the 'day' argument
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days_count = 0
    final_day = 0
    if day != None:
        final_day = int(days.index(day.title()))

    # We deconstruct the 'start' argument and convert the time to 24-hour format
    time1 = start.split(' ')[0]
    hours1 = int(time1.split(':')[0])
    minutes1 = int(time1.split(':')[1])
    am_or_pm = start.split(' ')[1].upper()
    if am_or_pm == 'PM':
        hours1 += 12
    
    # We deconstruct the 'duration' argument
    hours2 = int(duration.split(':')[0])
    minutes2 = int(duration.split(':')[1])
    
    # We calcule the new time
    new_hours = hours1 + hours2
    new_minutes = minutes1 + minutes2
    if new_minutes >= 60:
        new_minutes -= 60
        new_hours += 1
    if new_minutes < 10:
        new_minutes = f'0{new_minutes}'
    while new_hours >= 24:
            days_count += 1
            new_hours -= 24
    if new_hours > 13:
        new_hours -=12
        am_or_pm = 'PM'
    elif new_hours < 1:
        new_hours += 12
        am_or_pm = 'AM'
    elif hours1 < 12 and new_hours == 12 and days_count == 0:
        am_or_pm = 'PM'
    else:
        am_or_pm = 'AM'
            
    new_time = f'{new_hours}:{new_minutes} {am_or_pm}'

    # We calculate the new day
    if day != None:
        final_day += days_count
        while final_day >= 7:
            final_day -= 7
        new_time += f', {days[final_day]}'
    
    if days_count == 1:
        new_time += f' (next day)'
    if days_count > 1:
        new_time += f' ({days_count} days later)'
    
    return new_time