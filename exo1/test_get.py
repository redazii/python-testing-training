import pytest

@pytest.mark.parametrize(
    "dining_spot, expected_menu",
    [
        ('Default Diner', []),
        ("Static Sushi", [{"name": "Salmon Sashimi", "description": "Salmon (6 pieces)", "price": 5.99}]),
        ("Permanent Pizza", [
            {"name": "Pepperoni Pizza", "description": "A pizza with pepperoni on it", "price": 7.50},
            {"name": "Pineapple Pizza", "description": "A demon coming straight from hell", "price": 666}
        ])
    ]
)
def test_retrieve_menu(restaurant, expected_menu, restaurant_manager_fixture):
    rm = restaurant_manager_fixture
    menu = rm.get_menu(restaurant)
    assert menu == expected_menu