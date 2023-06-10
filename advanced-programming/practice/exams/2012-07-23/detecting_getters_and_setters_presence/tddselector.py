import unittest
from collections import defaultdict
from pprint import pprint as p

def SelectorPresenceTest(cls, instance):
    class SelectorPresenceTestInner(unittest.TestCase):
        def create_setters(self):
            self.setters = defaultdict()
            for name_attr, _ in instance.__dict__.items():
                self.setters[name_attr] = hasattr(cls, "set" + name_attr)
            self.setters = [i for i in self.setters.values()]

        def create_getters(self):
            self.getters = defaultdict()
            for name_attr, _ in instance.__dict__.items():
                self.getters[name_attr] = hasattr(cls, "get" + name_attr)
            self.getters = [i for i in self.getters.values()]

        def test_setters(self):
            self.create_setters()
            self.assertTrue(all(self.setters), '[SETTERS]')

        def test_getters(self):
            self.create_getters()
            self.assertTrue(all(self.getters), '[GETTERS]')

    return SelectorPresenceTestInner
