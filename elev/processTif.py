from tifffile import imread
import json
import csv
from getElevBounds import getGdalInfo

#from scipy.spatial import Delaunay
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
#import numpy as np 
#from new.coords_to_grid import getGridPosition

def makeMatrix(grid):
    matrix = []

    z = grid 
    for i,line in enumerate(z):
        for j,value in enumerate(line):
            matrix.append([i,j,value])
    return matrix

def makeJson(matrix, tris):
    jsonObj = {"verticesX": [], "verticesY": [], "verticesZ": [], "tris": []}
    for point in matrix:
        jsonObj["verticesX"].append(float(point[0]))
        jsonObj["verticesY"].append(float(point[1]))
        jsonObj["verticesZ"].append(float(-point[2]))
    jsonObj["tris"] = tris
    return jsonObj

def processElevData(filename, outfile, scalefactor, printInfo):

    minLatitude, maxLatitude, minLongitude, maxLongitude = getGdalInfo(filename)
    elevData = imread(filename)

    if (printInfo):
        print "Tiff Info:"
        print filename 
        print " minLatitude, maxLatitude, minLongitude, maxLongitude "
        print minLatitude, maxLatitude, minLongitude, maxLongitude
        print "Size: " + str(len(elevData[0]))+ "x" + str(len(elevData))

    x = range(int(len(elevData[0]) / scalefactor))
    y = range(int(len(elevData) / scalefactor))

    ystart = 2000 
    yend = 2100
    xstart = 2000  
    xend = 2100

    # TODO: Data will be broken into files containing 
    # fileChunkSize x fileChunkSize data points
    fileChunkSize = 100 

    elev = []
    if scalefactor != 1:
        for line in elevData[xstart:xend:scalefactor]:
            elev.append(line[ystart:yend:scalefactor])
        #for line in elevData[::scalefactor]:
            #elev.append(line[::scalefactor])
    else:
        elev = elevData

    if outfile == "":
        f = open(filename.split(".tif")[0] + ".csv", 'w')
    else:
        f = open(outfile + ".csv", 'w')
    w = csv.writer(f)
    w.writerows(elev)
    f.close()

# TODO: move to tools
#hf = plt.figure()
#ha = hf.add_subplot(111, projection='3d')

#X, Y = np.meshgrid(x, y)  # `plot_surface` expects `x` and `y` elev to be 2D
#ha.plot_surface(X, Y, elev)

#plt.show()


    matrix = makeMatrix(elev)

    matLen = len(elev[0])
    tris = []

    elevSlopeTiles = list(elev)
    elevTiles = list(elev)

    for i,row in enumerate(elev[:-1]):
        for j,item in enumerate(row[:-1]):
            index = i*matLen + j
            # first triangle:
            tris.append( index )        
            # x .
            # .
            tris.append(index + 1)           
            # . x
            # .
            tris.append(index + matLen)          
            # . .
            # x      

            # second triangle:
            tris.append(index + 1)         
            tris.append(index + matLen + 1)
            tris.append(index + matLen )

    for i,row in list(enumerate(elevSlopeTiles))[::2]:
        for j,col in list(enumerate(row))[::2]:
            elevSlopeTiles[i+1][j] = elevSlopeTiles[i][j]
            elevSlopeTiles[i+1][j+1] = elevSlopeTiles[i][j]
            elevSlopeTiles[i][j+1] = elevSlopeTiles[i][j]

    slopeTileMatrix = makeMatrix(elevSlopeTiles)

    savedPt = elevTiles[0][0]
    for i,row in enumerate(elevTiles[:-1]):
        for j,col in enumerate(row[:-1]):
            savedPt = elevTiles[i][j+1]
            elevTiles[i+1][j] = savedPt
            elevTiles[i+1][j+1] = savedPt
            elevTiles[i][j+1] = savedPt


    tileMatrix = makeMatrix(elevTiles)

    jsonObj = makeJson(matrix, tris)
    if outfile == "":
        f = open(filename.split('.')[0] + '.json', 'w')
    else:
        f = open(outfile + '.json', 'w')

    f.write(json.dumps(jsonObj))
    f.close()

    jsonObj2 = makeJson(slopeTileMatrix, tris)
    if outfile == "":
        f = open(filename.split('.')[0] + '_slope_tiles.json', 'w')
    else:
        f = open(outfile + '_slope_tiles.json', 'w')

    f.write(json.dumps(jsonObj2))
    f.close()

    jsonObj3 = makeJson(tileMatrix, tris)
    if outfile == "":
        f = open(filename.split('.')[0] + '_tiles.json', 'w')
    else:
        f = open(outfile + '_tiles.json', 'w')

    f.write(json.dumps(jsonObj3))
    f.close()

    #print (matrix)
    #print (tris)
