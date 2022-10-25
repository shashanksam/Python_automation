    #Program to create template for get details of a new sheet
from datetime import date, datetime


def Create_getDetailsJavaCodeTemplate():
    # Basics
    Your_Name  ="Your_Name"
    Object_Name="Object_Name"
    Sheet_Name ="Sheet_Name"

    """
    Your_Name
    Object_Name
    Sheet_Name

    getDetails_Object_SheetName_method_name
    getdetailsAPINAME
    tt_TableName_from_Entity
    r_Object_sheet_Name_Repository_instance_name

    DropdownName1
    DropdownName=[]
    field_Name_from_check_Table=[]
    TT_Check_Table_name=[]
    DropdownName1_from_field_name=[]

    """

    print("Provide "+	Your_Name	+" (Example:Shashank)")
    Your_Name= input()

    print("Provide "+	Object_Name	+" (Example:Material)")
    Object_Name= input()

    print("Provide "+	Sheet_Name	+" (Example:PlantData1)")
    Sheet_Name= input()



    #sheet_related_names
    getDetails_Object_SheetName_method_name="getDetails Object_SheetName method_name"
    getdetailsAPINAME="APINAME"
    #R$_getdetailsAPINAME	
    tt_TableName_from_Entity="tt_TableName_from_Entity"
    r_Object_sheet_Name_Repository_instance_name="r_Object_sheet Repository instance_name"

    print("Provide "+	getDetails_Object_SheetName_method_name	+" for this "+Sheet_Name+" (For example :getDetailsMATERIAL_PLANTDATA1) ")
    getDetails_Object_SheetName_method_name	= input()
    print("Provide "+	getdetailsAPINAME	+" for this "+Sheet_Name+" (For example :R4_MATERIAL_PLANTDATA1) ")
    getdetailsAPINAME	= input()
    print("Provide "+	tt_TableName_from_Entity	+" for this "+Sheet_Name+" (For example :TT_R4_PORTAL_MATERIAL_PLANTDATA1) ")
    tt_TableName_from_Entity	= input()
    print("Provide "+	r_Object_sheet_Name_Repository_instance_name	+" for this "+Sheet_Name+" (For example :r_Material_Plantdata1) ")	
    r_Object_sheet_Name_Repository_instance_name	= input()




    PartABeginningSequenceTemplate="""
        public Map<String, Object> """+ getDetails_Object_SheetName_method_name +"""(HttpSession session, Map<String, String> request) {
            UserSessionEntity currentUser = userDetailsController.setUserLastActiveTime(request.get("uniqueId"));
            String userMarket = currentUser.getMarket();
            logger.info("API """+ getdetailsAPINAME+ """ was invoked by   " + currentUser.getUserId() + ": " + userMarket);
            logger.info("Fetching dropdown details started.");

            Map<String, Map<String, String>> parentData = new HashMap<>();
            Map<String, Object> response = new HashMap<>();
    """


    #DropDown list names
    Count_i=1
    DropdownName1=""
    DropdownName=[]
    field_Name_from_check_Table=[]
    TT_Check_Table_name=[]
    DropdownName1_from_field_name=[]

    print(" And How many dropdowns?")
    Count_i=int(input())


    Part_B_DropDownFetchSequenceTemplate=""


    for i in range(Count_i):
        DropdownName.append(                 input(" Enter DropdownNamei "+str(i+1)+" (for Example:BOM_item_category_List)                    ") )
        field_Name_from_check_Table.append(  input(" Enter field_Name_from_check_Tablei "+str(i+1)+" (for Example:WERKS)                      ") )
        TT_Check_Table_name.append(          input(" Enter TT_Check_Table_namei "+str(i+1)+" (for Example:TT_S4APP_T001W)                     ") )
        DropdownName1_from_field_name.append(input(" Enter DropdownName "+str(i+1)+" to be sent to UI in response (for Example:\"BOM_item_category_List\") "))

    for i in range(Count_i):
        DropdownNamei=DropdownName[i]
        field_Name_from_check_Tablei=field_Name_from_check_Table[i]
        TT_Check_Table_namei=TT_Check_Table_name[i]
        DropdownName1_from_field_namei=DropdownName1_from_field_name[i]
        forEachPart_B_for_dropdowns="""
            String """+DropdownNamei+"""Query = "select distinct("""+field_Name_from_check_Tablei+""") from [2ONE_R4_" + dbSchemaRegion
                    + "].[dbo]."""+TT_Check_Table_namei+"""";
            
            List<String> """+DropdownNamei+"""Data = r4_Common_Repository.fetchDropDownList("""+DropdownNamei+"""Query);
            
            Map<String, String> """+DropdownNamei+"""Map = """+DropdownNamei+"""Data.stream()
                    .collect(Collectors.toMap(Function.identity(), data -> data));

            parentData.put(\""""+DropdownName1_from_field_namei+"""\", """+DropdownNamei+"""Map);
            """
        Part_B_DropDownFetchSequenceTemplate = Part_B_DropDownFetchSequenceTemplate+forEachPart_B_for_dropdowns
        

    #no idea why i made 2 for loops, i had other intentions for the lists, so i didnt have time to change the list and to make a single for loop


    PartB2_Extra_filter_extracting=""" String filter1=result.get("filter1"); """


    Part_C_FetchSheetDataEndSequenceTemplate="""
            logger.info("Fetching dropdown details ended.");
            logger.info("Fetching data by market started." + " Market: " + userMarket);
            List<"""+tt_TableName_from_Entity+"""> received_getDetails_Data = """+r_Object_sheet_Name_Repository_instance_name+"""
                    .findbymarket(userMarket);
            List<"""+tt_TableName_from_Entity+"""> scopedRecords = received_getDetails_Data.stream()
                    .filter(data -> !("Descope").equals(data.getCurrent_Status())).collect(Collectors.toList());
            List<"""+tt_TableName_from_Entity+"""> deScopedRecords = received_getDetails_Data.stream()
                    .filter(data -> ("Descope").equals(data.getCurrent_Status())).collect(Collectors.toList());
            logger.info("Fetching data by market has ended.");
            response.put("parentData", parentData);
            response.put("countFetched", received_getDetails_Data.size());
            logger.info("count of records fetched is "+ received_getDetails_Data.size());
            response.put("content", scopedRecords);
            response.put("deScopedcontent", deScopedRecords);

            logger.info("API """+ getdetailsAPINAME+ """ Ended");

            return response;
        }
    """

                
    print("Template Created for "+Object_Name+" "+Sheet_Name+" sheet by "+Your_Name+". on "+str(datetime.now())+":   -----")
    print(PartABeginningSequenceTemplate+Part_B_DropDownFetchSequenceTemplate+Part_C_FetchSheetDataEndSequenceTemplate)
    print("-------")


Create_getDetailsJavaCodeTemplate()
