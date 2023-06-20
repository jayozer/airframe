import streamlit as st
from snowflake.connector.pandas_tools import pd_writer
import pandas as pd
import os
from sqlalchemy import create_engine

from dotenv import load_dotenv

load_dotenv()

# see all the deprecation warnings
#os.environ["SQLALCHEMY_WARN_20"] = "1"  # Removes warning message in SQLAlchemy
st.set_page_config(layout="centered", page_title="Airframe-Stream", page_icon="👩🏻‍💻")


st.markdown("**:blue[ORDER PROJECT CHANNEL MAP:]** The list of projects `Enterprise`, `Independent Agency`.", unsafe_allow_html=False, help="Enter the associate email, id and team name.")

# Load authorized usernames and passwords from environment variables
user=os.getenv('SNOWFLAKE_USER')
password=os.getenv('SNOWFLAKE_PASSWORD') 
account=os.getenv('SNOWFLAKE_ACCOUNT')
database=os.getenv('SNOWFLAKE_DATABASE')
warehouse=os.getenv('SNOWFLAKE_WAREHOUSE')
schema=os.getenv('SNOWFLAKE_SCHEMA')
table=os.getenv('SNOWFLAKE_TABLEORDER') #note SNOWFLAKE_TABLEORDER from environment variables
role=os.getenv('SNOWFLAKE_ROLE')
streamlit_user=os.getenv('STREAMLIT_USERNAME') # Ultimately this will be populated by an user account from AD.

#read from snowflake. Select the table and schema according to the sidebar radio button choice for sheets.
def read_from_snowflake_table(table, schema, user, password, account, warehouse, database):
    engine = create_engine('snowflake://{user}:{password}@{account_identifier}/?role={role}&warehouse={warehouse}'.format(
    user=user,
    password=password,
    account_identifier=account,
    role=role,
    warehouse=warehouse,
    database=database,
    pool_pre_ping=True)
    )
    # use pandas DataFrame's read_sql method to query data from Snowflake
    df = pd.read_sql(f'SELECT * FROM {schema}.{table}', engine)
    return df    

# read the current table from snowflake
project_map_df=read_from_snowflake_table(table, schema, user, password, account, warehouse, database)
# Assign the df to editable experimental data editor
project_map = st.data_editor(
    data=project_map_df,
    width=None,
    height=None,
    use_container_width=True,
    num_rows="dynamic",
    disabled=False,       
    key=None,
    on_change=None,
    args=None,
    kwargs=None,
    )

# Download option because people love to download. 
if project_map is not None:
    st.download_button(
        "⬇ Download project map table as .csv", project_map.to_csv(), "project_map.csv", use_container_width=True
    )

# Push to Snwoflake - Right now it is a complete truncate and load but I need to merge the dataframes. 
# Using front end as the source of truth.
def load_dataframe_to_snowflake_table(df, table_name, schema_name, usr, pwd, acct, warehouse, database_name):
    engine = create_engine('snowflake://{user}:{password}@{account_identifier}/?role={role}&warehouse={warehouse}'.format(
    user=user,
    password=password,
    account_identifier=account,
    role=role,
    warehouse=warehouse,
    database=database)
    )
    #truncate the table in Snowflake using SQL
    with engine.begin() as conn: 
        conn.execute(f'TRUNCATE TABLE {schema}.{table}')

    # use pandas DataFrame's to_sql method to insert the data into Snowflake table
    df.to_sql(table_name, engine, schema=schema_name, if_exists='append', index=False)


#Call the function
button_clicked = st.button("Sync to Snowflake", use_container_width=True)
if button_clicked and project_map is not None:
    with st.spinner("Syncing to Snowflake..."):
        load_dataframe_to_snowflake_table(project_map, table, schema, user, password, account, warehouse, database)
        st.success("Sync to Snowflake successful!")
