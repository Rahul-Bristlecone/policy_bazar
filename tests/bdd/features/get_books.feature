Feature: Get list of books from the database
  Scenario: Books fetched successfully
    Given the database contains books
    When the url is hit with get request along with the required endpoint
    Then list of books is fetched and displayed