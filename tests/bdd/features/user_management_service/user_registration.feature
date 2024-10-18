# user management service - microservice
Feature: register a user in the list of existing user
  Scenario: user should be added to the list of existing users
    Given user provide email, first name, last name, password and age
    When details are submit
    Then user should be added to the DB with a user id