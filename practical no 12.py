#store GPS coordinates in a tuple
location = (18.5204, 73.8567)

print("GPS Location:", location)

#Indexing
print("Latitude:", location[0])
print("Longitude:", location[1])
#tuple oprations
print("Number of coordinates:", len(location))

#acces first element using nagative indexing
print("First coordinate:",location[0])

#acces last element using nagative indexing
print("Last coordinate:", location[-1])
#check whether a coordinate  exit
print("Is latitude 18.5204 present?", 18.5204 in location)

#tuple slicing
print("Coordinates using slicing:", location[0:2])
#concatenation
extra = ("Pune",)
new_location = location + extra

print("Location with city:", new_location)
#repetition
print("Repeated coordinates:", location * 2)