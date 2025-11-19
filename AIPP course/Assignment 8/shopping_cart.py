class ShoppingCart:
    def __init__(self): self.items = {}
    def add_item(self, name, price): self.items[name] = self.items.get(name, 0) + price
    def remove_item(self, name): self.items.pop(name, None)
    def total_cost(self): return sum(self.items.values())

if __name__ == "__main__":
    c = ShoppingCart()
    c.add_item("apple", 1.5); c.add_item("banana", 2.0)
    print(f"Test: add_item('apple', 1.5), add_item('banana', 2.0) | total_cost() = ${c.total_cost()}")
    c.remove_item("apple")
    print(f"Test: remove_item('apple') | total_cost() = ${c.total_cost()}")
    c.add_item("banana", 2.0)
    print(f"Test: add_item('banana', 2.0) | total_cost() = ${c.total_cost()}")
    print("Full class with tested functionalities\n")
    cart = ShoppingCart()
    while True:
        cmd = input("Enter command (add name price/remove name/total/quit): ").split()
        if cmd[0] == "add" and len(cmd) == 3: cart.add_item(cmd[1], float(cmd[2])); print(f"Added {cmd[1]}: ${cmd[2]}, Total: ${cart.total_cost()}")
        elif cmd[0] == "remove" and len(cmd) == 2: cart.remove_item(cmd[1]); print(f"Removed {cmd[1]}, Total: ${cart.total_cost()}")
        elif cmd[0] == "total": print(f"Total: ${cart.total_cost()}")
        elif cmd[0] == "quit": break
