
from navigationLocBook import locationManager # import custom module

def main():
    manager = locationManager()
    manager.loadLocations() 
    
    while True:
        # print out differnt options
        print("1. View All")
        print("2. Add a New Location")
        print("3. Search a Location")
        print("4. Exit")
        choice = input("Pick between 1-4): ")

        if choice == "1":
            manager.displayLocation() # displays all locations
            break
        elif choice == "2":
            # ask user for new locations
            name = input("Enter location name: ")
            lat = input("Enter latitude: ")
            lon = input("Enter longitude: ")
            manager.saveLocation(name, lat, lon)
            break
        elif choice == "3":
            searchName: str = input("Enter name to search: ") #enter location 
            manager.searchLocation(searchName)
            break
        elif choice == "4": # exit 
            break
        else:
            print("\nInvalid choice, please try again.\n")

if __name__ == "__main__": # runs main()
    main()
