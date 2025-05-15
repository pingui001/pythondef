#Seguimiento de cajas en un almacén:
#
#    Añadir tipos de caja
#    Actualizar cantidades
#    Verificar si hay cantidad suficiente

#añadir diferentes tipos de cajas
#actualizar la cantidad de cajas que hay por un tipo
#verificar si hay cantidad suficiente, pidiendo por ejemplo una cantidad de cajas que se necesita
def ask_number(message, kind="int"):
    while True:
        try:
            if kind == "int":
                return int(input(message))
            elif kind == "float":
                return float(input(message))
        except ValueError: 
            print("The entered value is invalid. Please try again.")

def menu_option():
    print("1. Add a box type")
    print("2. Update quantities")
    print("3. Check if there is sufficient quantity")
    print("4. View all box quantities")
    print("5. Exit the program")

def main():
    boxes = {}
    while True:
        menu_option()
        option = input("Select an option: ")

        if option == "1":
            print("Add a type of box to save")
            name = input("Add a box type: ")
            quantity = ask_number("Add the quantity of boxes: ")
            if quantity < 0:
                print("Negative numbers are not allowed, please try again.")
            else:
                boxes[name] = {"Name": name, "Quantity": quantity}
                print(f"Added box: {name}, Quantity: {quantity}")

        elif option == "2":
            print("Quantity update")
            name = input("Enter the name of the box type to update: ")
            if name in boxes:
                new_quantity = ask_number("Enter the new quantity of the box: ")
                if new_quantity < 0:
                    print("Negative numbers are not allowed, please try again.")
                else:
                    boxes[name]['Quantity'] = new_quantity
                    print(f"Updated quantity for {name}: {new_quantity}")
            else:
                print(f"Box type {name} not found.")

        elif option == "3":
            print("Check if there is sufficient quantity")
            name = input("Enter the name of the box type: ")
            if name in boxes:
                need = ask_number("Write the number of boxes you need: ")
                if need < 0:
                    print("Negative numbers are not allowed, please try again.")
                elif boxes[name]['Quantity'] >= need:
                    print(f"There are enough {name} boxes available ({boxes[name]['Quantity']} available).")
                else:
                    print(f"Not enough {name} boxes available ({boxes[name]['Quantity']} available).")
            else:
                print(f"Box type {name} not found.")

        elif option == "4":
            print("Current box quantities:")
            if boxes:
                for name, info in boxes.items():
                    print(f"Box type: {name}, Quantity: {info['Quantity']}")
            else:
                print("No box types registered.")

        elif option == "5":
            print("Exiting the program")
            break       
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()








