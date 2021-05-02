@home
Feature: home page can navigate to other module

    Scenario: go to popular make page and go back
        Given Go to Home page
        When  the user click popular make link
        Then  successfully go to make page
        And   ckick home logo can go back

    Scenario: go to popular model page and go back
        Given Go to Home page
        When  the user click popular model link
        Then  successfully go to model page
        And   ckick home logo can go back
    
    Scenario: go to overall rating page and go back
        Given Go to Home page
        When  the user click overall link
        Then  successfully go to overall rating page
        And   ckick home logo can go back