Feature: Basic POST operations on posts endpoint

#  Background:
#    Given a user
#    When the user logs in
#    Then the user is redirected to the home page


  Scenario: Verify POST functionality
    Given a post that needs to be added
    When we execute the POST API method
    Then the post is successfully added


  Scenario Outline: Verify different posts can be added
    Given a post with <user_id> <title> and <body>
    When we execute the POST API method
    Then the post is successfully added

  Examples:
  | user_id | title         | body                    |
  | 1       | "World News"  | "Some Text"             |
  | 2       | "Reddit"      | "The best site on Earth |
  | 3       | "Google"      | "Just google it!"       |
#
#
#  Scenario: Verify DELETE functionality
#    Given a post that needs to be deleted
#    When we execute the DELETE API method
#    Then the post is successfully deleted
