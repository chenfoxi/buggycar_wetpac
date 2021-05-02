@authen
Feature: buggy Login and logout
    the user login buggy with username and password

    @login
    Scenario: correct username and password
        Given Go to Home page
        And   the user has been registered correctly
        When  the user inputs <username> and <password>
        Then  login successfully and <name> should be displayed
        Examples: 
        | username | password   | name |
        | tchen    | Abc!123456 | foxi |

    @login
    Scenario: login with incorrect username and password
        Given Go to Home page
        When  the user inputs wrong <username> and <password>
        Then  error message is displayed
        Examples:
        | username     |  password      | 
        | nouser       |  wrongpassword |
        | tchen        |  %adminstrator |
    
    @logout
    Scenario: user logout
        Given Go to Home page
        Given the user has login with <username> and <password>
        When  the user logout
        Then  the user successfully logout
        Examples:
        | username     |  password   |
        | tchen        |  Abc!123456 |