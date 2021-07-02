# Created by Michael at 2021/06/30
Feature: Basic CRUD operations on posts endpoint

  Scenario: Verify POST functionality
    Given a post that needs to be added
    When we execute the POST API method
    Then the post is successfully added


  Scenario: Verify GET functionality
    Given a post id
    When we execute the GET API method
    Then the post is successfully received


  Scenario: Verify PUT functionality
    Given a post that needs to be updated
    When we execute the PUT API method
    Then the post is successfully updated


  Scenario: Verify DELETE functionality
    Given a post that needs to be deleted
    When we execute the DELETE API method
    Then the post is successfully deleted
