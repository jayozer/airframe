# airframe
Editable table(s) that sync to Snowflake table(s). 
V1:
- Add Authorization page. (Use face id or username/password) (Multi page auth is a must but not available without a hack. )
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
- Small Analytics. Current Number of Team members, Last updated date for the list, Any duplicate entries detected and if so returned in a dataframe.
- Need a spinner as I am querying the Snowflake table.
- Add who made the changes. Current login. Time updated. 
- Add key to each day editor.
- Create a template file to add more frames. Basically a empty shell of .py file that allows user to duplciate from and create a table in snwoflake. It should include the create scripts for table and views as well as where to add secrets. 

+ Check for duplicate rows
+ Session states is a must. Everything is running all the time.

-use the on_change event to trigger a calculation when a cell is changed. For example, the following code will calculate the sum of the values in the a and b columns and display the result in the c column:
Code snippet
df = pd.DataFrame({'a':[1,2,3], 'b':[4,5,6], 'c': [None, None, None]})

editable_df = st.experimental_data_editor(df, on_change=lambda df: df['c'] = df['a'] + df['b'])
Use code with caution. Learn more
The on_change event takes a function as its argument. The function is called whenever a cell in the data editor is changed. In this example, the function calculates the sum of the values in the a and b columns and assigns the result to the c column.

- Duplicate entries return null values since it sees nulls as duplicate. So need to add null, empty the script as well. The very first one. 