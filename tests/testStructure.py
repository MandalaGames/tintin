class Test(object):
    def run(self):
        pass
    def printResult(self, passed):
        if(passed):
            print "test " + self.__class__.__name__ + " succeeded"
        else:
            print "test " + self.__class__.__name__ + " failed"
