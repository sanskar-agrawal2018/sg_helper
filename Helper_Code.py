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
