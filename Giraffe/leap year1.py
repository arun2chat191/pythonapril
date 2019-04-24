month_days=[0,31,28,30,31,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year%4==0 and (year%100!=0 or year%400==0)

def days_in_month(year,month):

    if not 1<=month<=12:
        return 'Invalid Month'
    if  is_leap(year) and month==2:
          return 29


    return month_days[month]
print(is_leap(200))

print(days_in_month(2200,2))