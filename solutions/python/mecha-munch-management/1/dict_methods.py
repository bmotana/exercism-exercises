"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        try:
            current_cart[item] += 1
        except KeyError:
            current_cart[item] = 1

    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    shopping_cart = {
        
    }
    for item in notes:
        shopping_cart[item] = 1

    return shopping_cart
    


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    for update in recipe_updates:
        meal, food = update
        ideas.update({meal: food})
    return ideas





def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    sorted_cart = dict(sorted(cart.items()))

    return sorted_cart


def send_to_store(cart, isle_mapping):
    """Combine users order to isle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param isle_mapping: dict - isle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    for cart_item, quantity in cart.items():
        isle_mapping[cart_item].insert(0, quantity)
    sorted_mapping = dict(sorted(isle_mapping.items()))
    reversed_mapping = reversed(sorted_mapping)
    new_mapping = {item:value for item, value in reversed(sorted_mapping.items())}
    return new_mapping


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for item, item_list in fulfillment_cart.items():
        for _ in range(item_list[0]):
            store_inventory[item][0] -= 1
        if store_inventory[item][0] == 0:
            store_inventory[item][0] = "Out of Stock"
    return store_inventory
        
