Feature: Testing a simple Sever
    Scenario: Got a correct json
        Given {"input-string" : "this is the input string"}
        When a 200 status is received
        Then the output-string should be in all caps

    Scenario: Got a Bad json
        Given {"key":"string"}
        When a 400 status is received
        Then we should get an error message

