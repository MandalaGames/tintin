
def jsonToCsv(data, resolution):
    outData = ""
    for i,z in enumerate(data["verticesZ"][::resolution]):
        index = i * resolution
        x = data["verticesX"][index]
        y = data["verticesY"][index]
        outData += str(x) + "," + str(y) + "," +str(z) + "\n"
    return outData
