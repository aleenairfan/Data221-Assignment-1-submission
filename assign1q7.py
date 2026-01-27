# Time Conversion Function

def convertSeconds(secondsSinceMidnight):
    if not isinstance(secondsSinceMidnight, int) or secondsSinceMidnight < 0 or secondsSinceMidnight >= 86400:
        return "Invalid input."

    hours = secondsSinceMidnight // 3600
    minutes = (secondsSinceMidnight % 3600) // 60
    seconds = secondsSinceMidnight % 60

    period = "AM"
    if hours >= 12:
        period = "PM"
    if hours == 0:
        hours = 12
    elif hours > 12:
        hours -= 12

    return f"{hours} {minutes} {seconds} {period}"


# Example test
print(convertSeconds(19067))
