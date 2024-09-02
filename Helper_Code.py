import pandas as pd

# Sample DataFrame
data = {
    'column_name': ['123', '456.789', 'abc', '789.123', '999']
}
df = pd.DataFrame(data)

# Function to format number
def format_number(value):
    try:
        # Check if the value can be converted to a float
        number = float(value)
        # Format the number to a specific format, e.g., with two decimal places
        return f"{number:.2f}"
    except ValueError:
        # Return the original value if it's not a number
        return value

# Apply the function to the column
df['column_name'] = df['column_name'].apply(format_number)

print(df)

i
mport pandas as pd

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
