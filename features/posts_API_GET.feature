Feature: Basic GET operations on posts endpoint
  # Enter feature description here

  @minor
  Scenario: Verify GET functionality
    Given a post id
    When we execute the GET API method
    Then the post is successfully received
