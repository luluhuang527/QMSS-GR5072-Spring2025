
import datetime 

def get_age(yyyy:int, mm:int, dd:int) -> int:
    dob = datetime.date(yyyy, mm, dd)
    today = datetime.date.today()
    age = round((today - dob).days / 365.25)
    return age

# # Quick function test
# get_age(1980, 1, 23)
# get_age(2000, 1, 25)
# get_age(2000, 7, 4)
# get_age(2000, 12, 4)


# # Practice with the datetime class !
# x = datetime.date(2000, 3, 5)
# y = datetime.date(2000, 3, 6)
# z = datetime.date(2001, 3, 5)

# x - y
# (x - y).days
# x - z
# (x - z).days / 365.25
# round((x - z).days / 365.25)

t = 2
