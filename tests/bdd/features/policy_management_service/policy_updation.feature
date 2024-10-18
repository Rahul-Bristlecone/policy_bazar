# microservice - policy management service
  # policy update - only specific details can be updated
  Feature: update a policy for a policy bank
    Scenario: update a policy for a user when required details are provided
      Given details like policyID, category, tenure
      When policy will be added in the list of policies
      Then a new policy is created and added to the list of policies