Feature: OrangeHRM Valid Login

    Login with valid id and password

    Scenario:
      Given I launch chrome browser
      When I open orange hrm homepage
      And Enter username "Admin" and password "admin123"
      And I Click login button
      Then Successfully login to dashboard page
      And close web browser
