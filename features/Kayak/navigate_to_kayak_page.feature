@regression_tests
Feature: Validate element created dropdown column

  Scenario: Navigate to the Kayak home page and validate principal elements
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    And The page "should" contain the next elements
      | name   | type   |
      | where  | label  |
      | signin | button |

  Scenario: Validate URL of Home page
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    And The url page should be equal to the next "https://www.kayak.com.co/" url

  Scenario Outline: Navigate between countries and validate the URL
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    When I navigate to the "<url>" URL
    Then The url page should be equal to the next "<url>" url

    Examples:
      | url                       |
      | https://www.kayak.com.my/ |
      | https://www.kayak.com.pr/ |
      | https://www.kayak.com.br/ |


  Scenario Outline: Navegate for dropdown
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    When I click on the "<name>" "<type>"

    Examples:
      | name         | type   |
      | flights      | button |
      | stays        | button |
      | car          | button |
      | flight_hotel | button |
      | explore      | button |
      | blog         | button |

  Scenario: Navigate and check dropdown
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    When I click on the "flights" "button"
    When I click on the "stays" "button"
    When I click on the "car" "button"
    When I click on the "flight_hotel" "button"
    When I click on the "explore" "button"
    When I click on the "blog" "button"









