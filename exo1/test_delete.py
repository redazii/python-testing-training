import pytest
from class.RestaurantManager import RestaurantManager, MenuItemNotFound, RestaurantNotFound

@pytest.mark.parametrize("restaurant, item, expected_output", [
  ("Static Sushi", "Salmon Sashimi", "Salmon Sashimi removed from Static Sushi's menu"),
  ("Permanent Pizza", "Pineapple Pizza", "Pineapple Pizza removed from Permanent Pizza's menu")
])
def test_valid_delete_menu_item(restaurant, item, expected_output, default_restaurant_manager):
    rm = default_restaurant_manager
    output = rm.delete_menu_item(restaurant, item)
    assert output == expected_output

@pytest.mark.parametrize("restaurant, item, expected_error_message",[
  ("Static Sushi", "Salmon Sushi", "Static Sushi does not have Salmon Sushi in the menu"),
  ("Missing Milkshake", "Mega Mystery", "Missing Milkshake does not exists")
])
def test_invalid_delete_menu_item(restaurant, item, expected_error_message, default_restaurant_manager):
    rm = default_restaurant_manager
    with pytest.raises((MenuItemNotFound, RestaurantNotFound)) as e:
        rm.delete_menu_item(restaurant, item)
    assert str(e.value) == expected_error_message