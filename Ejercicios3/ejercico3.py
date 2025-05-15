# 3. Restaurant Menu Editor
dishes=[]
price=[]
availability=[]
def main():
    menu()
def menu():
    while True:
        try:
            opcion=int(input(("choose a opcion. \n.1 add dish \n.2 change availability \n.3 total price of the available dishes \n.4 exit")))
            
            if opcion==1:
                add_dish()
            elif opcion==2:
                change_availability()
                
            elif opcion==3:
                total_available_price()

            elif opcion==4:
                break
        except ValueError:
            print("invalid value")

def add_dish(): 
    n=input("enter the name of the dish:")
    p=int(input("enter the price of the product:"))
    availability1=input("enter the availability of the dish: yes|no:")
    dishes.append(n)
    price.append(p)
    availability.append(availability1)
    print("the dish has been added")
def change_availability(): 
    name=input("enter the dish to search for it: ")
    for i in range(len(dishes)):
        if dishes[i]==name:
            if availability[i]=="yes":
                availability[i]="no"
                print("the availability has been changed")
                break
            elif availability[i]=="no":
                availability[i]="yes"    
                print("the availability has been changed")
                break
        
def total_available_price(): 
    acumulator=0
    for i in range(len(dishes)):
        if availability[i]=="yes":
            acumulator+=price[i]
    print(f"the total value of the dishes with availability is: {acumulator}")
    
main()