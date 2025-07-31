def add_time(start, duration, start_day=None):  # start is in format "HH:MM AM/PM", duration is in format "HH:MM"

    # Parse start time
    time, period = start.split() # Split start time into time and period
    hour, minute = map(int, time.split(':')) # Split time into hour and minute

    # Convert start time to 24-hour format
    if period == 'PM' and hour != 12: 
        hour += 12
    if period == 'AM' and hour == 12: 
        hour = 0

    # Parse duration
    dur_hours, dur_minutes = map(int, duration.split(':')) # Split duration into hours and minutes

    # Add minutes and calculate new minutes and hour carry
    total_minutes = minute + dur_minutes 
    extra_hours = total_minutes // 60 
    new_minutes = total_minutes % 60

    # Add total hours
    total_hours = hour + dur_hours + extra_hours

    # Calculate final hour in 12-hour format
    new_hour_24 = total_hours % 24
    new_hour_12 = new_hour_24 % 12
    if new_hour_12 == 0:
        new_hour_12 = 12

    # Determine new AM/PM
    if new_hour_24 >= 12: # If new hour is after noon, it's PM
        new_period = 'PM' 
    else: # If new hour is before noon, it's AM
        new_period = 'AM'

    # Calculate how many days later
    days_later = total_hours // 24 

    # Day of week logic
    if start_day:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_index = days.index(start_day.capitalize()) # Get index of start day
        new_day = days[(day_index + days_later) % 7] # Get new day of week
        day_text = f", {new_day}" # Add new day of week to text

    else: # If start_day is not provided, use today's day of week
        day_text = ""

    # Days later text
    if days_later == 0: # If days_later is 0, there is no text
        later_text = ""
    elif days_later == 1: # If days_later is 1, there is 1 day later text
        later_text = " (next day)"
    else: # If days_later is more than 1, there is more than 1 day later text
        later_text = f" ({days_later} days later)"

    # Final formatted time
    new_time = f"{new_hour_12}:{new_minutes:02d} {new_period}{day_text}{later_text}"
    return new_time

print(add_time('11:59 PM', '24:05', 'Wednesday'))
