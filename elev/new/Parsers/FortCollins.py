import sys, re, math
with open(sys.argv[2]) as f:
    data = f.readlines()

longitude = []
latitude = []
elevation = []

for line in data:
    items = re.split("\t", line)
    try:
        longitude.append(float(items[0]))
        latitude.append( float(items[1]))
        elevation.append( float(items[2]))
    except ValueError:
        continue

longMin = min(longitude)
latMin = min(latitude)
# output json file ?
# ultimately pass to generateTris
lngRange = max(longitude) - longMin
latRange = max(latitude) - latMin

x = [math.floor((lng - longMin) * len(longitude) / lngRange)  for lng in longitude]
y = [math.floor((lat - latMin) * len(latitude) / lngRange) for lat in latitude]


grid = [[0 for i in range(int(max(longitude)))] for j in range(int(max(latitude)))]

def findElev(i,j):
    for index in x:
        index = int(index)
        try:
            if x[index] == i and y[index] == j:
                return elevation[index]
        except IndexError:
            continue


for i in range(int(max(longitude))):
    for j in range(int(max(latitude))):
        grid[j][i] = findElev(j,i)

print(grid)
