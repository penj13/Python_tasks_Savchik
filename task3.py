from datetime import datetime
d1 = datetime.strptime('1/1/2020', '%m/%d/%Y')
d2 = datetime.strptime('12/2/2019', '%m/%d/%Y')
def dayscount (d1, d2):
    n_days = abs((d2 - d1).days)
    return n_days
dayscount (d1, d2)
