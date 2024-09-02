import pandas as pd

# Sample DataFrame with mixed data types
data = {
    'A': [1.23e10, 4.56e-4, 7.89e3],  # Numeric column with scientific notation
    'B': [1.01e5, 2.02e-6, 3.03e2],   # Numeric column with scientific notation
    'C': ['text1', 'text2', 'text3']  # Non-numeric column
}

df = pd.DataFrame(data)

# Convert a specific numeric column to string format
column_to_convert = 'A'
if pd.api.types.is_numeric_dtype(df[column_to_convert]):
    df[column_to_convert] = df[column_to_convert].apply(lambda x: f"{x:.10f}")

# Display the modified DataFrame and its dtypes
print(df)
print(df.dtypes)
<UC_OBJECT OBJECT_TYPE="JOBS">
    <JOB TITLE="SSH to Linux Server" RUN_MASK="0000000000000000" OH_SubType="UNIX">
        <JBAgentName>YOUR_AGENT_NAME</JBAgentName>
        <JBAgentType>UNIX</JBAgentType>
        <JBAgentOsType>Unix</JBAgentOsType>
        <JBMode>PROCESS</JBMode>
        <JBProcess>
            <![CDATA[
#!/bin/bash

# Variables
REMOTE_USER="username"
REMOTE_HOST="your.linux.server"
COMMAND="ls -l /path/to/directory"

# SSH Command Execution
ssh -o StrictHostKeyChecking=no $REMOTE_USER@$REMOTE_HOST "$COMMAND"
            ]]>
        </JBProcess>
    </JOB>
    <ATTRIBUTES>
        <Queue>CLIENT_QUEUE</Queue>
        <Priority>000</Priority>
        <MaxExecutionTime>00:30</MaxExecutionTime>
        <TimeZone>UTC</TimeZone>
        <Notification></Notification>
    </ATTRIBUTES>
</UC_OBJECT>
