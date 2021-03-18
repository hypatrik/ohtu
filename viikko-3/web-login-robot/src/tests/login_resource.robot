*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set PasswordConfirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    [Arguments]  ${txt}
    Click Button  ${txt}

Input Credentials
    [Arguments]  ${username}  ${password}
    Set Username  ${username}
    Set Password  ${password}

Test Login With Correct Credentials
    Input Credentials  kalle  kalle123
    Submit Credentials  Login
    Login Should Succeed

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}