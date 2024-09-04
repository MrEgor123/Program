from datetime import date, datetime

def calculate_birthday_countdown(birthday_str):
    today = date.today()
    birthday = birthday_str
    
    this_year_birthday = get_birthday_for_year(birthday, today.year)

    if this_year_birthday < today:
        # ...то следующий ДР будет в следующем году.
        next_birthday = get_birthday_for_year(birthday, today.year + 1)
    else:
        next_birthday = this_year_birthday

    birthday_countdown = (next_birthday - today).days
    return birthday_countdown


def get_birthday_for_year(birthday, year):
    """
    Получает дату дня рождения для конкретного года.

    Ошибка ValueError возможна только в случае
    с високосными годами и ДР 29 февраля.
    В этом случае приравниваем дату ДР к 1 марта.
    """
    try:
        calculated_birthday = birthday.replace(year=year)
    except ValueError:
        calculated_birthday = date(year=year, month=3, day=1)
    return calculated_birthday
