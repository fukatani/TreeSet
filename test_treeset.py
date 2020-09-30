import unittest
from treeset import TreeSet

class TestTreeSet(unittest.TestCase):

    def test_treeset(self):
        ts = TreeSet([3,7,2,7,1,3])
        self.assertEqual(ts, [1, 2, 3, 7])

        ts.add(4)
        self.assertEqual(ts, [1, 2, 3, 4, 7])

        ts.add(4)
        self.assertEqual(ts, [1, 2, 3, 4, 7])

        ts.remove(7)
        self.assertEqual(ts, [1, 2, 3, 4])

        ts.remove(5)
        self.assertEqual(ts, [1, 2, 3, 4])

        ts.addAll([3,4,5,6])
        self.assertEqual(ts, [1, 2, 3, 4, 5, 6])

        ts.pop(3)
        self.assertEqual(ts, [1, 2, 3, 5, 6])

        self.assertEqual(ts[0], 1)

        self.assertEqual(ts[-1], 6)

        self.assertTrue(1 in ts)
        self.assertFalse(100 in ts)

        for i, element in enumerate(TreeSet([1,3,1])):
            if i==0:
                self.assertEqual(element, 1)
            elif i==1:
                self.assertEqual(element, 3)
            else:
                raise Exception

        ts_copy = ts.clone()
        self.assertEqual(ts, [1, 2, 3, 5, 6])

        self.assertEqual(ts.floor(4), 3)
        self.assertEqual(ts.ceiling(4), 5)
        self.assertEqual(ts.floor(3), 3)
        self.assertEqual(ts.ceiling(3), 3)

        ts.clear()
        self.assertEqual(ts._treeset, [])
        
        ts = TreeSet([int(x) for x in '934853458236'])
        self.assertEqual(ts.ceiling(100), None)
        self.assertEqual(ts.floor(0), None)

if __name__ == '__main__':
    unittest.main()
