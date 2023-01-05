import time
from datetime import datetime
import time
import requests as requests

from_date = input("Enter start date in yyyy/mm/dd format: ")
to_date = input("Enter end date in yyyy/mm/dd format: ")

#Convert date to datetime object format
from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

# Convert date to ml second format
from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))


url = f'https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1={from_epoch}&period2={to_epoch}&interval=1d' \
      '&events=history&includeAdjustedClose=true'
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 "
                         "Safari/537.36"}
# Method get accepts the current url for extract information, headers using for cancel website safety
# We use content instead text because we can use numeric and non-numeric values
content = requests.get(url, headers=headers).content

# Best practice is using 'wb' instead 'w' because wb can write text and not text value
with open('data.csv', 'wb') as file:
    file.write(content)