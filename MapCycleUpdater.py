import os

def scanForMaps():
    maps = [] 
    for root, dirs, files, in os.walk('D:\steamCMD\csgo\csgo\maps'):
        for file in files:
            if file.endswith('.bsp'):
                maps.append(file.removesuffix('.bsp'))
    maps.sort()
    return maps

def scanMapCycle():
    mapCycleMaps = []
    with open('D:\steamCMD\csgo\csgo\mapcycle.txt', 'r') as file:
        for line in file:
            mapCycleMaps.append(line.rstrip())
    mapCycleMaps.sort()
    return mapCycleMaps

mapCycleMaps = scanMapCycle()
maps = scanForMaps()

                
def compareMaps():
    diff = []

    for element in maps:
        if element not in mapCycleMaps:
            diff.append(element)

    return diff

diff = compareMaps()


def updateMapCycle():
    with open('D:\steamCMD\csgo\csgo\mapcycle.txt', 'a') as file:
        for line in diff:
            file.write("\n" + line)
    


updateMapCycle()
