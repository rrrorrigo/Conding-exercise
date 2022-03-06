"""ioet Position: Python Developer - Coding exercise"""


def hasToPay(text):
    """Method that calculate the amount to paid

    text: the name of an employee and the schedule they worked,
    indicating the time and hours

    return; a tuple of type (name, amount to paid)"""
    days = {
        'MO': 1,
        'TU': 2,
        'WE': 3,
        'TH': 4,
        'FR': 5,
        'SA': 6,
        'SU': 7
    }

    # Dictionary that have the amount to paid with this format
    # 'hour: (weekday, weekend)'
    time = {
        18.01: (20, 25),
        9.01: (15, 20),
        00.01: (25, 30)
    }

    try:
        nameEmployee, weekWorked = text.split('=')
        weekWorked = weekWorked.split(',')

        pay = 0

        for dayWorked in weekWorked:
            numDay = dayWorked[:2]
            timeStart, timeEnd = dayWorked.split('-')
            timeStart = float(timeStart[2:].replace(':', '.'))
            timeEnd = float(timeEnd.replace(':', '.'))
            hoursWorked = timeEnd - timeStart
            for key, value in time.items():
                if timeStart > key:
                    if days[numDay] < 6:
                        pay += value[0] * hoursWorked
                    elif days[numDay] > 5:
                        pay += value[1] * hoursWorked
                    break
        return nameEmployee, pay
    except:
        raise Exception('Please use the format of this example: RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00')
