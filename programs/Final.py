#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      students07
#
# Created:     11/12/2012
# Copyright:   (c) students07 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# Hotel Simulation

def numberOfFloors():
    global floors
    floors = int(input("Please enter the number of floors in the hotel"))
    return (floors)

def roomsPerFloor(floors):
    global rooms
    global occupied
    occupiedRatio = 0
    totalOccupied = 0
    totalVacant = 0
    for x in range (floors):
        rooms = int(input("Please enter the number of rooms on this floor"))
        occupied = int(input("Please enter the number of occupied rooms on this floor"))
        occupiedRatio = int((occupied/rooms) * 100)
        totalOccupied += occupied
        totalVacant = rooms - occupied
        if(rooms <5):
            rooms = int(input("Please enter the number of rooms on this floor"))
    print("Ratio Occupied: " + str(occupiedRatio))
    print("Total rooms occupied: " + str(totalOccupied))
    print("Total rooms vacant: " + str(totalVacant))

    return(rooms, occupied ,occupiedRatio)

numberOfFloors()
roomsPerFloor(floors)