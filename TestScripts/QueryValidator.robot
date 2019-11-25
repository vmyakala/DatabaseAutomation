***Settings***
Library    DatabaseLibrary    
Library    Collections 
Library    OperatingSystem    
Library    String 
Library    ../QuerySeparator.py    

***Variables***
${filePath}    log_folder/NAS.log.2019-11-15             

*** Test Cases ***

FetchQueriesFromLog
    Run Keyword    Get Queries From Log File    ${filePath}        
    ${File}=    Get File    ${filePath}.sql
    @{list}=    Split to lines  ${File}
    ${count}    Convert To Integer    1
    Connect To Database    dbConfigFile=default.cfg
    :FOR    ${line}    IN    @{list}
    \    Log To Console    Query-${count}
    \    ${Output}    Run Keyword And Continue On Failure     Execute Sql String    ${line}   
    \    Log To Console    ${line}    
    \    Log To Console    ${Output}  
    \    ${count}    Set Variable    ${count+1}  
    Disconnect From Database
    