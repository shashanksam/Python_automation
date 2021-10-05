#call this function by py change.py datalines

import re
import sys


datas=sys.argv[1]
values=[]
with open(datas) as f:
    for data in f:
        data = data.encode("ascii", "ignore").decode()
        data=re.sub('\s+',' ',data)
        pattern=r"^([\w]*[\d]*) current_date [-– ]* ([\d]*) days ([\w ]*) (\d*)$"
        insertis=r"INSERT INTO coupon_details VALUES('\1',date_sub(curdate(),interval \2 day),'\3',\4),"
        values.append(re.sub(pattern,insertis, data))

with open("newdata.txt", "w") as file:
    for value in values:
        file.write(value)
        
        
        """WELCOME20 	current_date –  7 days 	Welcome offer 	20
SEASONAL15 	current_date – 1 days 	Seasonal offer 	15
HAPPY30 	current_date  	Happy hours offer 	30
DHAMAKA20 	current_date + 31 days 	Marching it offer 	20"""
"""INSERT INTO coupon_details
VALUES('WELCOME20',date_sub(curdate(),interval 7 day),'Welcome offer',20);"""
