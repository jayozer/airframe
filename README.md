# airframe
Editable table(s) that sync to Snowflake table(s). 
V1:
- Add Authorization page. (Use face id or username/password)
- Side table list for TE_TIME_Process_Point (Agency_External_Users, TE_Time_Action_Weight_Lkp). EDM_Metadata (Order_Project_Channel_Map, Order_Status_Group_Lkp)
+ Add `Push to Snowflake` button. 
- Add user name to the table. The current passcode to login to Streamlit.
- Duplicated name or employee id is detected.


V2: 
Streamlit - experimental data editor add-ons
- Add a check that counts if a name is added more then once. 
- Check data types (numeric accepts numeric only)
- A way to track who made the change. Maybe get the login credentials and populate the audit fields automatically, including time of the add/update. This way it will be complete replacement. 
- Instead of creating an initial list of data, I should read what is in the DB.table first and display that in a editable data frame. Then I need to add to that and rerun......