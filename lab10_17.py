#Pablo Perez
#PSID: 1770045
class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0.0, item_quantity=0):
        self.item_name = str(item_name)
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)

    def print_item_cost(self):
        total = int(self.item_quantity * self.item_price)
        print(self.item_name, self.item_quantity, "@ $", end='')
        print(int(self.item_price), "= $", end='')
        print(total)


if __name__ == "__main__":
    # Type main section of code here
    print("Item 1")
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()

    print("Enter the item name:")
    item1.item_name = input()
    print("Enter the item price:")
    item1.item_price = float(input())
    print("Enter the item quantity:")
    item1.item_quantity = int(input())
    print()

    print("Item 2")
    print("Enter the item name:")
    item2.item_name = input()
    print("Enter the item price:")
    item2.item_price = float(input())
    print("Enter the item quantity:")
    item2.item_quantity = int(input())
    print()

    print("TOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()

    total = int(item1.item_price * item1.item_quantity) + int(item2.item_price * item2.item_quantity)
    print()
    print("Total: $" + str(total))