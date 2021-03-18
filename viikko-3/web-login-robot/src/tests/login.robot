*** Settings ***
Resource  resource.robot
Resource  login_resource.robot

Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kalle123
    Submit Credentials  Login
    Login Should Succeed


Login With Incorrect Password
    Input Credentials  kalle  kalle456
    Submit Credentials  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Login With Nonexistent Username
    Set Username  nalle
    Set Password  kalle456
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open
    