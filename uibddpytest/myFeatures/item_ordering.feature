Feature: Automate the item ordering process on Flipkart
	Scenario: Add two items to the cart and verify cart contents and total price
		Given User open the Flipkart website
		When User search for "Samsung S23 128 GB" and select the second item
		Then User check the availability using the pin code "201309" and add "mobile" it to the cart
		Then User return to the home page
		When User search for "bajaj iron majesty" and select the second item
		Then User check the availability using the pin code "201309" and add "iron" it to the cart
		Then User return to the home page
		Then User navigate to the cart
		Then User verify that both items are present in the cart
		Then User verify that the total price reflects the sum of both items
		Then User remove one item from the cart
		Then User verify that the total price is updated
