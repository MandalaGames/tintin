import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
from scipy.spatial import Delaunay
import json
import csv
from coords_to_grid import getGridPosition
from Parsers import Fuji, FortCollins

args = sys.argv
filename = args[1]

elev,x,y= Fuji.parse(args)

def plotData():
    hf = plt.figure()
    ha = hf.add_subplot(111, projection='3d')

    X, Y = np.meshgrid(x, y)  # `plot_surface` expects `x` and `y` elev to be 2D
    ha.plot_surface(X, Y, elev)

    plt.show()

def makeMatrix(grid): # ! how grid is structured: just matrix of elev values
    matrix = []

    z = grid 
    for i,line in enumerate(z):
        for j,value in enumerate(line):
            matrix.append([i,j,value])
    return matrix

matrix = makeMatrix(elev)

#print(matrix)

plotData()

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

def makeJson(matrix, tris):
    jsonObj = {"verticesX": [], "verticesY": [], "verticesZ": [], "tris": []}
    for point in matrix:
        jsonObj["verticesX"].append(float(point[0]))
        jsonObj["verticesY"].append(float(point[1]))
        jsonObj["verticesZ"].append(float(-point[2]))
    jsonObj["tris"] = tris
    return jsonObj

jsonObj = makeJson(matrix, tris)
f = open(filename.split('.')[0] + '.json', 'w')
f.write(json.dumps(jsonObj))
f.close()

jsonObj2 = makeJson(slopeTileMatrix, tris)
f = open(filename.split('.')[0] + '_slope_tiles.json', 'w')
f.write(json.dumps(jsonObj2))
f.close()

jsonObj3 = makeJson(tileMatrix, tris)
f = open(filename.split('.')[0] + '_tiles.json', 'w')
f.write(json.dumps(jsonObj3))
f.close()

f = open("gridexport.csv", 'w')
w = csv.writer(f)
w.writerows(elev)
f.close()

f = open("stuffAroundFuji.json")
store_locations = json.loads(f.read())
f.close()

latMin = 35 
latMax = 36
lngMin = 138
lngMax = 139

shopInfo = {"names": [], "xcoords": [], "ycoords": []}
for item in store_locations["results"]:
    shopInfo["names"].append(item["name"])
    loc =  item["geometry"]["location"]
    gridPos = (getGridPosition(elev, loc["lat"], loc["lng"], latMin, latMax, lngMin, lngMax))
    shopInfo["xcoords"].append(gridPos[0])
    shopInfo["ycoords"].append(gridPos[1])

f = open("shop_info.json", 'w')
f.write(json.dumps(shopInfo))
f.close()

print("mt fuji")
print(getGridPosition(elev,35.3618,138.7298, latMin, latMax, lngMin, lngMax))


def delaunayTris(): # not relevant
    tris = Delaunay(matrix)

    pfile = open('points.cs','w')
    tfile = open('tris.cs','w')
    p=''
    t=''
    for point in tris.points:	
        p += "new Vector3(" + str(point[0]) + ',' + str(point[1]) + ',' + str(point[2]) + '),\n'
    pfile.write(p)
    pfile.close()

    for simplex in tris.simplices:	
        t += str(simplex[0]) + ',' + str(simplex[1]) + ',' + str(simplex[2]) + ',' 
    tfile.write(t)
    tfile.close()
