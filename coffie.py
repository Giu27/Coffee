class Coffie:
    def __init__(self,name,price):
        self.name=name
        self.price = price

class Order:
    def __init__(self):
        self.item = [] 

    def add_item(self, coffie: Coffie):
        self.item.append(coffie)
        print(f"Added  to your order : ({coffie.name}  , price : {coffie.price})")
    
    def total(self):
        sum = 0
        for item in self.item:
            sum+=item.price
        return sum
    
    def show_order(self):
        if not self.item:
            print(" No item found ")
            return 
        for i, item in enumerate(self.item,1):
            print(f" item {i} , name {item.name}, ${item.price}")
        print(f"your total is {self.total()} \n")
    
    def check_out(self):
        if not self.item:
            print("your cart is empty ")
            return
        self.show_order()
        confirm = input("You want to remove the order  ? (yes/no)\n").lower()
        if confirm == 'yes':
            print("Order removed")
            self.item.clear()
        else:
            print("checkout cancelled ")

def main():
    menu = [Coffie("Espresso ", 2.5),Coffie("Latte",3.5),Coffie("Capuccino",3.0),Coffie("Americano",2.0)]
    
    oreder = Order()

    while True:
        print("--Coffie menu --")

        for i,coffiee in enumerate(menu,1):
            print(f"{i}. coffie name : {coffiee.name}, coffie price {coffiee.price}")
        
        print("5. view order")

        print("6. checkout")

        print("7. exit")

        choice = input("Choose an option:\n ")

        if choice in [ '1', '2' ,'3' ,'4' ]:
            oreder.add_item(menu[int(choice)-1])
        
        elif choice == '5':
            oreder.show_order()

        elif choice == '6':
            oreder.check_out()
        
        elif choice == '7':
            print("Thanks for visiting, goodbye")
            break
        else: 
            print("Invalid option. Try againg ")

if __name__ == "__main__":
    main()
