#!/usr/bin/python
from datetime import datetime, timedelta

count = 10
for day in range(count):
    print (datetime.now() + timedelta(days=-day)).strftime('%Y-%m-%d')
