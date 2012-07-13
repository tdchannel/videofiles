import unittest

from pytracer.core import PtBucket

class PtBucketTest(unittest.TestCase):
    def test_bwSquare(self):
        b = PtBucket.PtBucketWorker()
        b.calculateBuckets(320,320,32)
        self.assertEqual(b.numx, 10)
        self.assertEqual(b.numy, 10)
        self.assertEqual(b.buckets[-1].pos.x, 288)
        self.assertEqual(b.buckets[-1].pos.y, 288)

    def test_bwWide(self):
        b = PtBucket.PtBucketWorker()
        b.calculateBuckets(320,240,32)
        self.assertEqual(b.numx, 10)
        self.assertEqual(b.numy, 8)
        self.assertEqual(b.buckets[-1].pos.x, 288)
        self.assertEqual(b.buckets[-1].pos.y, 224)

    def test_bwTall(self):
        b = PtBucket.PtBucketWorker()
        b.calculateBuckets(240,320,32)
        self.assertEqual(b.numx, 8)
        self.assertEqual(b.numy, 10)
        self.assertEqual(b.buckets[-1].pos.x, 224)
        self.assertEqual(b.buckets[-1].pos.y, 288)

if __name__ == '__main__':
    unittest.main()
