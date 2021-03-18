import dist
import indexer
import distance
import stationVariable

# Method to display distance between stations:
def display():
    print()
    print("Origin      :",stationVariable.origin)
    print('            |')
    print('            |')
    print('            ----------->>','Distance: ',distance.distance(stationVariable.origin,stationVariable.destination),'Kilometers')
    print('            |')
    print('            |')
    print("Destination :",stationVariable.destination)

# Calling Display Function:
display()