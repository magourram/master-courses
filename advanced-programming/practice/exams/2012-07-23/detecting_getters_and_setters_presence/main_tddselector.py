from tddselector import *
from pprint import pprint as p

class TestClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 0
    def getx(self): return self.x
    def getz(self): return self.z
    def setz(self, x): self.z = x

class TestClass2(TestClass):
    def sety(self, z): self.y=z
    def gety(self): return self.y

ClassesToTest = [ \
    SelectorPresenceTest(TestClass, TestClass(7,25)), \
    SelectorPresenceTest(TestClass2, TestClass2(7,25))
]

if __name__ == "__main__":
    suite = unittest.TestSuite()
    for tc in ClassesToTest:
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(tc))
    unittest.TextTestRunner(verbosity=2).run(suite)
    
