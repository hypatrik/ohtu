*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  nalle
    Set Password  kalle123
    Set PasswordConfirmation  kalle123
    Submit Credentials  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Register Valid User

Register With Valid Username And Too Short Password
    Register Invalid Too Short Password

Register With Nonmatching Password And Password Confirmation
    Set Username  nalle
    Set Password  kalle1234
    Set PasswordConfirmation  kalle123
    Submit Credentials  Register
    Register Should Fail With Message  Mismatching password

Login After Successful Registration
    Register Valid User
    Go To Login Page
    Input Credentials  nalle  kalle123
    Submit Credentials  Login
    Login Should Succeed

Login After Failed Registration
    Register Invalid Too Short Password
    Go To Login Page
    Input Credentials  nalle  kalle
    Submit Credentials  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Valid User
    Set Username  nalle
    Set Password  kalle123
    Set PasswordConfirmation  kalle123
    Submit Credentials  Register
    Register Should Succeed

Register Invalid Too Short Password
    Set Username  nalle
    Set Password  kalle
    Set PasswordConfirmation  kalle
    Submit Credentials  Register
    Register Should Fail With Message  Invalid password

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open