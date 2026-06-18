#!/usr/bin/env python3

class CashRegister:
    """Represents a cash register that tracks items, calculates total, applies discount, and voids transactions."""

    def __init__(self, discount=0):
        """Initializes the CashRegister with a discount percentage (default 0), total, items list, and previous transactions."""
        self._discount = 0  # Setup default first so setter can access it safely
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        """Gets the discount percentage."""
        return self._discount

    @discount.setter
    def discount(self, value):
        """Sets the discount percentage, ensuring it's an integer between 0 and 100 inclusive."""
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        """Adds an item to the register, updating total and recording it in previous_transactions."""
        self.total += price * quantity
        self.total = round(self.total, 10)  # Avoid floating-point issues
        for _ in range(quantity):
            self.items.append(item)
        
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        """Applies the discount percentage to the total, prints success message or error if no discount."""
        if self.discount == 0 or not self.previous_transactions:
            print("There is no discount to apply.")
        else:
            self.total = self.total * (1 - self.discount / 100)
            self.total = round(self.total, 10)  # Avoid floating-point issues
            # Format printed total as integer if it's a whole number, otherwise show it directly
            formatted_total = int(self.total) if self.total == int(self.total) else self.total
            print(f"After the discount, the total comes to ${formatted_total}.")

    def void_last_transaction(self):
        """Voids the last transaction, reversing its impact on total and items."""
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return
        
        last_tx = self.previous_transactions.pop()
        self.total -= last_tx["price"] * last_tx["quantity"]
        self.total = round(self.total, 10)  # Avoid floating-point issues
        
        # Remove the last quantity occurrences of the item from self.items
        for _ in range(last_tx["quantity"]):
            # Since items are appended in order, they'll be at the end, so we pop them
            if self.items and self.items[-1] == last_tx["item"]:
                self.items.pop()
            else:
                # Fallback in case they are not at the end
                if last_tx["item"] in self.items:
                    self.items.remove(last_tx["item"])
