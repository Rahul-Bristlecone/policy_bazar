# user management service - microservice
Feature: successful log in for an existing user, no login required for new tab
  Scenario: user should be able to login successfully
    Given user provide password and email id
    When password and email exists and match from DB
    Then display list of existing policies
    And recommendations