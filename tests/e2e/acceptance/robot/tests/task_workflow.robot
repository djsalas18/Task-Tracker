*** Settings ***
Documentation       End-to-End Acceptance Tests for Task Workflow
Library             Collections
Resource            ../resources/common_keywords.resource
Resource            ../resources/task_keywords.resource

Test Setup          Start Test Session
Test Teardown       Close Browser

*** Test Cases ***

TC-US002-001: User Can Create A Valid Task Through The Web UI
    [Tags]    acceptance    ui    smoke    TC-US002-001
    Open Task Application          # This opens the browser
    Go To Add Task Page            # Now safe to use Go To
    Create Task Via UI    ${VALID_TITLE}    ${VALID_DESC}
    Task Should Be Visible In List    ${VALID_TITLE}

TC-US003-001: View Tasks Shows Empty List When No Tasks Exist
    [Tags]    acceptance    ui    TC-US003-001
    Delete All Tasks Via API
    Open Task Application
    Verify Empty Task List Message

TC-US003-002: User Can View All Created Tasks
    [Tags]    acceptance    ui    TC-US003-002
    Delete All Tasks Via API
    Create Task Via API    Task One    First description
    Create Task Via API    Task Two    Second description

    Open Task Application
    Task Should Be Visible In List    Task One
    Task Should Be Visible In List    Task Two

Health Check Endpoint Works
    [Tags]    acceptance    api    health    TC-US001-001
    API Should Return    ${API_HEALTH}

Create Task Returns 201 And Correct Data
    [Tags]    acceptance    api    TC-US002-001
    ${task}=    Create Task Via API    ${VALID_TITLE}    ${VALID_DESC}
    Dictionary Should Contain Key    ${task}    id
    Should Be Equal    ${task['title']}    ${VALID_TITLE}