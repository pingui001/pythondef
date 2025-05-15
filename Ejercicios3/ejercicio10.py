# 10. Gym Membership System
gym={
    "members":[],
    "plan":[],
    "paystatus":[]
    
    }
def main():
    menu()
def menu():
    while True:
        print("1. Register member")
        print("2. Change member plan")
        print("3. Show unpaid members")
        print("4. Exit")

        try:
            option = int(input("Choose an option: "))
            if option == 1:
                register_member()
            elif option == 2:
                change_plan()
            elif option == 3:
                unpaid_members()
            elif option == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid option.")
        except ValueError:
            print("Please enter a valid number.")
def register_member():
    member=input("name of the member: ")
    plan=input("type of plan can be:(normal,fit,pro)")
    paystatus=input("status of the membership can be:(paid,unpaid)")
    gym["members"].append(member); gym["plan"].append(plan); gym["paystatus"].append(paystatus)
    print("member added")
def change_plan(): 
    name=input("what member you wanna change his plan: ")
    if name in gym["members"]:
        position=gym["members"].index(name)
        new_plan=input("enter the new plan of the member can be:(normal,fit,pro) ")
        gym["plan"][position]=new_plan
    else:
        print("member does not exists ")
    

def unpaid_members(): 
    unpaid = []
    for i in range(len(gym["members"])):
        if gym["paystatus"][i]=="unpaid":
            unpaid.append(gym["members"][i])
            
    print(f"the unpaidmebers are {unpaid}")   

        
main()       