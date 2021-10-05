#simple way to take inputs in a variable data

import re
#print(re.sub(r'abc(def)g(hi)', r'nope\1\2',"abcdefghi") )
values=[]
#data="SEASONAL15 	current_date – 1 days 	Seasonal offer 	15"
dat=["1001 	Alex 	9900990091 	 USM101AL 	current_date - 750 days 	4.3",
"1002 	Bob 	8800880087 	 USQ102BO 	current_date - 700 days 	4.1",
"1003 	George 	9988998895 	 USB103GE 	current_date - 650 days 	3.9"]

datas=[]
while True:
    try:
        line = input("")
    except EOFError:
        break
    datas.append(line)

#rint('\n'.join(datas))
for data in datas:
        data = data.encode("ascii", "ignore").decode()
        data=re.sub('\s+',' ',data)
        #print(data)
        
        #1     2                   3                 4            5         6      7
        pattern=r"^(US31D\d{3}) (\d{4}) ([\w]* [\w]*) (\w*) (\d*) ([\d\.]*)$"
        insert=r"INSERT INTO vehicle_details VALUES('\1',\2,'\3','\4',\5,'\6');"
        values.append(re.sub(pattern,insert, data))
print('\n'.join(values))
#print([value for value in values])


"""
US31D456 	1001 	Toyota Corolla 	Sedan 	4 	39.00
US31D457 	1002 	Subaru Crosstek 	SUV 	6 	49.00
US31D458 	1003 	Toyota Highlander 	SUV 	6 	59.00
US31D459 	1004 	Honda Fit 	Mini 	3 	19.00
US31D460 	1005 	Volkswagon GTI 	Hatchback 	5 	27.00
US31D461 	1006 	Honda Civic 	Sedan 	4 	34.00
US31D462 	1007 	Kia Optima 	Sedan 	4 	29.00
US31D463 	1008 	Kia Rio 	Hatchback 	4 	29.00
US31D464 	1009 	Chevrolet Bolt 	Mini 	3 	17.00
US31D465 	1010 	Honda Pilot 	SUV 	6 	69.00
"""
