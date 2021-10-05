import re
import sys
datas=sys.argv[1]
values=[]
with open(datas) as f:
    for data in f:
        data = data.encode("ascii", "ignore").decode()
        data=re.sub('\s+',' ',data)
        #    1001 	Alex 	9900990091 	 USM101AL 	current_date - 750 days 	4.3
        #     1      2       3             4                  5   6           7
        #pattern=r"^([\w][\d]) current_date [-– ]* ([\d]) days ([\w ]) (\d*)$"
        pattern=r"^(\d{4}) (\w*) (\d*) (US[\w]\d{3}\w\w) current_date([\+\- ]*)(\d*) ?(days)? ([\d\.]*)$"
        interval=re.sub(pattern, r"\5",data).strip()
        print(interval) 
        if(interval=='-'):
            insertis=r"INSERT INTO driver_details VALUES(\1,'\2',\3,'\4', date_sub(curdate(),interval \6 day), '\8');"
        elif(interval=='+'):
            insertis=r"INSERT INTO driver_details VALUES(\1,'\2',\3,'\4', date_sub(curdate(),interval -\6 day), '\8');"
        else:
            insertis=r"INSERT INTO driver_details VALUES(\1,'\2',\3,'\4', date_sub(curdate()), '\8');"
        values.append(re.sub(pattern,insertis, data))
        print(values[0])
print('\n'.join(values))
with open("newdata.txt", "w") as file:
    for value in values:
        file.write(value)
        
#it can accept any kind of input, current date , future date +, past date -







        #    1001 	Alex 	9900990091 	 USM101AL 	current_date - 750 days 	4.3
        #     1      2       3             4                   5  6   7      8
"""
1001 	Alex 	9900990091 	 USM101AL 	current_date - 750 days 	4.3
1002 	Bob 	8800880087 	 USQ102BO 	current_date - 700 days 	4.1
1003 	George 	9988998895 	 USB103GE 	current_date - 650 days 	3.9
1004 	Garry 	8899889981 	 USE104GA 	current_date - 600 days 	4.0
1005 	Peter  	7788778819 	 USQ105PE 	current_date - 500 days 	4.2
1006 	Chris 	9988298877 	 USB106CH 	current_date - 300 days 	3.8
1007 	Tim 	8899676677 	 USY107TI 	current_date - 200 days 	4.0
1008 	Steve 	6577889988 	 USW108SE 	current_date - 100 days 	3.6
1009 	Pat 	9876678900 	 USH109PA 	current_date - 60 days 	4.8
1010 	Nathan 	7896789618 	 USN110NA 	current_date - 30 days 	4.0
"""


"""
INSERT INTO driver_details VALUES('1001','Alex','9900990091','USM101AL', date_sub(curdate(),interval 750 day), '4.3');
INSERT INTO driver_details VALUES('1002','Bob','8800880087','USQ102BO', date_sub(curdate(),interval 700 day), '4.1');
INSERT INTO driver_details VALUES('1003','George','9988998895','USB103GE', date_sub(curdate(),interval 650 day), '3.9');
INSERT INTO driver_details VALUES('1004','Garry','8899889981','USE104GA', date_sub(curdate(),interval 600 day), '4.0');
INSERT INTO driver_details VALUES('1005','Peter','7788778819','USQ105PE', date_sub(curdate(),interval 500 day), '4.2');
INSERT INTO driver_details VALUES('1006','Chris','9988298877','USB106CH', date_sub(curdate(),interval 300 day), '3.8');
INSERT INTO driver_details VALUES('1007','Tim','8899676677','USY107TI', date_sub(curdate(),interval 200 day), '4.0');
INSERT INTO driver_details VALUES('1008','Steve','6577889988','USW108SE', date_sub(curdate(),interval 100 day), '3.6');
INSERT INTO driver_details VALUES('1009','Pat','9876678900','USH109PA', date_sub(curdate(),interval 60 day), '4.8');
INSERT INTO driver_details VALUES('1010','Nathan','7896789618','USN110NA', date_sub(curdate(),interval 30 day), '4.0');
"""
