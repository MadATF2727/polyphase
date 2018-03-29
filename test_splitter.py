import unittest
import splitter

class testSplitter(unittest.TestCase):

    def test_split(self):
        '''ensure the signal is split properly'''
        testSig = range(27)
        M = 5
        arr = splitter.fillSigArray(testSig, M)
        rows = len(arr)
        cols = len(arr[0])
        self.assertEqual(M, rows)
        self.assertEqual(6, cols)

if __name__ == "__main__":
    unittest.main()