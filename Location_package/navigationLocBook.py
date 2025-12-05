import os
from typing import List, Dict, Optional

#define a class to manage locations
class locationManager:
    def __init__(self, locations:Optional[List[Dict[str, str]]] = None, fileName: str = 'locations.txt') -> None:
        self.fileName = fileName
        self.locations = locations if locations is not None else []

    def loadLocations(self) -> None:
        
        if not os.path.exists(self.fileName): # checks to see if there is an exsiting file 
            print("No existing location file found. Starting new list.\n")
            self.locations = []
            return
    
        try:
            with open(self.fileName, 'r') as locFile:  # open the file 
                self.locations = []
                lines = locFile.readlines()
                for line in lines:
                    name, lat, lon = line.strip().split(',') # split with a comma
                    self.locations.append({"name": name, "lat": lat, "lon": lon}) 
        except FileNotFoundError:
            self.locations = []

    def saveLocation(self, name: str, lat: str, lon: str) -> None:  
    
        with open(self.fileName, 'a') as locFile: 
            locFile.write(f"{name},{lat},{lon}\n")
        self.locations.append({"name": name, "lat": lat, "lon": lon}) #add locations
        print(f"\n Location '{name}' added successfully!\n")

    def displayLocation(self) -> None:
        if not self.locations:
            print("No locations found.")
        else:
            print("\n Saved Locations:")
            for loc in self.locations:
                print(f"Name: {loc['name']} | Latitude: {loc['lat']} | Longitude: {loc['lon']}")
        print()

    def searchLocation(self, searchName: str) -> None:
        found = False
        for loc in self.locations:
            if loc['name'].lower() == searchName.lower():#use lower case letter to check location
                print(f"Found: {loc['name']} | Latitude: {loc['lat']} | Longitude: {loc['lon']}")
                found = True
                break
        if not found:
            print("Location not found.\n")
