*** Settings ***
Library    SeleniumLibrary
Resource   variables.resource
Resource   common_keywords.resource

*** Keywords ***
Open Task Application
    [Documentation]    Open the main task list page (/tasks)
    Open Browser    ${BASE_URL}/tasks    ${BROWSER}
    Maximize Browser Window
    Wait Until Page Contains    All Tasks    timeout=10s

Go To Add Task Page
    [Documentation]    Navigate to the Create a Task form
    Go To    ${BASE_URL}/tasks/new
    Wait Until Page Contains    Create a Task    timeout=10s

Create Task Via UI
    [Arguments]    ${title}    ${description}
    [Documentation]    Fill and submit the add task form
    Input Text    id=task-title       ${title}
    Input Text    id=task-description    ${description}
    Click Button    Add Task
    Wait Until Page Contains    ${title}    timeout=5s

Task Should Be Visible In List
    [Arguments]    ${title}
    Page Should Contain    ${title}

Verify Empty Task List Message
    Page Should Contain    No tasks yet