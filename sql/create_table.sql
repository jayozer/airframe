create or replace TABLE DEMO_DB.STREAMABLE.EMPLOYEE_TEAM (
	EMPLOYEE_EMAIL VARCHAR(255),
	EMPLOYEE_ID VARCHAR(10),
	TEAM_NAME VARCHAR(255)
);

create or replace TABLE DEMO_DB.STREAMABLE.ORDER_PROJECT_CHANNEL_MAP (
	PROJECT_ID VARCHAR(256),
	SOURCE_SYSTEM_CODE VARCHAR(256),
	PARTNER_TYPE_ID VARCHAR(256),
	PARTNER_COMPANY_ID VARCHAR(256),
	TRANSACTION_TYPE_DESC VARCHAR(256),
	CHANNEL_SOLUTION_NAME VARCHAR(256),
	CHANNEL_NAME VARCHAR(256),
	PROJECT_NAME VARCHAR(256),
	UPDATED_BY VARCHAR(256),
	UPDATED_TS VARCHAR(256),
	PROJECT_TYPE_NAME VARCHAR(256),
	TRANSACTION_TYPE_ID VARCHAR(256)
);

-- client_sla_biz_hr_lkp