import unittest

from src.ds.min_pq_pr import MinPQPR


class TestMinPQPR(unittest.TestCase):

    def test_constructor_shouldCreateEmptyPQ(self):
        self.assertEqual(0, MinPQPR().size())

    def test_insert_withTimeAlwaysInPresent_shouldBehaveAsEphemeralMinPQ(self):
        pq = MinPQPR()
        for i in range(1, 20):
            pq.insert(-i, i)
            self.assertEqual(-i, pq.min())
            self.assertEqual(i, pq.size())
            self.assertEqual(i, len(pq))

        for i in range(1, 20):
            self.assertEqual(-20 + i, pq.delete_min(19 + i))
            self.assertEqual(19 - i, pq.size())

    def test_insert_withDifferentTimes_shouldInsertItemAndPropagateChanges(self):
        pq = MinPQPR()

        for i in range(1, 20):
            pq.insert(-i, i)

        for i in range(1, 20):
            pq.insert(-19 -i, i + 0.5)
            self.assertEqual(-19 -i, pq.min())
            self.assertEqual(19 + i, pq.size())

        pq.insert(-90, -90)
        self.assertEqual(-90, pq.min())

    def test_deleteMin_withEmptyPQInEveryTime_shouldReturnNone(self):
        pq = MinPQPR()
        for i in range(-20, 20):
            self.assertIsNone(pq.delete_min(i))

    def test_deleteMin_withTimeAlwaysInPresent_shouldBehaveAsEphemeralMinPQ(self):
        pq = MinPQPR()
        for i in range(1, 20):
            pq.insert(-i, i)

        for i in range(1, 20):
            self.assertEqual(-20 + i, pq.delete_min(19 + i))
            self.assertEqual(19 - i, pq.size())

    def test_deleteMin_withDifferentTimes_shouldDeleteMinAndPropagateChanges(self):
        pq = MinPQPR()
        for i in range(1, 20):
            pq.insert(-i, i)

        for i in range(19, 0, -1):
            pq.delete_min(i + 0.5)
            if i == 1:
                self.assertIsNone(pq.min())
            else:
                self.assertEqual(-i + 1, pq.min())
            self.assertEqual(i - 1, pq.size())

        pq = MinPQPR()
        for i in range(1, 20):
            pq.insert(-i, i)

        for i in range(1, 20):
            pq.delete_min(i + 0.5)
            if i == 19:
                self.assertIsNone(pq.min())
            else:
                self.assertEqual(-19, pq.min())
            self.assertEqual(19 - i, pq.size())



