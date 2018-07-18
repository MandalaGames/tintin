# Input: latitude, longitude, scale factor
# Output: index in grid, distance from (0,0) in square


def getGridPosition(grid, lat, lng, latMin, latMax, longMin, longMax ): # lat/long min and max are the maximum / minimum geo points in the grid
    gridRows = len(grid)
    gridCols = len(grid[0])
    latStep = (latMax - latMin) / gridRows
    lngStep = (longMax - longMin) / gridCols

    row = ((1 - (lat - latMin)) / latStep)
    col = ((lng - longMin) / lngStep)

    return row, col
