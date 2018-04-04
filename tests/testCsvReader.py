from testStructure import Test
from code.DataProcessors import CsvReader

class TestCsvReader(Test):
    def run(self):
        csvreader = CsvReader.CsvReader("data/smallCsv.csv", [int, int, float])

        grid = csvreader.getGrid()

        self.printResult(len(grid) == 1440) 

testCsvReader = TestCsvReader()
testCsvReader.run()

