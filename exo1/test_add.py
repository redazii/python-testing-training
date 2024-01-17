import pytest
from my_menu_module import RestaurantManager, MenuItemAlreadyAdded, RestaurantNotFound

@pytest.mark.parametrize(
   "restaurant, item, description, price, expected_error_message",
    [
        ("Default Diner", "Data", "Couldn't find anything eatable that starts with 'D'", 1, "Data added to Default Diner's menu"),
        ("Default Diner", "Dust", "Maybe you could eat this, I wouldn't recommend", 0.01, "Dust added to Default Diner's menu")
    ]
)
def test_valid_add_menu_item(restaurant, item, description, price, expected_output, default_restaurant_manager):
    rm = default_restaurant_manager
    output = rm.add_menu_item(restaurant, item, description, price)
    assert output == expected_output

@pytest.mark.parametrize(
        "restaurant, item, description, price, expected_error_message",
 [
    ("Sushi Palace", "Sashimi Platter", "Assorted Sashimi selection", 22.50, "Sushi Palace already has Sashimi Platter in the menu"),
    ("Le Pâtisserie", "Éclair", "Delicious French pastry", -3.50, "Price must be positive"),
    ("Unknown Café", "Latte", "Regular latte", 3.50, "Unknown Café does not exist")
])
def test_invalid_add_menu_item(restaurant, item, description, price, expected_error_message, default_restaurant_manager):
    rm = default_restaurant_manager
    with pytest.raises((MenuItemAlreadyAdded, ValueError, RestaurantNotFound)) as e:
        rm.add_menu_item(restaurant, item, description, price)
    assert str(e.value) == expected_error_message