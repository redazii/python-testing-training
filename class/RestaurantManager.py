class RestaurantManager:
    def __init__(self):
        self.restaurant_data = {}

    def find_restaurant(self, restaurant_name):
        if restaurant_name not in self.restaurant_data:
            raise UnknownRestaurant(f"{restaurant_name} n'existe pas.")
        return self.restaurant_data[restaurant_name]

    def create_restaurant(self, restaurant_name):
        if restaurant_name in self.restaurant_data:
            raise RestaurantExists(f"{restaurant_name} existe déjà.")
        self.restaurant_data[restaurant_name] = {"menu": {}}
        return self

    def remove_restaurant(self, restaurant_name):
        if restaurant_name not in self.restaurant_data:
            raise UnknownRestaurant(f"{restaurant_name} n'existe pas.")
        del self.restaurant_data[restaurant_name]
        return self

    def add_menu_item(self, restaurant_name, item_name, description, price):
        if price < 0:
            raise InvalidPrice("Le prix doit être positif.")
        if restaurant_name not in self.restaurant_data:
            raise UnknownRestaurant(f"{restaurant_name} n'existe pas.")
        if item_name in self.restaurant_data[restaurant_name]['menu']:
            raise MenuItemExists(f"{restaurant_name} a déjà {item_name} dans le menu.")
        self.restaurant_data[restaurant_name]["menu"][item_name] = {"description": description, "price": price}
        return f"{item_name} ajouté au menu de {restaurant_name}."

    def get_menu(self, restaurant_name):
        if restaurant_name not in self.restaurant_data:
            raise UnknownRestaurant(f"{restaurant_name} n'existe pas.")
        menu = []
        for item_name, item_info in self.restaurant_data[restaurant_name]["menu"].items():
            menu.append({"nom": item_name, "description": item_info["description"], "prix": item_info["price"]})
        return menu

    def update_menu_item(self, restaurant_name, item_name, description, price):
        if price < 0:
            raise InvalidPrice("Le prix doit être positif.")
        if restaurant_name not in self.restaurant_data:
            raise UnknownRestaurant(f"{restaurant_name} n'existe pas.")
        if item_name not in self.restaurant_data[restaurant_name]['menu']:
            raise UnknownMenuItem(f"{restaurant_name} n'a pas {item_name} dans le menu.")
        self.restaurant_data[restaurant_name]["menu"][item_name] = {"description": description, "price": price}
        return f"{item_name} mis à jour dans le menu de {restaurant_name}."

    def delete_menu_item(self, restaurant_name, item_name):
        if restaurant_name not in self.restaurant_data:
            raise UnknownRestaurant(f"{restaurant_name} n'existe pas.")
        if item_name not in self.restaurant_data[restaurant_name]['menu']:
            raise UnknownMenuItem(f"{restaurant_name} n'a pas {item_name} dans le menu.")
        del self.restaurant_data[restaurant_name]["menu"][item_name]
        return f"{item_name} retiré du menu de {restaurant_name}."


class UnknownRestaurant(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class RestaurantExists(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class UnknownMenuItem(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class MenuItemExists(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class InvalidPrice(Exception):
    def __init__(self, *args):
        super().__init__(*args)