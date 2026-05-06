*** Settings ***
Library    RequestsLibrary
Library    SeleniumLibrary
Resource   variables.resource

*** Keywords ***
Start Test Session
    [Documentation]    Common setup for API tests
    Create Session    task_api    ${BASE_URL}    verify=True

API Should Return
    [Arguments]    ${endpoint}    ${expected_status}=200
    ${response}=    GET    ${BASE_URL}${endpoint}
    Should Be Equal As Integers    ${response.status_code}    ${expected_status}
    RETURN    ${response.json()}

Create Task Via API
    [Arguments]    ${title}    ${description}
    ${payload}=    Create Dictionary    title=${title}    description=${description}
    ${response}=    POST    ${BASE_URL}${API_TASKS}    json=${payload}
    Should Be Equal As Integers    ${response.status_code}    201
    RETURN    ${response.json()}

Delete All Tasks Via API
    [Documentation]    Clean up all tasks before/after tests
    ${response}=    GET    ${BASE_URL}${API_TASKS}
    ${tasks}=    Set Variable    ${response.json()}
    FOR    ${task}    IN    @{tasks}
        ${id}=    Set Variable    ${task['id']}
        DELETE    ${BASE_URL}${API_TASKS}/${id}
    END