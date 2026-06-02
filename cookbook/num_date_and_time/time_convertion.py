'''  
Converting Days to Seconds, And other basic time Conversions

<.>
You have code that needs to perform simple time conversions, like days to seconds,
hours to minutes, and so on.
'''
from datetime import timedelta, datetime 


# a = timedelta(days=2, hours=6)

# b= timedelta(hours=4.5)

# c = a + b
# print(c.days)

# print(c.seconds)

# print(c.seconds / 3600)

# print(c.total_seconds() / 3600)

''' 
If you need to represent specific dates and times, create datetime instances and use the
standard mathematical operations to manipulate them.
'''
a = datetime(2012, 9, 23)

print(a + timedelta(days=10))

b = datetime(2012, 12, 21)
d = b - a
print(d.days)

now = datetime.today()

print(now)


# Determining Last Friday's date 

weekdays = ['Monday','Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday'
            ]

def get_prev_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)


    days_ago = (7 + day_num - day_num_target) % 7 
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date    


datetime.today() 

prev_day = get_prev_byday('Monday')

print(prev_day)

prev_tue = get_prev_byday('Tuesday')
print(prev_tue)

prev_fri = get_prev_byday('Friday')

print(prev_fri)
