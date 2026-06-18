Feature: Order Transaction test related to
  order transactions

  Scenario Outline: Verify success message shown in order details page
    Given Place the item order with <username> and <password>
    And the user on landing page
    When I log in to portal with <username> and <password>
    And navigate to order page
    And select the order
    Then order message is successfully displayed
    Examples:
      | username | password |
      | aumisky18@gmail.com | Testing@18 |