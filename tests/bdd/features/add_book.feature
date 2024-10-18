Feature: Add book to the list of existing books collection
         collection is defined based on genre
  Scenario: Book successfully added to a genre
            and if no genre comes in payload then undefined
    Given a json payload is provided with book data
    When the url is hit with post request and required endpoint
    Then book is added to the db
    And the response code is returned