class Coffee:
    def __init__(self,name,price):
        self.name=name
        self.price = price

class Order:
    def __init__(self):
        self.item = [] 

    def add_item(self, coffee: Coffee):
        self.item.append(coffee)
        print(f"Added to your order : ({coffee.name}, price : ${coffee.price:.2f}).")
    
    def total(self):
        sum = 0
        for item in self.item:
            sum+=item.price
        return sum
    
    def show_order(self):
        if not self.item:
            print("No item found. ")
            return 
        for i, item in enumerate(self.item,1):
            print(f"Item {i}, name {item.name}, ${item.price:.2f}")
        print(f"Your total is ${self.total():.2f}. \n")
    
    def check_out(self):
        if not self.item:
            print("Your cart is empty.")
            return
        self.show_order()
        confirm = input("Do you want to remove the order? (yes/no)\n").lower()
        if confirm == 'yes':
            print("Order removed.")
            self.item.clear()
        else:
            print("Checkout cancelled.")

def main():
    menu = [Coffee("Espresso", 2.5),Coffee("Latte",3.5),Coffee("Cappuccino",3.0),Coffee("Americano",2.0)]
    
    oreder = Order()

    while True:
        print("--Coffee menu--")

        for i,coffee in enumerate(menu,1):
            print(f"{i}. coffee name : {coffee.name}, price: ${coffee.price:.2f};")
        
        print("5. view order;")

        print("6. checkout;")

        print("7. exit.")

        choice = input("Choose an option:\n")

        if choice in [ '1', '2' ,'3' ,'4' ]:
            oreder.add_item(menu[int(choice)-1])
        
        elif choice == '5':
            oreder.show_order()

        elif choice == '6':
            oreder.check_out()
        
        elif choice == '7':
            print("Thanks for visiting, goodbye.")
            break
        else: 
            print("Invalid option. Please try again. ")

if __name__ == "__main__":
    main()
