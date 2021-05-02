@authen
Feature: register new user with valid info and block invalid register info 

    @register
    Scenario: register new user using valid info
        Given Go to register page
        When  the user register with <username> <firstname> <lastname> <password> and <confirmpassword>
        Then  register successfully and show <successfulMsg>
        And   register btn is disabled
        And   can login with <username> and <password>
        Examples: 
        | username     | firstname  | lastname | password   | confirmpassword | successfulMsg |
        | registerTestg | foxi       | reg      | Abc!123456 | Abc!123456      | Registration is successful |

    @register
    Scenario: register new user but username's existed
        Given Go to register page
        When  the user register with <username> <firstname> <lastname> <password> and <confirmpassword>
        Then  register unsuccessfully and error message <error> is displayed
        Examples:
        | username | firstname  | lastname | password   | confirmpassword | error |
        | tchen    | foxi       | reg      | Abc!123456 | Abc!123456      | User already exists |
    
    @register
    Scenario: without username cannot register
        Given Go to register page
        When  the user input <firstname> <lastname> <password> and <confirmpassword>
        Then  register btn is disabled
        Examples:
        | firstname  | lastname | password   | confirmpassword |
        | foxi       | reg      | Abc!123456 | Abc!123456      |
    
    @register
    Scenario: show error msg when password does not match 
        Given Go to register page
        When  the user input correct <username> <firstname> <lastname> <password> 
        And   the user input wrong <confirmpassword>
        Then  display <errormsg> show password doesn't match
        And   register btn is disabled
        Examples:
        | username   | firstname  | lastname | password   | confirmpassword | errormsg |
        | regRandom  | foxi       | reg      | Abc!123456 | Abc!12345       | Passwords do not match |
    
    @register
    Scenario: show error msg when erase exsiting input info 
        Given Go to register page
        When  the user input correct <username> <firstname> <lastname> <password> <confirmpassword>
        And   the user erase <input>
        Then  <input> display <errormsg>
        And   register btn is disabled
        Examples:
        | username   | firstname  | lastname | password   | confirmpassword  | errormsg               | input     | 
        | regRandom  | foxi       | reg      | Abc!123456 | Abc!123456       | Login is required      | username  |
        | regRandom  | foxi       | reg      | Abc!123456 | Abc!123456       | First Name is required | firstname |
        | regRandom  | foxi       | reg      | Abc!123456 | Abc!123456       | Last Name is required  | lastname  |
        | regRandom  | foxi       | reg      | Abc!123456 | Abc!123456       | Password is required   | password  |
        | regRandom  | foxi       | reg      | Abc!123456 | Abc!123456       | Passwords do not match | confirm   |
