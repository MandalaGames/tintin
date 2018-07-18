from tifffile import imread


def parse(args):
#filename = input('filename?')
    filename = args[1]

    scalefactor = 1

    if len(args) > 2:
        scalefactor = int(args[2])

    if len(args) == 7:
        xMin = int(args[3])
        xMax = int(args[4])
        yMin = int(args[5])
        yMax = int(args[6])

    print(filename)
    elevData = imread(filename)

    x = range(int(len(elevData[0]) / scalefactor))
    y = range(int(len(elevData) / scalefactor))

    elev = []
    if scalefactor != 1:
        if len(args) == 7:
            for line in elevData[xMin:xMax:scalefactor]:
                elev.append(line[yMin:yMax:scalefactor])
        else:
            for line in elevData[::scalefactor]:
                elev.append(line[::scalefactor])

    else:
        elev = elevData
    return elev,x,y
