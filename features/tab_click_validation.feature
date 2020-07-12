Feature: Checking all tab clicks are working fine
  This is to check whether tab clicks are working well

    Background: : Open Chrome and login
      Given I launch chrome browser
      When I open orange hrm homepage
      And Enter username "Admin" and password "admin123"
      And I Click login button
      Then Successfully login to dashboard page

    Scenario Outline: Check click functionality of tabs
      When Check Successful login in dashboad
      Then click on "<tab>"
      And check title name is "<heading>"
      And close web browser
      Examples:
        |           tab                          | heading                |
        | menu_admin_viewAdminModule             | System Users           |
        |   menu_pim_viewPimModule               | Employee Information   |
        | menu_leave_viewLeaveModule             | Leave List             |
        | menu_time_viewTimeModule               | Define Timesheet Period|
        | menu_recruitment_viewRecruitmentModule | Candidates             |
        | menu__Performance                      | Performance Trackers   |
        | menu_dashboard_index                   | Dashboard              |
        | menu_directory_viewDirectory           | Search Directory       |
        | menu_maintenance_purgeEmployee         | Purge Employee Records |
        | menu_buzz_viewBuzz                     | Error                  |



