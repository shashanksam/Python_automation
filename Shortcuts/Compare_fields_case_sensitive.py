

def popOutDifferentFields():
    payloadListCollection="""approved_By			
approved_Flag		
approver_COMMENTS	
cLient				
current_Status		
customer_No			
job_Run_Date		
language_Key		
market				
modified_By			
modified_Date		
modified_Time		
name				
placeHolder			
placeholderextra7	
release				
text				
text_ID
    """

    entityListCollection="""approved_By
approved_Flag
approver_COMMENTS
client
current_Status
customer_No
job_Run_Date
language_Key
market
modified_By
modified_Date
modified_Time
name
placeholder
PLACEHOLDEREXTRA7
release
text
text_Id
    """

    payloadListOld=payloadListCollection.split("\n")
    entityListOld=entityListCollection.split("\n")

    payloadList={}
    entityList={}
    for payload in payloadListOld:
        field=payload.strip()
        payloadList[field.lower()]=field
        
    for entity in entityListOld:
        field=entity.strip()
        entityList[field.lower()]=field

    notPresentfields=[]
    wrongCaseSensitiveFields=[]
    for field in payloadList.keys():
        if(field in entityList.keys()):
            if(payloadList[field]!=entityList[field]):
                print(payloadList[field])
                # wrongCaseSensitiveFields.append(payloadList[field)
        else: notPresentfields.append(field)
    
    print("\nField Not Present: ")
    # print(notPresentfields)
    for field in notPresentfields:print(field)


popOutDifferentFields()





    

