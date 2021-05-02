@overallRating
Feature: check overall rating list and view it page by page

    Scenario: show orverall rating list correctly
        Given Go to overall page
        When  the user check the overall list
        Then  rating list showed correctly

    Scenario: sort orverall rating by rank
        Given Go to overall page
        When  the user sort the list by rank (click it)
        Then  rating show according the rank ascending
    
    Scenario: go to a model page through clicking view more
        Given Go to overall page
        When  the user click the viewmore button to see the <num> model 
        Then  go to a model page
        Examples:
        | num |
        | 1   |
    
    Scenario: go to next page by right arrow
        Given Go to overall page
        When  the user click right arrow to see next page
        Then  go to the next page
    
    Scenario: go to previous page by left arrow
        Given Go to overall page
        When  the user click right arrow to see next page
        And   the user click left arrow to previous page
        Then  go to the previous page

    Scenario: go to a certain page by inputing number
        Given Go to overall page
        When  the user input <num> in the edit control
        Then  go to the <num> page
        Examples:
        | num |
        | 5   |