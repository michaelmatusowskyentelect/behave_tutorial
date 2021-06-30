# Created by Michael at 2021/06/30
Feature: Verify if posts are added and deleted using the posts API

  Scenario: Verify posts API functionality
    Given a post that needs to be added
    When we execute the posts API method
    Then the post is successfully added
