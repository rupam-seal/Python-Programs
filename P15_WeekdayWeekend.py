#check if the given date is a weekday or weekend
from datetime import datetime
week_date = date(2022, 3, 3)
week_date.weekday() <= 4

True

from datetime import datetime
week_date = date(2022, 3, 6)
week_date.weekday() > 4

True