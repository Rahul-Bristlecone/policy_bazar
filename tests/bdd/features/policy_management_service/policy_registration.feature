# microservice - policy management service - for user
  Feature: register a policy for a userId
    Scenario: register a policy for a user when required details are provided like tenure
      Given details like policyID
      When user accepts and submit
      Then a new policy no. is created and it will refer to the user id