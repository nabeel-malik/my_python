"""
Dates, times, datetimes, timezones, time deltas.

Naive datetimes: Unaware of timezones and daylight savings time (DST)
Aware datetimes: Have enough information to determine their timezones (tz) and DST
"""

import datetime
import pytz         # used later (in section 6.) for tz aware dates

print('\n############################ 1. NAIVE DATES - datetime.date ############################\n')
'''
With datetime.date, we are only working with: YEAR, MONTH and DAY.
'''
# create a NAIVE dates
d = datetime.date(2020, 9, 15)          # pass regular integers, with no leading zeroes
print(type(d))
print(d)

tday = datetime.date.today()
print(tday)
print(tday.day)
print(tday.month)
print(tday.year)

print(tday.weekday())                   # Monday: 0, Sunday: 6
print(tday.isoweekday())                # Monday: 1, Sunday: 7

print('\n######################### 2. TIME DELTA - datetime.timedelta #########################\n')

# date +/- timedelta = date
tdelta = datetime.timedelta(days=7)
print(type(tdelta))
print(tday + tdelta)

# date - date = timedelta (+ operator is not supported between two date objects)
print(tday - d)

# how many days are left till my next birthday
bday = datetime.date(2021, 1, 25)
print(bday - tday)                                                                      # birthday - today
print(type(bday-tday))
print(f"{(bday - tday).days} days left till your next birthday!")                       # timedelta.days attribute
print(f"{(bday - tday).total_seconds()} seconds left till your next birthday!")         # timedelta.total_seconds()

print('\n############################ 3. NAIVE TIME - datetime.time ############################\n')
'''
With datetime.date, we are only working with: YEAR, MONTH and DAY.
With datetime.time, we are working with: HOURS, MINUTES, SECONDS and MICROSECONDS.
'''

# create NAIVE time
t = datetime.time(9, 30, 45, 100000)            # hours, mintues, seconds and microseconds
print(type(t))
print(t)
print(t.hour)

print('\n######################### 4. NAIVE DATETIME - datetime.datetime #########################\n')
'''
With datetime.datetime, we are working with: YEAR, MONTH, DAY, HOURS, MINUTES, SECONDS and MICROSECONDS.
'''
dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)     # year, month, day, hour, minute, seconds, microseconds
print(type(dt))
print(dt)
print(dt.date())                # datetime.date() method
print(dt.time())                # datetime.time() method
print(dt.day)
print(dt.minute)

# timedeltas work similarly with datetime
tdelta = datetime.timedelta(hours=12)
print(dt + tdelta)

print('\n######################### 5. ALTERNATIVE CONSTRUCTORS FOR DATETIME #########################\n')

# there are 3 alternative constructors for datetime
dt_today = datetime.datetime.today()        # returns current local datetime, with timezone (tz) of None.
dt_now = datetime.datetime.now()            # similar to today(), but gives us the option to pass in a tz.
dt_utcnow = datetime.datetime.utcnow()      # gives current UTC time, but tz is still None

print(dt_today)
print(dt_now)
print(dt_utcnow)

'''
Therefore none of the above 3 variables are tz aware datetimes. In section 8, we will see how to make these NAIVE
datetimes AWARE.
'''

print('\n######################### 6. AWARE DATETIME & pytz PACKAGE #########################\n')
'''
pytz is a third-party package that you have to install for tz aware datetimes. Although this is a third-party package, 
even in the Python docs, they recommend pytz for tz aware datetime.

In the documentation for pytz, it is recommended to always work with UTC when dealing with timezones. There are a lot
of good reasons for this, that we will not go into here.
'''

# create AWARE datetime by passing tzinfo argument
dt = datetime.datetime(2015, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

# get current UTC time that is also tz aware using datetime.now() --> Corey's preferred method
dt_now_utc = datetime.datetime.now(tz=pytz.UTC)
print(dt_now_utc)

# get current UTC time that is also tz aware using datetime.utcnow() --> Less preferred method
dt_utcnow_utc = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

print('\n########### 7. SWITCHING BETWEEN TIMEZONES IN AWARE datetimes - .astimezone() metod ###########\n')

# create aware datetime with UTC
dt_utc = datetime.datetime.now(tz=pytz.UTC)
print(dt_utc)

# convert UTC to Mountain
dt_mtn = dt_utc.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

# view all available tzs in pytz
# for tz in pytz.all_timezones:
#     print(tz)

print('\n############# 8. CONVERT NAIVE datetime TO AWARE datetime - .localize() method #############\n')

'''
Now let's say that our local timezone on 'US/Mountain', and we want to do the following:
1. Create a NAIVE local datetime
2. Make the NAIVE local datetime, AWARE (with the local timezone, i.e. US/Mountain) --> .localize() method
3. Convert the AWARE datetime from 'US/Mountain' to 'US/Eastern' tz.

'''

# 1. Create a NAIVE local datetime
dt_mtn = datetime.datetime.now()
print(dt_mtn)

'''
Now, since the datetime created above is NAIVE, we can not convert the above datetime to US/Mountain tz directly. 
'''

# 2. Make the NAIVE local datetime, AWARE (with the local timezone, i.e. US/Mountain) --> .localize() method
dt_mtn = pytz.timezone('US/Mountain').localize(dt_mtn)

# 3. Convert the AWARE datetime from 'US/Mountain' to 'US/Eastern' tz.
dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)

print('\n################ 9. Convert datetime to string - .strftime() method ################\n')

# Let's create AWARE local (US/Mountain) current datetime
dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))

# One international standard to display dates and times is ISO format - .isoformat() method
print(dt_mtn.isoformat())

'''
To convert datetime to a string in a specific format, check the following link:
https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes 
'''

# print date in a desired string format
print(dt_mtn.strftime('%B %d, %Y'))

print('\n################ 10. Convert string to datetime - .strptime() method ################\n')

dt_str = 'October 04, 2020'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)












