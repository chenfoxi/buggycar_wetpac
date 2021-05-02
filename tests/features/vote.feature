@vote
Feature: vote for model

    Scenario: logined user vote a model and add comment
        Given Go to register page register a new user <username>
        And   Login with the new user
        And   Go to a model
        When  the user add <comment> and vote
        Then  vote successfully
        And   comment <comment> showed successfully
        Examples: 
        | comment | username |
        | testABC | chen     |

    Scenario: logined user vote a model without comment
        Given Go to register page register a new user <username>
        And   Login with the new user
        And   Go to a model
        When  the user vote
        Then  vote successfully
        Examples: 
        | username |
        | chen     |

    
    Scenario: No login user cannot vote
        Given Without login and go to a model
        When  the user want to vote
        Then  cannot vote