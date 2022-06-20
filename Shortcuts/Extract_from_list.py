import re

pattern= r"[(\d*)]"

names=[]
# listnames=input()
x = '' # The string is declared
while True:
    try:
        line = input()
    except EOFError:
        break
    names.append(line)
for name in names:
    x = re.search(r"\[(.*)\]", name)
    print("private String  ", x.group(1), " ;") 
    
    #inputs are
    """
    ,[Class_type]
      ,[Component_quantity]
      ,[Component_Unit_of_Measure]
      ,[Fixed_qty]
      ,[Operation_scrap]
      ,[Component_Scrap_in_Percent]
      ,[Indicator_Net_scrap]
    """
    
    
    #output is 
"""
private String   Class_type  ;
private String   Component_quantity  ;
private String   Component_Unit_of_Measure  ;
private String   Fixed_qty  ;
private String   Operation_scrap  ;
private String   Component_Scrap_in_Percent  ;
private String   Indicator_Net_scrap  ;
"""
