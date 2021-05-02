@profile
Feature: view profile and edit profile

    
    Scenario: the user's profile can be displayed correctly
        Given login with <username> and <currentpwd>
        And   goto profile page
        When  look the profile info
        Then  correctly display <username>, <firstname>, <lastname>, <gender>, <age>, <address>, <phone>, <hobby>
        Examples: 
        | username | firstname  | lastname | currentpwd | gender | address | phone | hobby | age |
        | tchen    | foxi       | chen     | Abc!123456 |        |         |       |       |     |

    
    Scenario: correctly update the user's info
        Given login with <username> and <currentpwd>
        And   goto profile page
        When  the user update with <firstname>, <lastname>, <gender>, <age>, <address>, <phone>, <hobby>
        Then  profile updates successfully <successMsg>
        Examples:
        | username       | firstname  | lastname | gender | address | phone | hobby   | currentpwd | age | successMsg |
        | tchenChange    | newName    | reg      | Male   | address | 1234  | Reading | Abc!123456 | 20  | The profile has been saved successful |
    
    
    Scenario: can correctly change the user's password
        Given login with <username> and <currentpwd>
        And   goto profile page
        When  the user update <currentpwd> with <newpassword> and <confirmpassword>
        Then  profile updates successfully <successMsg>
        And   login successfully with <username> and <newpassword>
        Examples:
        | username    | newpassword  | confirmpassword  | currentpwd | successMsg |
        | tchenPwd    | Abc!1234567  | Abc!1234567      | Abc!123456 | The profile has been saved successful |
    
    

    Scenario: show error msg when erase exsiting input info 
        Given login with <username> and <currentpwd>
        And   goto profile page
        When  the user erase <input>
        Then  <input> display <errormsg>
        And   save btn is disabled
        Examples:
        | username | currentpwd  | errormsg               | input     | 
        | tchen    | Abc!123456  | First Name is required | firstname |
        | tchen    | Abc!123456  | Last Name is required  | lastname  |
    

    Scenario: show error msg when password does not match 
        Given login with <username> and <currentpwd>
        And   goto profile page
        When  the user input <newpassword> 
        And   the user input wrong <confirmpassword>
        Then  display <errormsg> show password doesn't match
        And   save btn is disabled
        Examples:
        | username | currentpwd  | confirmpassword | newpassword  | errormsg |
        | tchen    | Abc!123456  | Abc!123456      | Abc!12345    | Passwords do not match |
        
