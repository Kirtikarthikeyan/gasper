class PoultryShop:
    def _init_(self, total_chickens):
        self.chicken_weight = 1.6
        self.leg_weight = 0.2 
        self.wing_weight = 0.2  
        self.flesh_weight = 0.8  
        self.total_legs = total_chickens * 2 
        self.total_wings = total_chickens * 2 
        self.total_flesh = total_chickens * 1 
        self.total_chickens = total_chickens
    def process_order(self, order_legs, order_wings, order_flesh):
        order_legs_weight = order_legs * self.leg_weight
        order_wings_weight = order_wings * self.wing_weight
        order_flesh_weight = order_flesh * self.flesh_weight
        total_order_weight = order_legs_weight + order_wings_weight + order_flesh_weight
        chickens_needed = max(
            (order_legs + 1) // 2,
            (order_wings + 1) // 2,
            order_flesh
        )
        if order_legs > self.total_legs or order_wings > self.total_wings or order_flesh > self.total_flesh:
            print("Not enough inventory to fulfill the order.")
            return
        self.total_legs -= order_legs
        self.total_wings -= order_wings
        self.total_flesh -= order_flesh
        remaining_legs = self.total_legs
        remaining_wings = self.total_wings
        remaining_flesh = self.total_flesh
        total_remaining_weight = (
            remaining_legs * self.leg_weight +
            remaining_wings * self.wing_weight +
            remaining_flesh * self.flesh_weight
        )
        print("\nOrder Summary:")
        print(f"Total order weight: {total_order_weight} kg")
        print(f"Chickens required to fulfill order: {chickens_needed}")
        print(f"Remaining Legs: {remaining_legs}, Remaining Wings: {remaining_wings}, Remaining Flesh Portions: {remaining_flesh}")
        print(f"Total remaining inventory weight: {total_remaining_weight} kg")
    def get_inventory(self):
        return {
            "legs": self.total_legs,
            "wings": self.total_wings,
            "flesh": self.total_flesh,
            "chickens": self.total_chickens,
        }
if _name_ == "_main_":
    shop = PoultryShop(total_chickens=12)
    shop.process_order(order_legs=24, order_wings=13, order_flesh=7)
    print("\nRemaining Inventory:")
    inventory = shop.get_inventory()
    print(f"Legs: {inventory['legs']}, Wings: {inventory['wings']}, Flesh Portions: {inventory['flesh']}, Chickens: {inventory['chickens']}")