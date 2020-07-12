Feature: Failed login test check
  This scenario is to check failed login test of the user

  Scenario Outline: To check multiple failed login scenario
    Given Launch ChromeBrowser
    When Entered username is "<username>" and password is "<password>"
    Then Check Invalid message on screen
    Then Close Browser
    Examples:
      | username | password |
      | admin12  | admin    |
      | admin    | 12334    |
      |          | hello    |
      | admin12  |          |