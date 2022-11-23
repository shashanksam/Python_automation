import re



def filterFieldsFromJSON(ListOfJsons):
    FieldsFromJsonList=[]
    for jsonfield in ListOfJsons:
        field=re.search("\"(.*)\":", jsonfield)
        if(field):
            FieldsFromJsonList.append(field.group(1))
#             print(field.group(1))
    return FieldsFromJsonList


def filterFieldsFromJavaEntityFile(ListOfentity):
    FieldsFromEntityList=[]
    for entityfield in ListOfentity:
        field=re.search("private String(.*);", entityfield)
        if(field):
            FieldsFromEntityList.append(field.group(1).strip())
#             print(field.group(1).strip())
    return FieldsFromEntityList



def popOutDifferentFields():
    payloadListCollection=""""placeholder": "90",
"material_No": "",
"length": null,
"width": null,
"height": null,
"approved_Flag": "AWAITING",
"modified_Date": "21",
"modified_By": "dated",
"approved_By": null,
"current_status": null,
"error_DETAILS": null,
"modified_Time": "13:31:3",
"load_PROCESS": "CREATE",
"approver_COMMENTS": null,
"placeholderextra7": ""

    """

    entityListCollection="""
private String	placeholder	;
private String	material_No	;
private String	length	;
private String	width	;
private String	height	;

private String	approved_Flag	;
private String	modified_Date	;
private String	modified_By	;
private String	approved_By	;
private String	current_status;
private String	error_DETAILS;
private String	modified_Time;
private String	load_PROCESS;
private String  approver_COMMENTS;

private String placeholderextra7;"""

    payloadListOld=payloadListCollection.split("\n")
    entityListOld=entityListCollection.split("\n")

    print("payloadOldList<")
    payloadListOld=filterFieldsFromJSON(payloadListOld)

    print(">\nentityOldList<")
    entityListOld=filterFieldsFromJavaEntityFile(entityListOld)
    print(">")


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
    print("Wrong Fields<")
    for field in payloadList.keys():
        if(field in entityList.keys()):
            if(payloadList[field]!=entityList[field]):
                print(payloadList[field])
                # wrongCaseSensitiveFields.append(payloadList[field)
        else: notPresentfields.append(field)
    print(">")
    print("\nField Not Present:< ")
    # print(notPresentfields)
    for field in notPresentfields:print(field)
    print(">")


popOutDifferentFields()





    

