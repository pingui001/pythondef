#Sistema de calificación de películas:

#Añadir películas
#Registrar calificaciones (1–5)
#Calcular promedio de calificación
movies = {}

def Addmovie(Name):
    if Name in movies:
        print(f" The movie {Name} has already been recorded")
    else:
        movies[Name] = []
        print(f"movie {Name} added successfully.")

def RegisterRating(Name, qualification):
    if Name not in movies:
        print(f"the movie {Name} is not registered.")
    elif not 1 <= qualification <= 5:
        print("The rating must be between 1 and 5.")
    else:
        movies[Name].append(qualification)
        print(f"qulificacion {qualification} added to {Name}.")

def calculateaverage(Name):
    if Name not in movies:
        print(f"The movie {Name} is not registered.")
    elif not movies[Name]:
        print(f"ℹthe movie {Name} has no ratings yet.")
    else:
        average = sum(movies[Name]) / len(movies[Name])
        print(f"Average grade for {Name}: {average:.2f}")

while True:
    option = input("Select the option you want to perform:\n 1. Add movie\n 2. Record rating\n 3. Calculate average rating\n 4. Exit: ")

    if option == "1":
        Name = input("Enter the name of the movie: ")
        Addmovie(Name)

    elif option == "2":
        Name = input("Enter the name of the movie: ")
        try:
            qualification = int(input("Enter the rating (1 to 5): "))
            RegisterRating(Name, qualification)
        except ValueError:
            print("The grade must be an integer.")

    elif option == "3":
        Name = input("Enter the name of the movie: ")
        calculateaverage(Name)

    elif option == "4":
        print("exit the menu")
        break

    else:
        print("the option is not valid")