import subprocess
import re


# Input: tif filename
# Output: Min and max latitude and longitude
def getGdalInfo(tifFilename):
    try:
        out = subprocess.Popen(["gdalinfo", tifFilename], stdout=subprocess.PIPE)
    except OSError:
        print "Error running gdalinfo! Do you have gdalinfo installed?"
    tifOutput = out.stdout.read()
    for line in tifOutput.split("\n"):
        # flags for upper left and lower right:
        ul = False
        lr = False
        line = line.lower() # lower case
        if("upper left") in line:
            content = line.split("upper left")[1].strip(" ")
            ul = True
        elif("lower right") in line:
            content = line.split("lower right")[1].strip(" ")
            lr = True
        else: 
            continue

        rePatternOne = '''\(\ * 
                        (
                        .*?\..*?
                        )
                        ,''' 

        rePatternTwo = ''',\ * 
                        (
                        .*?\..*?
                        )
                        \)''' 
        p1 = re.compile(rePatternOne, re.VERBOSE)
        p2 = re.compile(rePatternTwo, re.VERBOSE)
        longitude = p1.findall(content)[0]
        latitude = p2.findall(content)[0]

        print  "latitude ",latitude,"longitude ", longitude, ul, lr

        if(ul):
            minLatitude = float(latitude)
            maxLongitude = float(latitude)
        elif(lr):
            maxLatitude = float(latitude)
            minLongitude = float(longitude)
    print minLatitude, maxLatitude, minLongitude, maxLongitude
