DATABASE = {}
def add_pets():
    pet = (input ("Enter the name of the animal:"))
    species =  (input("Enter the specie of the animal:"))
    age =  (input("Enter the age of the animal:"))
    DATABASE[species] = (pet,age)
    print (f"the animal with the name {pet} of the species {species} and the age of {age}.")

def search_pets():
    pet = input ("Enter the specie of the animal: ")
    if pet in DATABASE: 
        species, age = DATABASE[pet]
        print (f"The animal with name {pet} and specie {species} and age {age} It is on the list of base.")
    else: 
        print("the animal not found.")

def filter_by_age():
    min_age = int (input ("Enter the minime age: "))
    max_age = int (input ("Enter the max age: "))
    found = False
    for pet, (species, age) in DATABASE.items():
        print (f"Name: {pet} - Specie: {species} Age: {age}")
        found = True
    if not found: 
        print(f"No animals found within thw age range {min_age} and {max_age}")
        
def view_database():
    print ("DATABASE: ")
    for species, (pet, age) in DATABASE.items():
        print (f"species {species} - name {pet} - Age {age}")

print ("WELCOME TO THE DATABASE!")
print ("1. Add Pets.")
print ("2. Search Pets.")
print ("3. Filter by age.")
print ("4. View Database.") 
print ("5. exit")

while True:
    
 options = input ("SELECT A OPTION (1-5): ")
 if options == "1":
     add_pets()
 elif options == '2':
     search_pets()
 elif options == "3":
     filter_by_age()
 elif options == "4":
     view_database()
 elif options == "5":
     print ("Good bayy!")
     break
 else: 
     print ("Error, please selection a option (1 - 5)")

